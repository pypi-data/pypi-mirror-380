# Speech Recognition Module

## Установка зависимостей

```sh
poetry env use 3.10 && poetry install
```

## Запуск сервера

```sh
poetry run uvicorn speechrec.server:app --host 0.0.0.0 --port 8000
```

## Тестирование

### Юнит-тесты

```sh
poetry run pytest tests/
```

### Тест работы API

```sh
curl -f -X POST http://localhost:8000/transcribe -F file=@tests/assets/count_ru.wav
```
