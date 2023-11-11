# Компоненты

В директории `/components` создадим все необходимые для нас самостоятельные компоненты со своей логикой и стилями.

=== "View"

    ```html title="components/View.vue"
    --8<-- "laboratory_work_4/src/components/View.vue"
    ```

    Самый базовый компонент, в котором будет рендериться основное содержимое страницы, указанное в роутере.

=== "Title"

    ```html title="components/Title.vue"
    --8<-- "laboratory_work_4/src/components/Title.vue"
    ```

    Этот компонент будет выступать хедером страницы. Чтобы сделать его динамичным, объявим `props` с помощью функции `defineProps`, 
    Значения для указанных переменных сможет передать родительский компонент.  
    Принимать будем четыре пропа: `groupName`, `showGroupName`, `showTitle`, `showLogout`.

    Сам хедер состоит из двух элементов: текста на фоне картинки и кнопки выхода. В различных состояних текст хедера должен 
    отличаться, кнопка выхода также должна появляться не всегда. Это поведение мы и будем варьировать на основе полученных пропов.

    В этом нам поможет директива `v-if`, которая рендерит элементы только в том случае, если указанное условие истино.

    Таким образом, если родительский класс передал `showLogout=false`, то кнопку выхода рендерить не будем. Таким же образом будем 
    заголовок не будет отображаться, если `showTitle=false`. И если указан номер группы с истиным булевым, будем его выводить.

    К кнопке выхода привяжем функцию хранилища `logout`.


=== "Footer"

    ```html title="components/Footer.vue"
    --8<-- "laboratory_work_4/src/components/Footer.vue"
    ```

    Футером нашей страницы будет картинка волны, которую мы с помощью директивы `v-for` повторим 6 раз.


=== "LoginButton"

    ```html title="components/LoginButton.vue"
    --8<-- "laboratory_work_4/src/components/LoginButton.vue"
    ```

    Этот компонент будет выводить кнопку авторизации вместе с небольшим дисклеймером. Помимо уже упомянутого `props`, 
    в этом компоненте также укажем `emits` с помощью функции `defineEmits`. Переданные сюда события будут отправлены в родительский 
    компонент, где смогут быть использованы.

    В `props` укажем булевое `disabled`, с помощью которого будем отключать кнопку авторизации.  
    В `emits` передадим клик на кнопку, если она не отключена.


=== "LoadingScreen"

    ```html title="components/LoadingScreen.vue"
    --8<-- "laboratory_work_4/src/components/LoadingScreen.vue"
    ```

    Этот компонент будет выводить гифку вращающегося логотипа клуба вместе с небольшой надписью. С помощью css-свойства 
    `z-index` будет выводить этот компонент поверх всего остального содержимого страницы, чтобы сымитировать поведение 
    загрузочного экрана.


=== "Label"

    ```html title="components/Label.vue"
    --8<-- "laboratory_work_4/src/components/Label.vue"
    ```

    В этом компоненте будем создавать надписи для полей формы на основе переданных в `props` значений.


=== "TextArea"

    ```html title="components/TextArea.vue"
    --8<-- "laboratory_work_4/src/components/TextArea.vue"
    ```

    Этот компонент импортирует другой компонент `Label` и выводит большое текстовое поле сразу с заголовком. Также он 
    выводит небольшой счётчик символов.

    Чтобы родительский компонент смог отслеживать изменение значения в этом поле, с помощью директивы `v-model` будем 
    передавать все значения в переменную `textArea`, с помощью функции `watch` будем получать новое значение и отправлять 
    его в родительский компонент с помощью `emit`.


=== "Slider"

    ```html title="components/Slider.vue"
    --8<-- "laboratory_work_4/src/components/Slider.vue"
    ```

    Этот компонент выводит слайдер от 1 до 5. С помощью `ref` создадим реактивную переменную со значением по умолчанию равным 3.
    С помощью директивы `v-model` создадим переменную `sliderValue`. В функции `onMounted`, которая вызывается при рендеринге 
    компонента, будем передавать это значение по умолчанию в слайдер. 

    И таким же образом, как это сделано с компонентом `TextArea` будем передавать значения в родительский компонент.


=== "AdapterSlider"

    ```html title="components/AdapterSlider.vue"
    --8<-- "laboratory_work_4/src/components/AdapterSlider.vue"
    ```

    Это усложнённая версия слайдера. На вход она должна принимать список словарей с id и фамилией и именем адаптеров, чтобы 
    для каждого из них вывести отдельный слайдер со своим значением.

    Создадим пустой реактивный словарь `sliderValues` и в функции `onMounted` заполним его значением по умолчанию равным 3 для 
    каждого из адаптеров.

    В директиве `v-model` укажем конкретный элемент этого словаря, соответствующий адаптеру.

    И снова уже ранее описанным образом будем передавать наш реактивный словарь в родительский компонент.


=== "Select"

    ```html title="components/Select.vue"
    --8<-- "laboratory_work_4/src/components/Select.vue"
    ```

    Этот компонент будет выводить выпадающий список с двумя выборами: "Да" и "Нет". 

    Так как у него нет значения по умолчанию, это поле сделаем обязательным для заполнения, для этого создадим с помощью 
    функции `computed` реактивную переменную `error`, которая будет хранить булевое значение, равное истине при отсутствии 
    выбранного значения. 

    На основе этой переменной будем менять класс выпадающего списка и добавлять сообщение об обязательности заполнения поля. 

    Помимо значения самого поля, будем в родительский компонент так же передавать и факт наличия ошибки.


=== "TrainingSelect"

    ```html title="components/TrainingSelect.vue"
    --8<-- "laboratory_work_4/src/components/TrainingSelect.vue"
    ```

    Это поле использует компоненты `Select` и `Slider`, поэтому на вход требует не только `text` и `helpText`, но и 
    `trainingText` и `trainingHelpText` для второго поля.

    Это поле изначально выводит только выпадающий список, но если в нём выбрано значение "Да", то также выводит и слайдер.

    Являясь родительским классом, этот компонент должен принимать значения этих компонент и передавать их уже в свой родительский класс.

    Для удобства передавать будем численное значение, считая "Нет" за 0, и в случае "Да" будем брать значение слайдера.


=== "SubmitButton"

    ```html title="components/SubmitButton.vue"
    --8<-- "laboratory_work_4/src/components/SubmitButton.vue"
    ```

    Этот компонент создаёт кнопку для отправки формы.

    Изначально кнопка отключена (предполагая, что в форме будут обязательные для заполнения поля), 
    но с помощью `props` можно поменять её состояние.


=== "InfoContainer"

    ```html title="components/InfoContainer.vue"
    --8<-- "laboratory_work_4/src/components/InfoContainer.vue"
    ```

    Этот компонент выводит текст в оформленном контейнере. Он нужен, чтобы показывать различные информационные сообщения.

    Чтобы удобно передавать в него текст между редиректами на страницы, хранить для него текст будет в отдельном хранилище Pinia:

    ```js title="stores/info.store.js"
    --8<-- "laboratory_work_4/src/stores/info.store.js"
    ```

    В нём всего лишь будем хранить только одну переменную и объявим только две функции: на её обновление и удаление.