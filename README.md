# ДЗ 3: Настройка стратегий развертывания модели 

## Описание проекта

В данном проекте реализован ML-сервис с REST API для инференса модели машинного обучения.
Сервис упакован в Docker и разворачивается с использованием стратегии безопасного деплоя
**Blue-Green Deployment**. Процесс сборки и деплоя автоматизирован с помощью **GitHub Actions (CI/CD)**.

Проект демонстрирует:
- деплой ML-моделей в production-окружение;
- управление версиями моделей;
- переключение трафика без остановки сервиса;
- возможность быстрого отката при ошибках.

---
## Структура проекта

```text
ml-deploy/
│
├── .github/
│   └── workflows/
│       └── deploy.yml          ← CI/CD (GitHub Actions)
├── main.py                     ← FastAPI сервис
├── train.py                    ← обучение модели (1 раз)
├── model.pkl                   ← сохранённая модель
├── requirements.txt            ← зависимости
├── Dockerfile                  ← Docker образ сервиса
│
├── docker-compose.blue.yml     ← Blue версия (v1.0.0)
├── docker-compose.green.yml    ← Green версия (v1.1.0)
│
├── .gitignore
└── README.md                   
```

## Функциональность API

Сервис предоставляет два эндпоинта:

### `GET /health`
Возвращает статус сервиса и текущую версию модели.

Пример ответа:
```json
{
  "status": "ok",
  "version": "v1.0.0"
}
```

## Скрины работы
1.
<img width="1280" height="258" alt="image" src="https://github.com/user-attachments/assets/38884717-afae-49b6-a2c9-ac4e6b69e2f0" />
<img width="1280" height="379" alt="image" src="https://github.com/user-attachments/assets/66064f0d-9d3e-4179-98e4-a5738af403a2" />

2.
<img width="1280" height="563" alt="image" src="https://github.com/user-attachments/assets/004d0bd5-b02d-4fcf-adf7-0029929b2eeb" />
<img width="1280" height="422" alt="image" src="https://github.com/user-attachments/assets/d468dcae-0a79-40d0-a7dd-f27c92ab634d" />

3.
<img width="1280" height="207" alt="image" src="https://github.com/user-attachments/assets/768e2f4e-698c-4624-9ced-e537cae215ab" />
<img width="1280" height="869" alt="image" src="https://github.com/user-attachments/assets/ab7a1d42-13dd-49ab-b998-a34912f468c6" />
