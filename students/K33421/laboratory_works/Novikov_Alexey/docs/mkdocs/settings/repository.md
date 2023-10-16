# Репозиторий

#### Ссылка

Чтобы добавить ссылку на репозиторий, нужно в свойстве `repo_url` указать нужную ссылку:

``` yaml
repo_url: https://github.com/kinsl/ITMO_ICT_WebDevelopment
```

Ссылка отобразится в правом верхнем углу на больших экранах и в навигационном меню на маленьких. Для публичных 
репозиториев GitHub и GitLab также отобразится количество звёзд и форков.

Для GitHub репозиториев также отобразится версия последнего созданного тега, если имеется.

#### Название

По умолчанию MkDocs подписывает кнопку названием используемой системы контроля версий (GitHub, GitLab и тд), 
но можно написать своё название, указав свойство `repo_name`:

``` yaml
repo_name: kinsl/ITMO_ICT_WebDevelopment
```

Лично я оставил название по умолчанию.

#### Иконка

По умолчанию используется обычная иконка git, но можно также использовать и любую встроенную в тему иконку:

``` yaml
theme:
  icon:
    repo: fontawesome/brands/git-alt
```

Популярные решения:

- :fontawesome-brands-git: – `fontawesome/brands/git`
- :fontawesome-brands-git-alt: – `fontawesome/brands/git-alt`
- :fontawesome-brands-github: – `fontawesome/brands/github`
- :fontawesome-brands-github-alt: – `fontawesome/brands/github-alt`
- :fontawesome-brands-gitlab: – `fontawesome/brands/gitlab`
- :fontawesome-brands-gitkraken: – `fontawesome/brands/gitkraken`
- :fontawesome-brands-bitbucket: – `fontawesome/brands/bitbucket`
- :fontawesome-solid-trash: – `fontawesome/solid/trash`