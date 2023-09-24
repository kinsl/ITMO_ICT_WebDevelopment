# Создание проекта

Установим фреймворк Django и библиотеку django-bootstrap5, которая нам понадобится для удобного форматирования форм:

```commandline
pip install django django_bootstrap5
```

Создадим проект `laboratory_work_2` и приложение `flights`:
```commandline
django-admin startproject laboratory_work_2
cd laboratory_work_2
python manage.py startapp flights
```

Перейдём в файл `settings.py` и сделаем некоторые изменения:

- Добавим наше приложение и bootstrap5 в `INSTALLED_APPS`:
```Python
--8<-- "laboratory_work_2/laboratory_work_2/settings.py:35:44"
```

- Поменяем язык на русский:
```Python
--8<-- "laboratory_work_2/laboratory_work_2/settings.py:110:110"
```

- Помянем часовой пояс на GMT+3:
```Python
--8<-- "laboratory_work_2/laboratory_work_2/settings.py:112:112"
```

- Помянем LOGIN_URL (используется для декоратора `login_required`, позже по этому URL добавим своё представление):
```Python
--8<-- "laboratory_work_2/laboratory_work_2/settings.py:129:129"
```

- Помянем теги встроенного messages фреймворка в соответствии с bootstrap5:
```Python
--8<-- "laboratory_work_2/laboratory_work_2/settings.py:131:137"
```