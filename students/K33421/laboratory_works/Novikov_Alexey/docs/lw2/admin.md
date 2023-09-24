# Администрирование

Чтобы настроить админ-панель, перейдём в файл `admin.py` в нашем приложении.

Первым делом настроим заголовки страницы:

```Python
from django.contrib import admin

--8<-- "laboratory_work_2/flights/admin.py:9:10"
```

Далее необходимо зарегистрировать все модели. Чтобы дополнительно их настроить, создадим новые классы, наследуемые от 
`admin.ModelAdmin` и повесим на них декоратор `#!py3 @admin.register(НазваниеМодели)`. Внутри классов переопределим следующие атрибуты:

- `list_display` - то, что будет отображаться в табличном виде;
- `list_filter` - фильтры в таблице;
- `search_fields` - по каким полям искать нужные строчки;
- `readonly_fields` - "самописная" информация, не зависящая от конкретного поля. Будет отображаться в "карточке" объекта.

С помощью декоратора `#!py3 @admin.display` можно создать новые "поля" в табличном представлении модели или в "карточках" объектов.

Доступ к полям "соединённых" таблиц можно получить, используя двойное подчёркивание (`__`).

=== "Авиакомпания"

    ```Python
    from django.contrib import admin
    from django.urls import reverse
    from django.utils import timezone
    from django.utils.safestring import mark_safe
    
    from .models import Airline


    --8<-- "laboratory_work_2/flights/admin.py:13:37"
    ```

    В этом классе определим новый метод, возвращающий количество рейсов у авикомпании. Для этого 
    вызовем метод `.count()` у атрибута `flights` и узнаем количество объектов в запросе. Название этого метода введём 
    в `list_display`, чтобы отобразить это количество в таблице для каждой авиакомпании.

    Также определим метод `get_flights`, который мы введём в `readonly_fields`. В этом методе проитерируемся по всем рейсам 
    и соберём информацию о каждом из них, чтобы вывести её в карточках авиакомпаний.

    Также вставим ссылки на карточки соответствующих рейсов. Для этого вызовем функцию `django.urls.reverse()`, 
    первым аргументом которой будет ссылка на изменение объекта в админ-панели. Получим её, используя защищённый 
    атрибут `_meta` и его атрибуты `app_label` и `model_name`, а также значение первичного ключа объекта.

    Занесём каждую строчку в список и затем объединим с помощью метода `.join`, где разделителем будет тэг `<br>`.
    Так как Django по умолчанию избегает HTML тэгов в целях безопасности, пометим этот текст как безопасный с помощью 
    функции `mark_safe`.

    <figure markdown>
      ![Список авиакомпаний](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw2/admin/airlines.png)
      <figcaption>Список авиакомпаний</figcaption>
    </figure>

    <figure markdown>
      ![Информация об авикомпании](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw2/admin/airline_details.png)
      <figcaption>Информация об авикомпании</figcaption>
    </figure>

=== "Рейс"

    ```Python
    from django.contrib import admin
    from django.urls import reverse
    from django.utils.safestring import mark_safe
    
    from .models import Flight


    --8<-- "laboratory_work_2/flights/admin.py:40:63"
    ```
    
    По аналогии с авиакомпаниями и список рейсов создадим метод `get_bookings`, чтобы получить список всех броней на рейс.

    <figure markdown>
      ![Список рейсов](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw2/admin/flights.png)
      <figcaption>Список авиакомпаний</figcaption>
    </figure>

    <figure markdown>
      ![Информация о рейсе](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw2/admin/flight_details.png)
      <figcaption>Информация о рейсе</figcaption>
    </figure>

=== "Бронь"

    ```Python
    from django.contrib import admin
    from django.urls import reverse
    from django.utils import timezone
    from django.utils.safestring import mark_safe
    
    from .models import Booking


    --8<-- "laboratory_work_2/flights/admin.py:66:92"
    ```

    <figure markdown>
      ![Список броней](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw2/admin/bookings.png)
      <figcaption>Список броней</figcaption>
    </figure>

=== "Отзыв"

    ```Python
    from django.contrib import admin
    
    from .models import Feedback


    --8<-- "laboratory_work_2/flights/admin.py:95:119"
    ```

    <figure markdown>
      ![Список отзывов](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw2/admin/feedbacks.png)
      <figcaption>Список отзывов</figcaption>
    </figure>    