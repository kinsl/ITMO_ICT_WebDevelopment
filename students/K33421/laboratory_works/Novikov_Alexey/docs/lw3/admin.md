# Администрирование

Чтобы настроить админ-панель, перейдём в файл `admin.py` в наших приложениях.

Далее необходимо зарегистрировать все модели. Чтобы дополнительно их настроить, создадим новые классы, наследуемые от 
`admin.ModelAdmin` и повесим на них декоратор `#!py3 @admin.register(НазваниеМодели)`. Внутри классов переопределим следующие атрибуты:

- `list_display` - то, что будет отображаться в табличном виде;
- `list_filter` - фильтры в таблице;
- `search_fields` - по каким полям искать нужные строчки;
- `readonly_fields` - "самописная" информация, не зависящая от конкретного поля. Будет отображаться в "карточке" объекта.

С помощью декоратора `#!py3 @admin.display` можно создать новые "поля" в табличном представлении модели или в "карточках" объектов.

Доступ к полям "соединённых" таблиц можно получить, используя двойное подчёркивание (`__`).

=== "adapter"

    ```Python title="Адаптеры"
    from django.contrib import admin

    from apps.adapter.models import Adapter


    --8<-- "laboratory_work_3/src/apps/adapter/admin.py:6:12"
    ```

    Для этой модели в табличном виде будем выводить только фамилию и имя, остальные параметры оставим по умолчанию.

    <figure markdown>
      ![Список адаптеров](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/admin/adapter.png)
      <figcaption>Список адаптеров</figcaption>
    </figure>

=== "oidc"

    ```Python title="Пользователи"
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
    from django.contrib.auth.models import User
    
    from apps.oidc.models import ItmoIdProfile

    --8<-- "laboratory_work_3/src/apps/oidc/admin.py:8:43"
    ```

    Для модели ItmoIdProfile создадим класс, наследуемый от `admin.StackedInline`, чтобы не создавать для неё отдельную 
    таблицу, а выводить данные в модели пользователей. Для это укажем новый класс в атрибуте `inlines` класса `UserAdmin`.
    
    Также дополним базовый класс `UserAdmin` новыми методами для отображения данных профиля в табличном виде, добавим фильтры 
    и поля для поиска. Затем перерегистрируем класс в админ-панели.

    <figure markdown>
      ![Список пользователей](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/admin/users.png)
      <figcaption>Список пользователей</figcaption>
    </figure>

    <figure markdown>
      ![Информация о пользователе](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/admin/user_details.png)
      <figcaption>Информация о пользователе</figcaption>
    </figure>

=== "survey"

    === "Группы"
    
        ```Python
        import csv
        from collections import defaultdict
        
        from django.contrib import admin
        from django.db.models import Q, Avg, QuerySet
        from django.http import HttpResponse
        from django.utils.safestring import mark_safe
        from requests import Request
        
        from apps.survey.models import SurveyGroup
    
    
        --8<-- "laboratory_work_3/src/apps/survey/admin.py:13:103"
        ```

        Для этой модели была реализован метод для `readonly_fields`, который подсчитывает и выводит баллы за каждый 
        вопрос, переведённые по соответствующим критериям, для каждого адаптера группы.

        Этот метод также вызывается в другом методе, который отвечает за экспорт данных в CSV. Далее этот метод используется 
        как action в админ-панели.
    
        <figure markdown>
          ![Список групп](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/admin/groups.png)
          <figcaption>Список групп</figcaption>
        </figure>

        <figure markdown>
          ![Информация о группе](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/admin/group_detail.png)
          <figcaption>Информация о группе</figcaption>
        </figure>
    
    === "Факультеты"
    
        ```Python
        from django.contrib import admin
        
        from apps.survey.models import SurveyFaculty
    
    
        --8<-- "laboratory_work_3/src/apps/survey/admin.py:106:111"
        ```
    
        <figure markdown>
          ![Список факультетов](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/admin/faculties.png)
          <figcaption>Список факультетов</figcaption>
        </figure>    

    === "Вопросы"
    
        ```Python
        from django.contrib import admin
        
        from apps.survey.models import SurveyQuestion
    
    
        --8<-- "laboratory_work_3/src/apps/survey/admin.py:114:119"
        ```
    
        <figure markdown>
          ![Список вопросов](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/admin/questions.png)
          <figcaption>Список вопросов</figcaption>
        </figure>    

        <figure markdown>
          ![Информация о вопросе](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/admin/question_details.png)
          <figcaption>Информация о вопросе</figcaption>
        </figure>    

    === "Ответы"
    
        ```Python
        from django.contrib import admin
        
        from apps.survey.models import SurveyAnswer
    
    
        --8<-- "laboratory_work_3/src/apps/survey/admin.py:122:134"
        ```
    
        <figure markdown>
          ![Список ответов](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/admin/answers.png)
          <figcaption>Список ответов</figcaption>
        </figure>    

        <figure markdown>
          ![Информация об ответе](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/admin/answer_detail.png)
          <figcaption>Информация об ответе</figcaption>
        </figure>    