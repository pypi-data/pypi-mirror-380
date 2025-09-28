"""Пакет распознавания речи.

Экспортирует основной интерфейс и реализацию Whisper.
"""

from .speech_recognizer import SpeechRecognizer, WhisperRecognizer

__all__ = [
    "SpeechRecognizer",
    "WhisperRecognizer",
]
