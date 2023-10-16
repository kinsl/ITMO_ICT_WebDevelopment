# Цветовая палитра

#### Цветовая схема

Material for MkDocs поддерживает две цветовые схемы: светлую (значение `default`) и тёмную (значение `slate`). 
Чтобы выбрать цветовую схему, используйте следующий код:

``` yaml
theme:
  palette:
    scheme: slate
```

Нажмите на кнопки, чтобы изменить цветовую схему:

<div class="mdx-switch">
  <button data-md-color-scheme="default"><code>default</code></button>
  <button data-md-color-scheme="slate"><code>slate</code></button>
</div>

<script>
  var buttons = document.querySelectorAll("button[data-md-color-scheme]")
  buttons.forEach(function(button) {
    button.addEventListener("click", function() {
      document.body.setAttribute("data-md-color-switching", "")
      var attr = this.getAttribute("data-md-color-scheme")
      document.body.setAttribute("data-md-color-scheme", attr)
      var name = document.querySelector("#__code_0 code span.l")
      name.textContent = attr
      setTimeout(function() {
        document.body.removeAttribute("data-md-color-switching")
      })
    })
  })
</script>

#### Основной цвет

Основной цвет используется в шапке сайта, текстовых ссылках и в некоторых других компонентах. Чтобы его изменить, 
нужно поменять следующее значение на одно из доступных:

``` yaml
theme:
  palette:
    primary: black
```

Нажмите на кнопки, чтобы изменить основной цвет:

<div class="mdx-switch">
  <button data-md-color-primary="red"><code>red</code></button>
  <button data-md-color-primary="pink"><code>pink</code></button>
  <button data-md-color-primary="purple"><code>purple</code></button>
  <button data-md-color-primary="deep-purple"><code>deep purple</code></button>
  <button data-md-color-primary="indigo"><code>indigo</code></button>
  <button data-md-color-primary="blue"><code>blue</code></button>
  <button data-md-color-primary="light-blue"><code>light blue</code></button>
  <button data-md-color-primary="cyan"><code>cyan</code></button>
  <button data-md-color-primary="teal"><code>teal</code></button>
  <button data-md-color-primary="green"><code>green</code></button>
  <button data-md-color-primary="light-green"><code>light green</code></button>
  <button data-md-color-primary="lime"><code>lime</code></button>
  <button data-md-color-primary="yellow"><code>yellow</code></button>
  <button data-md-color-primary="amber"><code>amber</code></button>
  <button data-md-color-primary="orange"><code>orange</code></button>
  <button data-md-color-primary="deep-orange"><code>deep orange</code></button>
  <button data-md-color-primary="brown"><code>brown</code></button>
  <button data-md-color-primary="grey"><code>grey</code></button>
  <button data-md-color-primary="blue-grey"><code>blue grey</code></button>
  <button data-md-color-primary="black"><code>black</code></button>
  <button data-md-color-primary="white"><code>white</code></button>
</div>

<script>
  var buttons = document.querySelectorAll("button[data-md-color-primary]")
  buttons.forEach(function(button) {
    button.addEventListener("click", function() {
      var attr = this.getAttribute("data-md-color-primary")
      document.body.setAttribute("data-md-color-primary", attr)
      var name = document.querySelector("#__code_1 code span.l")
      name.textContent = attr.replace("-", " ")
    })
  })
</script>

#### Акцентный цвет

Акцентный цвет используется для выделения элементов, с которыми можно взаимодействовать, например, ссылок при наведении, 
кнопок, колеса прокрутки. Чтобы его изменить, нужно поменять следующее значение на одно из доступных:

``` yaml
theme:
  palette:
    accent: indigo
```

Нажмите на кнопки, чтобы изменить акцентный цвет:

<style>
  .md-typeset button[data-md-color-accent] > code {
    background-color: var(--md-code-bg-color);
    color: var(--md-accent-fg-color);
  }
</style>

<div class="mdx-switch">
  <button data-md-color-accent="red"><code>red</code></button>
  <button data-md-color-accent="pink"><code>pink</code></button>
  <button data-md-color-accent="purple"><code>purple</code></button>
  <button data-md-color-accent="deep-purple"><code>deep purple</code></button>
  <button data-md-color-accent="indigo"><code>indigo</code></button>
  <button data-md-color-accent="blue"><code>blue</code></button>
  <button data-md-color-accent="light-blue"><code>light blue</code></button>
  <button data-md-color-accent="cyan"><code>cyan</code></button>
  <button data-md-color-accent="teal"><code>teal</code></button>
  <button data-md-color-accent="green"><code>green</code></button>
  <button data-md-color-accent="light-green"><code>light green</code></button>
  <button data-md-color-accent="lime"><code>lime</code></button>
  <button data-md-color-accent="yellow"><code>yellow</code></button>
  <button data-md-color-accent="amber"><code>amber</code></button>
  <button data-md-color-accent="orange"><code>orange</code></button>
  <button data-md-color-accent="deep-orange"><code>deep orange</code></button>
</div>

<script>
  var buttons = document.querySelectorAll("button[data-md-color-accent]")
  buttons.forEach(function(button) {
    button.addEventListener("click", function() {
      var attr = this.getAttribute("data-md-color-accent")
      document.body.setAttribute("data-md-color-accent", attr)
      var name = document.querySelector("#__code_2 code span.l")
      name.textContent = attr.replace("-", " ")
    })
  })
</script>

#### Переключатель цветовой палитры

Можно также добавить переключатель между светлой и тёмной темой:

``` yaml
theme:
  palette:

    # Переключатель для светлой темы
    - scheme: default
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode

    # Переключатель для тёмной темы
    - scheme: slate
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
```

Для каждой цветовой палитры помимо цветовой схемы можно выбрать свои основные и акцентные цвета.

Следующие свойства должны быть указаны для каждого переключателя:

`icon`:  
Это свойство должно указывать на существующий путь иконки, встроенный в тему. Популярные решения:

* :material-brightness-7: + :material-brightness-4: – `material/brightness-7` + `material/brightness-4`
* :material-toggle-switch: + :material-toggle-switch-off-outline: – `material/toggle-switch` + `material/toggle-switch-off-outline`
* :material-weather-night: + :material-weather-sunny: – `material/weather-night` + `material/weather-sunny`
* :material-eye: + :material-eye-outline: – `material/eye` + `material/eye-outline`
* :material-lightbulb: + :material-lightbulb-outline: – `material/lightbulb` + `material/lightbulb-outline`

Список всех доступных иконок можно найти [здесь].

  [здесь]: https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#search

`title`

Это свойство используется в качестве всплывающей подсказки при наведении на переключатель.

#### Системные предпочтения

Каждая цветовая палитра может быть связана с системными предпочтениями пользователя в отношении 
светлых и темных тонов с помощью медиа-запроса. Просто добавьте свойство `media` рядом с определением схемы:

``` yaml
theme:
  palette:

    # Переключатель для светлой темы
    - media: "(prefers-color-scheme: light)"
      scheme: default
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode

    # Переключатель для тёмной темы
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
```