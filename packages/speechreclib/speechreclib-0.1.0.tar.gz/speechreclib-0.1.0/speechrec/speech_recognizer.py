import os
import tempfile
from abc import ABC, abstractmethod
from typing import Any

import torch
import whisper


class SpeechRecognizer(ABC):

    @abstractmethod
    def recognize(self, audio_data: bytes) -> str:
        raise NotImplementedError


class WhisperRecognizer(SpeechRecognizer):
    def __init__(self, model_name: str = "tiny") -> None:
        """Инициализирует распознаватель Whisper.

        Parameters:
            model_name: Имя модели Whisper (например, "tiny", "base", "small").
        """
        self._model_name = model_name

    def recognize(self, audio_data: bytes) -> str:
        """Распознаёт речь из WAV/MP3 байтов, используя openai-whisper.

        Parameters:
            audio_data: Сырые байты аудио. Поддерживаются WAV (PCM) и MP3.

        Returns:
            str: Распознанный текст.

        Raises:
            ValueError: если входные аудиоданные пустые.
            ImportError: если отсутствуют обязательные зависимости (whisper/torch).
        """
        if not audio_data:
            raise ValueError("Пустые аудиоданные переданы в recognize().")

        device = "cuda" if getattr(torch, "cuda", None) and torch.cuda.is_available() else "cpu"

        # Определяем итоговое имя модели (позволяем переопределить через переменную окружения)
        effective_model_name = os.getenv("WHISPER_MODEL", self._model_name)

        # Кэшируем модель по имени и устройству, чтобы не загружать её на каждый вызов
        model = _get_or_load_model(
            model_name=effective_model_name,
            device=device,
            whisper_module=whisper,
        )

        # Определяем формат входа и сохраняем во временный файл с корректным расширением
        tmp_path = None
        suffix = _guess_audio_suffix(audio_data)
        tmp_file = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
        try:
            tmp_file.write(audio_data)
            tmp_file.flush()
            tmp_path = tmp_file.name
        finally:
            tmp_file.close()

        try:
            # fp16 имеет смысл только на GPU
            use_fp16 = device == "cuda"

            # Позволяем опционально зафиксировать язык через переменную окружения
            language_env = os.getenv("WHISPER_LANGUAGE")

            decode_kwargs = {
                "fp16": use_fp16,
                "task": "transcribe",
                "temperature": 0.0,
                "condition_on_previous_text": False,
                "without_timestamps": True,
                "beam_size": 5,
            }
            if language_env:
                decode_kwargs["language"] = language_env

            result = model.transcribe(tmp_path, **decode_kwargs)
            text = result.get("text", "") if isinstance(result, dict) else ""
            text = text if isinstance(text, str) else str(text)
            text = text.strip()
            return text
        finally:
            if tmp_path:
                try:
                    os.remove(tmp_path)
                except Exception:
                    # Безопасно игнорируем ошибки удаления временного файла
                    pass


# --- Внутренняя реализация кеширования модели ---
_CACHED_MODELS: dict[tuple[str, str], object] = {}


def _get_or_load_model(model_name: str, device: str, whisper_module: Any):
    """Возвращает кэшированную модель Whisper или загружает новую.

    Parameters:
        model_name: Имя модели Whisper.
        device: Устройство загрузки ("cpu" или "cuda").
        whisper_module: Модуль whisper (лениво импортированный).

    Returns:
        object: Экземпляр загруженной модели Whisper.
    """
    key = (model_name, device)
    model = _CACHED_MODELS.get(key)
    if model is None:
        model = whisper_module.load_model(model_name, device=device)
        _CACHED_MODELS[key] = model
    return model


def _guess_audio_suffix(audio_bytes: bytes) -> str:
    """Определяет расширение файла по сигнатуре аудиобайтов.

    Parameters:
        audio_bytes: Сырые байты аудиофайла.

    Returns:
        str: Рекомендуемое расширение (".mp3" или ".wav").
    """
    # MP3 может содержать ID3-тэг ("ID3" в начале) или frame sync (0xFFEx)
    if len(audio_bytes) >= 3 and audio_bytes[:3] == b"ID3":
        return ".mp3"
    if len(audio_bytes) >= 2:
        b0, b1 = audio_bytes[0], audio_bytes[1]
        if b0 == 0xFF and (b1 & 0xE0) == 0xE0:
            return ".mp3"
    # WAV RIFF header: "RIFF" .... "WAVE"
    if len(audio_bytes) >= 12 and audio_bytes[:4] == b"RIFF" and audio_bytes[8:12] == b"WAVE":
        return ".wav"
    # По умолчанию отдаём WAV, ffmpeg обычно корректно определяет по содержимому
    return ".wav"
