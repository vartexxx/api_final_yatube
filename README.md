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

cd api_final_yatube
```

Создать виртуальное окружение:

```
python -m venv venv
```
Активировть виртуальное окружение.

```
source/venv/Scripts/activate
```

Обновить пакетный менеджер PIP:

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Перейти в каталог с проектом:

```
cd api_final_yatube
```

Запустить проект

```
python manage.py runserver
```

##Автор
👤 **Бурлака Владислав**

-GitHub: [@kefranabg](https://github.com/vartexxx)