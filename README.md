# Проект Яндекс.Практикум API_Yatuve
Учебный проект курса Python Яндекс.Практикум
## Описание:
API для социальной сети проекта Yatube.
Предоставляет пользователям возможность удалённого взаимодействия с сайтом Yatube в зависимости от уровня доступа.
## Используемые технологии:
- Python
- Django
### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/vartexxx/api_final_yatube.git
```
```
cd api_final_yatube
```

Создать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source/venv/Scripts/activate
```

Установить зависимости из файла requirements.txt

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
cd api_final_yatube
```

```
python manage.py runserver
```