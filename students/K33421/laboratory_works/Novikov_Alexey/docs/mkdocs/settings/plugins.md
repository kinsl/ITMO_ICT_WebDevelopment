# Расширения и плагины

### Список атрибутов

Это расширение позволяет добавлять HTML атрибуты и CSS практически ко всем Markdown элементам на уровне строк и блоков 
с помощью специального синтаксиса:

``` yaml
markdown_extensions:
  - attr_list
```

Это расширение необходимо для работы многих других расширений и плагинов.

### Кнопка копирования кода

В каждом блоке кода появится кнопка для копирования содержимого:

``` yaml
theme:
  features:
    - content.code.copy
```

??? info "Включение или отключение кнопки копирования кода для конкретных блоков"

    Если вы не хотите включать кнопку для всех блоков, можно включить её только для конкретного блока, 
    используя немного другой синтаксис, основанный на расширении [Список атрибутов](#_2):

    ```` yaml
    ``` { .yaml .copy }
    # Code block content
    ```
    ````

    Обратите внимание, что сначала должен быть указан шорткод языка блока с дополнительным префиксом `.`. 
    Подобным образом можно отключить кнопку копирования для конкретного блока:

    ```` { .yaml .no-copy }
    ``` { .yaml .no-copy }
    # Code block content
    ```
    ````

### Markdown в HTML

По умолчанию Markdown игнорирует содержимое необработанного HTML-элемента блочного уровня. 
При включенном расширении `md-in-html` содержимое необработанного элемента блочного уровня HTML 
может быть распаршено как Markdown при добавлении атрибута `markdown` в открывающий тег. 
При этом атрибут `markdown` будет удален из выходных данных, а все остальные атрибуты будут сохранены:

``` yaml
markdown_extensions:
  - md_in_html
```

``` html
<div markdown>
This is a *Markdown* Paragraph.
</div>
```

### SuperFences

Расширение позволяет произвольно встраивать блоки кода и контента друг в друга, 
включая советы, вкладки, списки и любые другие элементы:

``` yaml
markdown_extensions:
  - pymdownx.superfences
```

Это расширение необходимо для работы многих других расширений и плагинов.

### Highlight

Расширение [Highlight] добавляет поддержку подсветки синтаксиса в блоках кода (с помощью [SuperFences](#superfences)) и 
во вложенных блоках кода (с помощью [InlineHilite]):

``` yaml
markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.superfences 
  - pymdownx.inlinehilite
```

  [Highlight]: https://facelessuser.github.io/pymdown-extensions/extensions/highlight/
  [InlineHilite]: https://facelessuser.github.io/pymdown-extensions/extensions/inlinehilite/

### Вкладки

Расширение [Tabbed] позволяет использовать вкладки контента, простой способ группировки связанного контента и блоков кода:

``` yaml
markdown_extensions:
  - pymdownx.tabbed:
      alternate_style: true
```

  [Tabbed]: https://facelessuser.github.io/pymdown-extensions/extensions/tabbed/

#### Использование

```
=== "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```
```

<div class="result" markdown>

=== "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```

</div>

### Snippets

Расширение [Snippets] позволяет встраивать в документ содержимое других файлов, например, других документов 
или файлов с исходным кодом:

``` yaml
markdown_extensions:
  - pymdownx.snippets
```

  [Snippets]: https://facelessuser.github.io/pymdown-extensions/extensions/snippets/

#### Использование

Чтобы встроить содержимое какого-либо файла, нужно написать `--8<--` и название файла в кавычках:

`--8<-- "filename.py"`

Для указания, с какой по какую строчку вы хотите встроить содержимое, укажите номер строки начала и номер строки конца 
после название файла, разделив их с помощью `:`:

  - Чтобы встроить содержимое, начиная с какой-то строки, просто используйте `filename.py:3`
  - Чтобы встроить всё содержимое до какой-то строки, используйте `filename.py::3`. В данном случае встроится с 1 по 3 строку.
  - Чтобы встроить содержимое, начиная с какой-то строки и заканчивая другой, используйте `filename.py:4:6`.

### Советы

Советы являются отличным вариантом для добавления побочного контента без существенной перегрузки страницы. 
Material for MkDocs предоставляет несколько различных типов советов и позволяет встраивать в них произвольный контент.

Следующие расширения позволяют сделать советы сворачиваемыми и добавлять в них "вложенное" содержимое:

``` yaml
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
```

#### Использование

Синтаксис советов прост: блок начинается с `!!!`, после чего следует одно ключевое слово, 
используемое в качестве [классификатора типа](#_13). Содержимое блока начинается с пропуском строки и с отступом в четыре пробела:

``` markdown
!!! note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```

<div class="result" markdown>

!!! note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

</div>

#### Иконки

Каждый поддерживаемый тип советов имеет свою иконку, которую можно изменить на любую другую:

``` yaml
theme:
  icon:
    admonition:
      <type>: <icon>
```

??? example "Раскройте, чтобы посмотреть альтернативные наборы иконок"

    === ":octicons-mark-github-16: Octicons"

        ``` yaml
        theme:
          icon:
            admonition:
              note: octicons/tag-16
              abstract: octicons/checklist-16
              info: octicons/info-16
              tip: octicons/squirrel-16
              success: octicons/check-16
              question: octicons/question-16
              warning: octicons/alert-16
              failure: octicons/x-circle-16
              danger: octicons/zap-16
              bug: octicons/bug-16
              example: octicons/beaker-16
              quote: octicons/quote-16
        ```


    === ":fontawesome-brands-font-awesome: FontAwesome"

        ``` yaml
        theme:
          icon:
            admonition:
              note: fontawesome/solid/note-sticky
              abstract: fontawesome/solid/book
              info: fontawesome/solid/circle-info
              tip: fontawesome/solid/bullhorn
              success: fontawesome/solid/check
              question: fontawesome/solid/circle-question
              warning: fontawesome/solid/triangle-exclamation
              failure: fontawesome/solid/bomb
              danger: fontawesome/solid/skull
              bug: fontawesome/solid/robot
              example: fontawesome/solid/flask
              quote: fontawesome/solid/quote-left
        ```

#### Изменение заголовка

По умолчанию заголовок совета - название типа, но это можно изменить, добавив строку в кавычках в соответствии 
с Markdown (включая ссылки и форматирование) после определения типа:

``` markdown
!!! note "Phasellus posuere in sem ut cursus"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```

<div class="result" markdown>

!!! note "Phasellus posuere in sem ut cursus"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

</div>

#### Удаление заголовка

Аналогично с изменением заголовка, его можно удалить, для этого нужно вставить пустую строку после определения типа
(не работает для [раскрываемых блоков](#_12)):

``` markdown
!!! note ""

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```

<div class="result" markdown>

!!! note ""

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

</div>

#### Раскрываемые блоки

Если включен `pymdownx.details` и блок совета начинается с `???`, а не с `!!!`, то совет рендерится как раскрываемый блок:

``` markdown
??? note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```

<div class="result" markdown>

??? note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

</div>

Если после `???` добавить `+`, блок рендерится сразу раскрытым:

``` markdown
???+ note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```

<div class="result" markdown>

???+ note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

</div>

#### Поддерживаемые типы

`note`

!!! note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
    euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
    purus auctor massa, nec semper lorem quam in massa.

`abstract`

!!! abstract

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
    euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
    purus auctor massa, nec semper lorem quam in massa.

`info`

!!! info

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
    euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
    purus auctor massa, nec semper lorem quam in massa.

`tip`

!!! tip

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
    euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
    purus auctor massa, nec semper lorem quam in massa.

`success`

!!! success

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
    euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
    purus auctor massa, nec semper lorem quam in massa.

`question`

!!! question

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
    euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
    purus auctor massa, nec semper lorem quam in massa.

`warning`

!!! warning

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
    euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
    purus auctor massa, nec semper lorem quam in massa.

`failure`

!!! failure

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
    euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
    purus auctor massa, nec semper lorem quam in massa.

`danger`

!!! danger

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
    euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
    purus auctor massa, nec semper lorem quam in massa.

`bug`

!!! bug

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
    euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
    purus auctor massa, nec semper lorem quam in massa.

`example`

!!! example

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
    euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
    purus auctor massa, nec semper lorem quam in massa.

`quote`

!!! quote

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
    euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
    purus auctor massa, nec semper lorem quam in massa.


### Клавиши

Расширение [Keys] позволяет с использованием простого синтаксиса рендерить клавиши и их сочетания:

``` yaml
markdown_extensions:
  - pymdownx.keys
```

  [Keys]: https://facelessuser.github.io/pymdown-extensions/extensions/keys/

#### Использование

``` markdown
++ctrl+alt+del++
```

<div class="result" markdown>

++ctrl+alt+del++

</div>

### Эмодзи

Расширение [Emoji] автоматически рендерит текстовые указания на эмодзи:

``` yaml
markdown_extensions:
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji 
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
```

  [Emoji]: https://facelessuser.github.io/pymdown-extensions/extensions/emoji/


#### Использование

```
:smile:
```

<div class="result" markdown>

:smile:

</div>

```
:fontawesome-regular-face-laugh-wink:
```

<div class="result" markdown>

:fontawesome-regular-face-laugh-wink:

</div>


### Lightbox

Если вы хотите добавить возможность открывать картинки на полный экран и зумить их, [glightbox] плагин - прекрасный выбор. 
Установите его с помощью `pip`:

  [glightbox]: https://github.com/blueswen/mkdocs-glightbox

``` shell
pip install mkdocs-glightbox
```

И добавьте в `mkdocs.yml`:

``` yaml
plugins:
  - glightbox:
      auto_caption: true
```

#### Использование

```
<figure markdown>
  ![Рандомная картинка](https://dummyimage.com/600x400/eee/aaa)
  <figcaption>Рандомная картинка</figcaption>
</figure>
```

<div class="result" markdown>

<figure markdown>
  ![Рандомная картинка](https://dummyimage.com/600x400/eee/aaa)
  <figcaption>Рандомная картинка</figcaption>
</figure>

</div>