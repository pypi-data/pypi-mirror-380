from abc import ABC, abstractmethod


class SpeechRecognizer(ABC):
    """Базовый класс-интерфейс моделей распознавания речи."""

    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    def recognize(self, audio_data: bytes) -> str:
        """Распознаёт речь из аудиоданных.

        Parameters:
            audio_data: Сырые байты аудио.

        Returns:
            str: Распознанный текст.

        Raises:
            AudioProcessingError: если входные аудиоданные пустые.
            ModelLoadError: если не удалось загрузить модель.
            SpeechRecognitionError: при других ошибках распознавания.
        """
        raise NotImplementedError
