# Добавление ассетов

Если есть желание как-то модифицировать тему или изменить какую-то логику, 
можно добавить в директорию `docs` CSS и JS файлы и указать относительный путь до них:

``` { .sh .no-copy }
.
├─ docs/
│  ├─ stylesheets/
│  │  └─ extra.css
│  └─ javascripts/
│     └─ extra.js
└─ mkdocs.yml
```

``` yaml
extra_css:
  - stylesheets/extra.css
extra_javascript:
  - javascripts/extra.js
```