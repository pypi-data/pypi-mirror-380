import logging
import os
import tempfile
from abc import ABC, abstractmethod
from contextlib import contextmanager
from typing import Any, Generator, Optional

import torch
import whisper

logger = logging.getLogger(__name__)


# Пользовательские исключения
class SpeechRecognitionError(Exception):
    """Базовое исключение для ошибок распознавания речи."""

    pass


class ModelLoadError(SpeechRecognitionError):
    """Исключение при ошибке загрузки модели."""

    pass


class AudioProcessingError(SpeechRecognitionError):
    """Исключение при ошибке обработки аудио."""

    pass


# Константы
DEFAULT_MODEL_NAME = "tiny"
DEFAULT_BEAM_SIZE = 5
DEFAULT_TEMPERATURE = 0.0

# Константы для определения формата аудио
ID3_TAG_PREFIX = b"ID3"
RIFF_HEADER = b"RIFF"
WAVE_HEADER = b"WAVE"
MP3_SYNC_BYTE = 0xFF
MP3_SYNC_MASK = 0xE0


@contextmanager
def _temporary_audio_file(audio_data: bytes) -> Generator[str, None, None]:
    """Контекстный менеджер для создания временного аудиофайла.

    Parameters:
        audio_data: Сырые байты аудио.

    Yields:
        str: Путь к временному файлу.

    Raises:
        AudioProcessingError: Если аудиоданные пустые.
    """
    if not audio_data:
        raise AudioProcessingError("Пустые аудиоданные переданы в recognize().")

    suffix = _guess_audio_suffix(audio_data)
    logger.debug("Определен формат аудио: %s", suffix)

    tmp_file = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
    try:
        tmp_file.write(audio_data)
        tmp_file.flush()
        yield tmp_file.name
    finally:
        tmp_file.close()
        try:
            os.remove(tmp_file.name)
        except Exception as e:
            logger.warning("Не удалось удалить временный файл %s: %s", tmp_file.name, e)


class SpeechRecognizer(ABC):

    @abstractmethod
    def recognize(self, audio_data: bytes) -> str:
        raise NotImplementedError


class WhisperRecognizer(SpeechRecognizer):
    def __init__(
        self, model_name: str = DEFAULT_MODEL_NAME, language: Optional[str] = None, device: Optional[str] = None
    ) -> None:
        """Инициализирует распознаватель Whisper.

        Parameters:
            model_name: Имя модели Whisper (например, "tiny", "base", "small").
            language: Язык распознавания (например, "ru", "en"). По умолчанию
                None, в этом случае будет использован язык из аудиофайла.
            device: Устройство для загрузки модели (например, "cuda", "cpu").
                По умолчанию используется "cuda" если оно доступно, иначе
                "cpu".
        """
        self._model_name = model_name
        self._language = language
        self._device = self._determine_device(device)

        # Предварительно загружаем модель при инициализации
        try:
            self._model = _get_or_load_model(
                model_name=self._model_name,
                device=self._device,
                whisper_module=whisper,
            )
            logger.info(
                "WhisperRecognizer инициализирован с моделью '%s' на устройстве '%s'", self._model_name, self._device
            )
        except Exception as e:
            raise ModelLoadError(
                f"Не удалось загрузить модель Whisper '{self._model_name}' " f"на устройстве '{self._device}': {e}"
            ) from e

    def _determine_device(self, device: Optional[str]) -> str:
        """Определяет устройство для загрузки модели.

        Parameters:
            device: Предпочтительное устройство или None для автоопределения.

        Returns:
            str: Определенное устройство ("cuda" или "cpu").
        """
        if device:
            return device

        # Проверяем доступность CUDA более безопасно
        try:
            cuda_available = hasattr(torch, "cuda") and torch.cuda.is_available() and torch.cuda.device_count() > 0
            return "cuda" if cuda_available else "cpu"
        except Exception:
            # Если есть проблемы с CUDA, принудительно используем CPU
            logger.warning("Ошибка при проверке CUDA, используем CPU")
            return "cpu"

    def _create_transcription_params(self) -> dict[str, Any]:
        """Создает параметры для транскрипции.

        Returns:
            dict: Словарь с параметрами для whisper.transcribe().
        """
        return {
            "fp16": self._device == "cuda",  # fp16 имеет смысл только на GPU
            "task": "transcribe",
            "temperature": DEFAULT_TEMPERATURE,
            "condition_on_previous_text": False,
            "without_timestamps": True,
            "beam_size": DEFAULT_BEAM_SIZE,
            "language": self._language,
        }

    def _extract_text_from_result(self, result: Any) -> str:
        """Извлекает текст из результата транскрипции.

        Parameters:
            result: Результат от whisper.transcribe().

        Returns:
            str: Извлеченный и очищенный текст.
        """
        text = result.get("text", "") if isinstance(result, dict) else ""
        text = text if isinstance(text, str) else str(text)
        return text.strip()

    def recognize(self, audio_data: bytes) -> str:
        """Распознаёт речь из WAV/MP3 байтов, используя openai-whisper.

        Parameters:
            audio_data: Сырые байты аудио. Поддерживаются WAV (PCM) и MP3.

        Returns:
            str: Распознанный текст.

        Raises:
            AudioProcessingError: если входные аудиоданные пустые.
            ModelLoadError: если не удалось загрузить модель.
            SpeechRecognitionError: при других ошибках распознавания.
        """
        logger.debug("Начинаем распознавание аудио размером %d байт", len(audio_data))

        with _temporary_audio_file(audio_data) as tmp_path:
            decode_kwargs = self._create_transcription_params()
            logger.debug(
                "Запускаем транскрипцию с параметрами: fp16=%s, language=%s",
                decode_kwargs.get("fp16"),
                decode_kwargs.get("language"),
            )

            result = self._model.transcribe(tmp_path, **decode_kwargs)
            text = self._extract_text_from_result(result)

            logger.debug("Распознавание завершено, длина текста: %d символов", len(text))
            return text


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
        logger.info("Загружаем модель Whisper '%s' на устройство '%s'", model_name, device)
        model = whisper_module.load_model(model_name, device=device)
        _CACHED_MODELS[key] = model
        logger.debug("Модель '%s' успешно загружена и закеширована", model_name)
    else:
        logger.debug("Используем закешированную модель '%s' с устройства '%s'", model_name, device)
    return model


def _guess_audio_suffix(audio_bytes: bytes) -> str:
    """Определяет расширение файла по сигнатуре аудиобайтов.

    Parameters:
        audio_bytes: Сырые байты аудиофайла.

    Returns:
        str: Рекомендуемое расширение (".mp3" или ".wav").
    """
    # MP3 может содержать ID3-тэг ("ID3" в начале) или frame sync (0xFFEx)
    if len(audio_bytes) >= 3 and audio_bytes[:3] == ID3_TAG_PREFIX:
        return ".mp3"
    if len(audio_bytes) >= 2:
        b0, b1 = audio_bytes[0], audio_bytes[1]
        if b0 == MP3_SYNC_BYTE and (b1 & MP3_SYNC_MASK) == MP3_SYNC_MASK:
            return ".mp3"
    # WAV RIFF header: "RIFF" .... "WAVE"
    if len(audio_bytes) >= 12 and audio_bytes[:4] == RIFF_HEADER and audio_bytes[8:12] == WAVE_HEADER:
        return ".wav"
    # По умолчанию отдаём WAV, ffmpeg обычно корректно определяет по содержимому
    return ".wav"
