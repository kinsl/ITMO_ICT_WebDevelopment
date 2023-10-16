# GitHub Pages

GitHub Pages — удобный способ бесплатно и легко опубликовать свою документацию.

А ещё проще это сделать с помощью GitHub Actions, чтобы весь процесс происходил автоматически.

Создайте в корне проекта файл `.github/workflows/ci.yml` и поместите в него следующее содержимое:

``` yaml
name: ci
on:
  push:
    branches:
      - main
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: 3.x
      - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV
      - uses: actions/cache@v3
        with:
          key: mkdocs-material-${{ env.cache_id }}
          path: .cache
          restore-keys: |
            mkdocs-material-
      - run: pip install mkdocs-material mkdocs-glightbox
      - run: mkdocs gh-deploy --force
        working-directory: ./students/K33421/laboratory_works/Novikov_Alexey
```

Важно в `branches` указать ветку, в которой находятся файлы вышей документации 
и в `working-directory` указать путь, в котором находится ваш файл `mkdocs.yml`.

Теперь каждый коммит в эту ветку будет создавать все статические файлы сайта в новой ветке `gh-pages`. Осталось только 
указать её в настройках GitHub Pages:

<figure markdown>
  ![](https://kinsl.github.io/ITMO_ICT_WebDevelopment/img/mkdocs/ghpages/ghpages.png)
</figure>