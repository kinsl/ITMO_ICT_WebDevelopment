# Представления

Представления - основная логика нашего сайта, именно здесь мы будем создавать наши эндпоинты. 
Для этого перейдём в файл `views.py` в наших приложениях.

Для большинства функций написан длинный декоратор `#!py3 @extend_schema`, он используется для конкретизации документации 
Swagger. Об этом подробнее [здесь](swagger.md).

=== "oidc"

    === "Авторизация"

        ```Python
        from urllib.parse import urlencode, quote
        
        from allauth.socialaccount.providers.oauth2.client import OAuth2Client
        from allauth.socialaccount.providers.openid_connect.views import OpenIDConnectAdapter
        from dj_rest_auth.registration.views import SocialLoginView
        from django.conf import settings
        from django.http import HttpResponseRedirect
        from drf_spectacular.types import OpenApiTypes
        from drf_spectacular.utils import extend_schema, inline_serializer, OpenApiParameter
        from rest_framework import status, serializers
        from rest_framework.request import Request
        from rest_framework.response import Response
        from rest_framework.views import APIView
    
    
        --8<-- "laboratory_work_3/src/apps/oidc/views.py:16:72"
        ```
    
        В начале файла импортируем из настроек базовые URL для наших бэкенда и фронтенда, они нам понадобятся для редиректов.

        В классе `ItmoIdAuthUrl` создадим метод `get`, который будет создавать и возвращать ссылку на авторизацию в ITMO.ID
        на основе данных имеющегося клиента.

        Класс `ItmoIdAdapter` - наследник от `OpenIDConnectAdapter` (из библиотеки `django-allauth`), который переопределяет
        только его метод инициализации, дополнительно указывая название используемого OIDC провайдера.

        В классе `ItmoIdAuth` создадим метод `get`, который из query параметров получит `code` и отправит его во фронтенд приложение. 
        Эндпоинт, связанный с этим классом, указывается, как `redirect_uri` в настройках провайдера OIDC, и после успешной авторизации 
        в нём, он редиректнет пользователя на него вместе с необходимыми параметрами.

        Класс `ItmoIdLogin` - наследник от `SocialLoginView` (из библиотеки `dj-rest-auth`). Именно он отвечает за основной процесс 
        авторизации в стороннем провайдере: обмен кода авторизации на JWT токены провайдера, получение из токена информации 
        о пользователе, создание нового пользователя в БД, создание "социального аккаунта" пользователя (со всей полученной 
        информацией), выдача собственных JWT токенов.

        Также, для удобной работы создадим Django-сигнал, который при создании социального аккаунта так же создаст запись в нашей 
        таблице профилей ITMO.ID, и привяжет эту запись к нужному пользователю:

        ```Python title="signals.py"
        --8<-- "laboratory_work_3/src/apps/oidc/signals.py"
        ```

        Этот сигнал получает информацию из полученного от ITMO.ID токена (сохранённую в социальном аккаунте в виде словаря) 
        и распрасит её в поля модели, создав запись в ней.

        Чтобы он работал, его нужно импортировать при инициализации приложения (в методе `ready`):

        ```Python title="apps.py"
        --8<-- "laboratory_work_3/src/apps/oidc/apps.py"
        ```

    === "Группа"

        ```Python
        from drf_spectacular.types import OpenApiTypes
        from drf_spectacular.utils import extend_schema, inline_serializer
        from rest_framework import status, serializers
        from rest_framework.request import Request
        from rest_framework.response import Response
        from rest_framework.views import APIView
    
    
        --8<-- "laboratory_work_3/src/apps/oidc/views.py:75:96"
        ```

        В этом же приложении и в этом же файле также создадим класс `ItmoIdProfileGroupView`. В нём метод `get` будет 
        возвращать учебную группу пользователя. Для этого класса нужно указать доступ только для авторизованных пользователей 
        с помощью `#!py3 permission_classes = [IsAuthenticated]`.

=== "survey"

    === "Вопросы"

        ```Python
        from rest_framework import generics
        from rest_framework.permissions import IsAuthenticated
        
        from .serializers import SurveyQuestionSerializer
        from .models import SurveyQuestion
    
    
        --8<-- "laboratory_work_3/src/apps/survey/views.py:21:29"
        ```

        В этом классе за основу возьму `generics.ListAPIView`, возвращающий список объектов. Укажем необходимый запрос 
        с сортировкой по полю `order`, ранее созданный сериализатор и доступ только авторизованным пользователем. 
        Также в методе `get_serializer_context` передадим полученный запрос для корректной работы нашего сериализатора.

    === "Проверка"

        ```Python
        from drf_spectacular.utils import extend_schema, inline_serializer
        from rest_framework import status, serializers
        from rest_framework.permissions import IsAuthenticated
        from rest_framework.request import Request
        from rest_framework.response import Response
        from rest_framework.views import APIView
        
        from .models import SurveyFaculty, SurveyGroup, SurveyAnswer
    
    
        --8<-- "laboratory_work_3/src/apps/survey/views.py:32:73"
        ```

        Опрос должен быть доступен не всем, поэтому создадим эндпоинт, который проверит все условия для пользователя и вернёт 
        ответ, чтобы фронтенд мог решить, что делать дальше.

        Проверим курс пользователя, его факультет и статус активности, его учебную группу и наличие привязанных к ней адаптеров 
        и факт прохождения опроса.

    === "Ответы"

        ```Python
        import logging
        
        import requests
        from django.conf import settings
        from drf_spectacular.utils import extend_schema, inline_serializer
        from rest_framework import status, serializers
        from rest_framework.permissions import IsAuthenticated
        from rest_framework.request import Request
        from rest_framework.response import Response
        from rest_framework.views import APIView
        
        from .serializers import SurveyAnswerSerializer
        from .models import SurveyQuestion, SurveyAnswer
        
        
        logger = logging.getLogger("root")
        
        BE_BASE_URL = settings.BE_BASE_URL
    
    
        --8<-- "laboratory_work_3/src/apps/survey/views.py:76:166"
        ```

        В этом эндпоинте в POST запросе будем проверять отправленные ответы.

        Для начала нам снова нужно проверить условия для прохождения опроса пользователем, 
        для этого отправим запрос на эндпоинт проверки.

        Если условия соблюдены, нужно проверить входные данные с помощью написанного ранее сериализатора для ответов.

        Если все данные корректны, создадим список объектов `SurveyAnswer`, который будем создавать, проверяя различные 
        условия, затем массово создадим все записи в БД с помощью метода `bulk_create`.