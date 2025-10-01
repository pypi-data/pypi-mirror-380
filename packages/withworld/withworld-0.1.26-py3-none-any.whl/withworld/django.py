
def install_django():
    """
django-admin startproject NAME
python django startapp APPNAME    
    """


def set_postgres():
    

    """pip install python-dotenv
--- docker-compose.yml

services:
  db:
    image: postgres:15
    container_name: postgres
    env_file:
      - .env
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: always

    

--- settings.py

from dotenv import load_dotenv
import os
# Загружаем .env
load_dotenv(BASE_DIR / ".env")

DATABASES = {
"default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "database"),
        "USER": os.getenv("POSTGRES_USER", "user"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "password"),
        "HOST": os.getenv("POSTGRES_HOST", "db"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}

--- .env

POSTGRES_DB=database
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432
    """


def set_script():
    """
myapp/management/commands/startbot.py

--- startbot.py

from django.core.management.base import BaseCommand
from django.conf import settings

def start():
    print('start hello!')

class Command(BaseCommand):
    help = "Запуск Telegram-бота"

    def handle(self, *args, **kwargs):
        start()

--- command

python manage.py startbot
    """


def gunicorn_start():
    """Как установить запустить gunicorn
    pip install gunicorn
-----------
    Настройки ДОКЕР
web:
    build: ./crmworld
    container_name: django_web
    command: bash -c "python manage.py migrate && gunicorn crmworld.wsgi:application --bind 0.0.0.0:8000"
    volumes:
      - ./crmworld:/app
    depends_on:
      - db
    env_file:
      - .env
    expose:
      - "8000"
    restart: always
---------------------
    Обычно gunicorn запускают с несколькими воркерами, например:

    gunicorn crmworld.wsgi:application --workers 3 --bind 0.0.0.0:8000


    Количество воркеров = (CPU * 2) + 1.
    Если сервер, например, 2 CPU → ставим --workers 5.
-------------------
НУЖНО ПРОПИСАТЬ ДОМЕН
ALLOWED_HOSTS = ["fokinax.com", "www.fokinax.com", "127.0.0.1", "localhost"]

-------------------
Настроить статику если есть фронтенд
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

-----------------
В продакшене включи:

CSRF_TRUSTED_ORIGINS = ["https://fokinax.com", "https://www.fokinax.com"]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


    """
    