# Bookmarks app

Django приложение для хранения закладок.

## Техническое задание

Реализовать сервис закладок с использованием django.
Сервис должен предоставлять следующие возможности:

- Регистрация/Авторизация пользователей
- Возможность добавлять ссылки в закладки. После того как пользователь добавил ссылку, ее нужно распарсить,
  получить title, description, favicon. Парсер должен поддерживать различные схемы разметки, такие как schema.org,
  opengraph, JSON-LD. В приоритете использовать размеченные данные. Парсинг организовать с использованием очереди, таск
  должен парсить страницы и сохранять результат в бд. Форма должна принимать только валидный url, если url введен не
  верный, выводить ошибку, так же выдавать ошибку, если такой урл пользователь уже добавлял.
- Список ссылок. Выводить title, url, description и иконку сайта. Если данные еще не спарсили, то выводим только url.

Наличие функциональных и/или юнит тестов будет плюсом.
По фронтенду требований никаких не предъявляется.
Можно использовать любимый фреймворк или, например, воспользоваться Twitter Bootstrap. Уделяйте основное внимание
бэкенду, оформлению кода.

## Стек

- Python
- Django
- Redis
- Celery

## Запуск проекта

Клонируйте репозиторий:

```bash
git clone git@github.com:galirkil/bookmarks.git
```

Перейдите в папку с проектом, установите и активируйте виртуальное окружение:

```bash
cd bookmarks
python3 -m venv venv
source venv/bin/activate
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

Выполните миграции:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Запустите сервер:

```bash
python3 manage.py runserver
```

Установите Redis:
``
https://redis.io/download/
``

Запустите Celery:

```bash
celery -A bookmarks worker --loglevel=INFO  
```
