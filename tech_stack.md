Технический стек для Telegram-бота
Язык программирования:
Python 3.11+
Установка: Скачать с python.org или использовать предустановленную версию на сервере.
Библиотека для Telegram API:
aiogram 2.x
Установка: pip install aiogram
База данных:
SQLite
Хранение: Локальный файл diet_bot.db.
Хостинг:
railway
Может развернуть проект прямо из репозитория ГХ.
Контроль версий:
Git/GitHub
Установка: Установить Git (git-scm.com), создать репозиторий на github.com.
Дополнительные инструменты:
Логирование: Python-модуль logging для отслеживания ошибок.
API для продуктов (опционально, не для MVP): Nutritionix или Edamam для расширения базы в будущем.
Тестирование: Локальный запуск через python bot.py, проверка базы через DB Browser for SQLite.

diet_bot/

├── bot.py # Основной код бота

├── db.py # Логика работы с базой данных

├── diet_bot.db # Файл базы SQLite

├── requirements.txt # Зависимости (aiogram, python-dotenv)

├── .env # Токен бота (не пушить в Git)

├── README.md # Описание проекта

└── .gitignore # Игнорировать .env, diet_bot.db
