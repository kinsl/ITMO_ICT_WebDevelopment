# Swagger

Для того чтобы создать Swagger документацию, воспользуемся библиотекой `drf-spectacular`.

Мы уже настроили эту библиотеку ранее [здесь](settings.md), а также указали нужные маршруты [здесь](router.md).
Этого достаточно, чтобы документация заработала и показывала информацию о наших эндопоинтах.

Но, к сожалению, отображаемся информация не всегда соответствует реальности, поэтому нам нужно расширить некоторые схемы 
с помощью декоратора `#!py3 @extend_schema` на методах наших представлений и с помощью Docstring там, где повесить декоратор 
не так просто.

Декоратор принимает несколько аргументов:

* `summary` - то, что будет отображаться рядом с URL эндпоинта;
* `description` - то, что будет написано в описании эндпоинта. Вместо этого аргумента можно использовать Docstring;
* `parameters` - схемы для входных данных. Указываются списком объектов класса `OpenApiParameter` с названием параметра и 
его типом;
* `responses` - словарь, где ключ - статус ответа, а значение - сериализатор. Можно как использовать готовые сериализаторы, 
так и написать сериализатор на месте с помощью `inline_serializer`.

Код для декораторов уже был представлен [здесь](views.md), дублировать информацию не буду.

Полученная документация:

=== "Список эндпоинтов"

    <figure markdown>
      ![Список эндпоинтов](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/swagger/main.png)
    </figure>   

=== "Ответы"

    <figure markdown>
      ![Ответы](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/swagger/answers.png)
    </figure>   

=== "Вопросы"

    <figure markdown>
      ![Вопросы](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/swagger/questions.png)
    </figure>   

=== "Проверка"

    <figure markdown>
      ![Проверка](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/swagger/check.png)
    </figure>   

=== "Редирект авторизации"

    <figure markdown>
      ![Редирект авторизации](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/swagger/redirect.png)
    </figure>   

    Здесь отсутствует ответ при статусе 200, так как эндпоинт возвращает редирект.

=== "Ссылка на авторизацию"

    <figure markdown>
      ![Ссылка на авторизацию](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/swagger/auth_url.png)
    </figure>   

=== "Группа"

    <figure markdown>
      ![Группа](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/swagger/group.png)
    </figure>   

=== "Авторизация"

    <figure markdown>
      ![Авторизация](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/swagger/login.png)
    </figure>   

=== "Обновление токена"

    <figure markdown>
      ![Обновление токена](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/lw3/swagger/refresh_token.png)
    </figure>   