# Шаблоны

Django имеет встроенную систему для работы с шаблонами - Django template language (DTL). С помощью этой системы можно 
использовать в HTML файлах различные переменные и теги, например, циклы.

Создадим папку `templates` в нашем приложении flights, в ней создадим ещё одну папку `flights`, и туда будем помещать 
все наши шаблоны.

=== "База"

    ```HTML title="base.html"
    --8<-- "laboratory_work_2/flights/templates/flights/base.html"
    ```

    Чтобы не повторять один и тот же HTML код во всех шаблонах, создадим базовый шаблон, от которого потом будем наследоваться 
    с помощью тега `{% extends %}`.

    В `<head>` подключим css файл bootstrap5, с помощью которого будет проще кастомизировать наш сайт. Также в <body> 
    нужно подключить js скрипт bootstrap5.

    В заголовке страницы создадим блок title - `{% block title %}Авиаперелёты{% endblock %}`. С помощью блоков шаблон-наследник 
    сможет переопределять значения в них. Собственно, в данном случае, если ребёнок не будет переопределять значение блока 
    title, то заголовок страницы будет "Авиаперелёты".

    Также создадим пустой `block css` на случай, если наследнику нужно будет спользовать свои стили.

    В теле страницы с помощью bootstrap5 создадим навигационное меню. Внутри меню поместим условие 
    `#!py3 {% if user.is_authenticated %}`, с помощью которого будет проверять, авторизован ли пользователь.  
    Если авторизован, в меню появится ссылка на просмотр броней и кнопка выхода с фамилией и именем пользователя. 
    Если не авторизован, то в меню появится кнопка входа.

    Ранее мы прописали названия для всех маршрутов сайта, поэтому в шаблонах можем не хардкодить адрес страницы, а использовать 
    тег `#!py3 {% url "название маршрута"  %}`.

    Так как мы используем в наших представлениях встроенный фреймворк messages, нам нужно как-то выводить их на страницах. 
    Для этого поместим в условие `#!py3 {% if messages %}` контейнер, в котором проитерируемся по всем сообщениям и для каждого 
    создадим ещё один контейнер нужного класса (ранее в настройках мы заменили теги сообщений, чтобы они соответствовали классам 
    bootstrap), в котором поместим текст сообщения и кнопку для закрытия.

    В конце создадим пустой `block content`, в котором наследники будут создавать контент своей страницы.


=== "Регистрация"

    ```HTML title="register.html"
    --8<-- "laboratory_work_2/flights/templates/flights/register.html"
    ```

    Наследуем базовый шаблон с помощью тега `#!py3 {% extends "flights/base.html" %}`.  
    С помощью тега `{% load django_bootstrap5 %}` подключим библиотеку `django-bootstrap5`, которую установили ранее.

    Переопределим блок `title` и содержимое страницы поместим в блок `content`.

    Создадим форму, в которой обязательно поместим тег `{% csrf_token %}` (POST запросы в Django защищены 
    от межсайтовой подделки запросов).  
    Само содержимое формы создадим с помощью тега `{% bootstrap_form register_form %}` (`register_form` - форма, 
    которую мы передали в шаблон). Также с помощью bootstrap создадим кнопку для отправки запроса.

    Если вдруг пользователь уже зарегистрирован, оставим ссылку на представление `login`.

    <figure markdown>
      ![Регистрация](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw2/templates/register.png)
      <figcaption>Отображение в браузере</figcaption>
    </figure>

    <figure markdown>
      ![Регистрация с ошибками](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw2/templates/register_with_errors.png)
      <figcaption>Ошибки валидации</figcaption>
    </figure>


=== "Вход"

    ```HTML title="login.html"
    --8<-- "laboratory_work_2/flights/templates/flights/login.html"
    ```

    Аналогично странице регистрации создаём страницу входа.

    <figure markdown>
      ![Вход](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw2/templates/login.png)
      <figcaption>Отображение в браузере</figcaption>
    </figure>

    <figure markdown>
      ![Регистрация с ошибками](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw2/templates/login_with_errors.png)
      <figcaption>Ошибки валидации</figcaption>
    </figure>


=== "Просмотр рейсов"

    ```HTML title="flights_list.html"
    --8<-- "laboratory_work_2/flights/templates/flights/flights_list.html"
    ```

    Создаём таблицу. Итерируемся по всем объектам в переданном в шаблон списке `flights` и выводим необходимую информацию. 
    Также в каждой строчке добавляем ссылку в виде кнопки на представление `book_flight` и передаём туда id рейса. Нажатие 
    этой кнопки забронирует рейс.

    Если список пустой, в DTL есть тег `{% empty %}`, чтобы сообщить об этом пользователю.

    <figure markdown>
      ![Просмотр рейсов](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw2/templates/flights_list.png)
      <figcaption>Отображение в браузере</figcaption>
    </figure>


=== "Просмотр броней"

    ```HTML title="my_flights.html"
    --8<-- "laboratory_work_2/flights/templates/flights/my_flights.html"
    ```

    Создадим навигационные вкладки с помощью bootstrap и поместим в них ссылки на то же представление, но с разным значеним 
    активной вкладки. Активную вкладку будем подсвечивать.

    Так же создадим таблицу с информацией о рейсах. В столбце с номерами рейсов поместим ссылки на представление `flight_details`, 
    чтобы перейти на страницу с дополнительной информацией о рейсе.  
    В зависимости от активной вкладки будем выводить либо кнопку удаления брони, либо кнопку для оставления отзыва.

    <figure markdown>
      ![Предстоящие рейсы](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw2/templates/upcoming_bookings.png)
      <figcaption>Предстоящие рейсы</figcaption>
    </figure>

    <figure markdown>
      ![Прошедшие рейсы](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw2/templates/past_bookings.png)
      <figcaption>Прошедшие рейсы</figcaption>
    </figure>


=== "Отзывы"

    ```HTML title="feedback.html"
    --8<-- "laboratory_work_2/flights/templates/flights/feedback.html"
    ```

    С помощью библиотеки `django_bootstrap5` выводим содержимое формы, которую передали в шаблон.

    <figure markdown>
      ![Написание отзыва](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw2/templates/feedback.png)
      <figcaption>Отображение в браузере</figcaption>
    </figure>

    <figure markdown>
      ![Написание отзыва с ошибками](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw2/templates/feedback_with_errors.png)
      <figcaption>Ошибки валидации</figcaption>
    </figure>


=== "Информация о рейсе"

    ```HTML title="flight_details.html"
    --8<-- "laboratory_work_2/flights/templates/flights/flight_details.html"
    ```

    Итерируемся по всем броням, привязанным к выбранному рейсу и на основе этой информации создаём таблицу со всеми пассажирами.

    Также итерируемся по всем отзывывам и выводим их под таблицей.

    <figure markdown>
      ![Информация о рейсе](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw2/templates/flight_details.png)
      <figcaption>Отображение в браузере</figcaption>
    </figure>