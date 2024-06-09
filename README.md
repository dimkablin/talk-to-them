# Talk-to-them

```text
project-root/
├── backend/
│   ├── Dockerfile
│   ├── app/
│   │   ├── main.py  # Основной код для API
│   │   ├── ocr_client.py  # Клиент для взаимодействия с OCR контейнером
│   │   └── nlp_client.py  # Клиент для взаимодействия с NLP контейнером
│   ├── requirements.txt  # Зависимости для backend
├── frontend/
│   ├── Dockerfile
│   ├── src/
│   │   ├── index.html
│   │   ├── App.js  # Основной файл React/Vue.js приложения
│   │   └── ...  # Другие компоненты и стили
│   ├── package.json  # Зависимости для frontend
├── ocr/
│   ├── Dockerfile
│   ├── app/
│   │   ├── main.py  # Основной код OCR сервиса
│   │   └── model/  # Каталог с моделью и весами
│   ├── requirements.txt  # Зависимости для OCR
├── nlp/
│   ├── Dockerfile
│   ├── app/
│   │   ├── main.py  # Основной код NLP сервиса
│   │   └── model/  # Каталог с моделью и весами
│   ├── requirements.txt  # Зависимости для NLP
├── docker-compose.yml  # Конфигурация для Docker Compose
└── README.md  # Описание проекта и инструкции по запуску
```

# Tasks
#### Common tasks
- [x] Define the project's structure

#### NLP module
- [x] Add loading .gguf models from HF
- [x] Define a class LLM with the ```__call__()``` function for predictions.
- [ ] Add stream of generation support in cmd


#### OCR module
- [ ] Add weights of tesseract model
- [ ] Define a class OCR with the ```__call__()``` function for predictions.
- [ ] Define the pipline of image processing

#### Backend module
- [ ] Make gradio app