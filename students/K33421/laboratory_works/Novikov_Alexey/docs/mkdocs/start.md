# Начало работы

## Установка

Material for MkDocs опубликован как [Python пакет] и может быть установлен с помощью `pip`. Откройте 
терминал и установите пакет с помощью:

``` sh
pip install mkdocs-material
```

Вместе с пакетом установятся необходимые версии его зависимостей: [MkDocs], [Markdown], [Pygments] 
и [Python Markdown Extensions].

  [Python пакет]: https://pypi.org/project/mkdocs-material/
  [MkDocs]: https://www.mkdocs.org
  [Markdown]: https://python-markdown.github.io/
  [Pygments]: https://pygments.org/
  [Python Markdown Extensions]: https://facelessuser.github.io/pymdown-extensions/

## Создание сайта

Чтобы создать базу документации, перейдите в нужную директорию и выполните следующую команду в терминале:

``` sh
mkdocs new .
```

Она создаст следующую структуру:

``` { .sh .no-copy }
.
├─ docs/
│  └─ index.md
└─ mkdocs.yml
```

`mkdocs.yml` — основной файл документации, в нём хранятся все настройки и маршруты, и все команды, связанные с созданным 
сайтом нужно выполнять в директории, в которой находится этот файл.  
`docs/` — директория, в которой хранятся все файлы сайта: дополнительные стили, картинки, файлы Markdown.

## Предварительный просмотр

В MkDocs есть возможность запустить локальный сервер для предварительного просмотра. Все изменения тут же отражаются на 
сайте. Чтобы его запустить, перейдите в директорию с файлом `mkdocs.yml` и выполните команду:

``` sh
mkdocs serve
```

Затем перейдите на [http://localhost:8000][live preview], и вы увидите следующую страницу:

  [live preview]: http://localhost:8000

<figure markdown>
  ![](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/mkdocs/start/preview.png)
</figure>

Выглядит не очень, не правда ли? Чтобы это исправить, необходимо настроить файл конфигурации, 
об этом в [следующем разделе](settings/index.md).
