# 💳 Payments System — Django Test

## Описание
Сервис принимает вебхуки от банка и начисляет баланс организации по ИНН. Защита от дублей по operation_id.

## Технологии
- Python 3.9  
- Django 4.2.17  
- MySQL  
- Django REST Framework

## Запуск
```bash
python -m venv .venv
source .venv/Scripts/Activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
