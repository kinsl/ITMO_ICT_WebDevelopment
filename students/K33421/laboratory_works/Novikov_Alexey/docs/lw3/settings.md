# Создание проекта

Установить необходимо огромное количество библиотек. Создадим файл `requirements.txt` со следующим содержимым:

``` title="requirements.txt"
--8<-- "laboratory_work_3/requirements.txt"
```

Чуть подробнее о каждой библиотеке:

* `Django` - сам веб-фреймворк, который мы будем использовать;
* `django-cors-headers` - настройка CORS;
* `djangorestframework` - библиотека для REST API с использованием Django;
* `djangorestframework-simplejwt` - управление JWT токенами с помощью DRF;
* `django-allauth` + `dj-rest-auth` - удобная авторизация с помощью API, в том числе с помощью различных сторонних 
провайдеров (включая OIDC, который мы и будем использовать);
* `dj_database_url` - парсер БД-URL в настройки Django;
* `drf-spectacular` - Swagger для DRF;
* `gunicorn` - популярный веб-сервер, с помощью которого и будем запускать наш бэкенд;
* `psycopg[c]` - адаптер для PostgreSQL;
* `python-dotenv` + `starlette` - удобное управление переменными окружения;

Теперь установим все библиотеки следующей командой:

```commandline
pip install -r requirements.txt
```

Создадим проект `laboratory_work_3` и сразу несколько приложений:
```commandline
django-admin startproject laboratory_work_3
cd laboratory_work_3
python manage.py startapp adapter
python manage.py startapp oidc
python manage.py startapp survey
```

Приложение `adapter` будет представлять минимально необходимое взаимодействие с адаптерами.  
Приложение `oidc` будет отвечать за авторизацию с помощью OIDC ITMO.ID.  
В приложении `survey` будет всё взаимодействие с опросом.

Немного изменим структуру проекта и добавим некоторые файлы для удобного взаимодействия и дальнейшего деплоя:

``` { .sh .no-copy }
.
├─ src/
│  ├─ apps/
│  │  ├─ adapter/
│  │  ├─ oidc/
│  │  ├─ survey/
│  │  └─ __init__.py
│  ├─ delivery/
│  │  ├─ __init__.py
│  │  ├─ asgi.py
│  │  ├─ gunicorn.conf.py
│  │  ├─ urls.py
│  │  └─ wsgi.py
│  ├─ manage.py
│  └─ settings.py
├─ .env
├─ docker-compose.yml
├─ Dockerfile
└─ requirements.txt
```

Все файлы основные файлы проекта мы перенесли в директорию `src`, это будет отправная точка для создания docker образа.

Файлы проекта, отвечающие за поднятие сервера перенесли в отдельную директорию `delivery` и добавили туда файл настроек 
для gunicorn.

Приложения перенесли в отдельную директорию `apps`.

Теперь перейдём в файл `settings.py` и настроим все наши приложения и библиотеки:

- Загрузим переменные окружения и будем использовать их значения для важных настроек (важно не забыть указать их 
в `.env` файле):
```Python
--8<-- "laboratory_work_3/src/settings.py:20:39"
```

- Добавим все библиотеки и приложения в `INSTALLED_APPS`:
```Python
--8<-- "laboratory_work_3/src/settings.py:44:64"
```

- Добавим ID сайта (который далее создадим в админ-панели):
```Python
--8<-- "laboratory_work_3/src/settings.py:66:66"
```

- Добавим мидлварь для CORS первым элементом (важно) и мидлварь для авторизации:
```Python
--8<-- "laboratory_work_3/src/settings.py:68:78"
```

- Настройки для CORS будем так же брать из переменных окружения:
```Python
--8<-- "laboratory_work_3/src/settings.py:80:81"
```

- Поменяем путь до файла `url.py`, потому что мы изменили структуру проекта:
```Python
--8<-- "laboratory_work_3/src/settings.py:83:83"
```

- Также изменим путь до `wsgi.py`:
```Python
--8<-- "laboratory_work_3/src/settings.py:101:101"
```

- Получим ссылку на БД из переменных окружения (рекомендуется использовать PostgreSQL) и будем использовать SQLite, 
если в `.env` ничего не указано.  
Распарсим эту ссылку и используем в настройках БД:
```Python
--8<-- "laboratory_work_3/src/settings.py:107:111"
```

- Поменяем язык на русский:
```Python
--8<-- "laboratory_work_3/src/settings.py:136:136"
```

- Помянем часовой пояс на GMT+3:
```Python
--8<-- "laboratory_work_3/src/settings.py:138:138"
```

- Поменяем хранилище для статических файлов:
```Python
--8<-- "laboratory_work_3/src/settings.py:148:155"
```

- Укажем пути хранения статических файлов:
```Python
--8<-- "laboratory_work_3/src/settings.py:163:165"
```

- Настроим логгер:
```Python
--8<-- "laboratory_work_3/src/settings.py:176:188"
```

- Настроим DRF:  
В качестве класса для авторизации укажем `JWTCookieAuthentication` из библиотеки `dj_rest_auth`.  
Все ответы API будем выводить в виде JSON, используя класс по умолчанию `JSONRenderer`.  
Схемой для документации укажем `drf_spectacular`.  
Настроим тротлинг до 20 запросов в минуту.
```Python
--8<-- "laboratory_work_3/src/settings.py:191:200"
```

- Настроим кэш, который необходим для работы тротлинга:
```Python
--8<-- "laboratory_work_3/src/settings.py:202:207"
```

- Укажем время жизни JWT токенов:
```Python
--8<-- "laboratory_work_3/src/settings.py:209:212"
```

- Настроим `dj_rest_auth`:
```Python
--8<-- "laboratory_work_3/src/settings.py:214:220"
```

- Получим Client ID для клиента ITMO.ID из переменной окружения:
```Python
--8<-- "laboratory_work_3/src/settings.py:222:222"
```

- Настроим `django-allauth`:
```Python
--8<-- "laboratory_work_3/src/settings.py:224:227"
```

- Настроим Swagger:
```Python
--8<-- "laboratory_work_3/src/settings.py:229:237"
```

- Получим ссылки на бэкенд и фронтенд из переменных окружения:
```Python
--8<-- "laboratory_work_3/src/settings.py:239:240"
```