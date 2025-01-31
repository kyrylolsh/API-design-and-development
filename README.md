FastAPI CRUD API

Встановлення:

Клонуйте репозиторій:

git clone <repo_url>
cd <repo_name>

Створіть віртуальне середовище та активуйте його:

python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate  # Для Windows

Встановіть залежності:

pip install -r requirements.txt

Запуск

uvicorn main:app --reload
