from django.db import models


class SurveyGroup(models.Model):
    class Meta:
        db_table = "survey_group"
        verbose_name = "группа"
        verbose_name_plural = "группы"

    name = models.CharField(max_length=7, verbose_name="Название")
    students_count = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Количество студентов")
    adapters = models.ManyToManyField("adapter.Adapter", blank=True, related_name="groups", verbose_name="Адаптеры")

    def __str__(self):
        return self.name


class SurveyFaculty(models.Model):
    class Meta:
        db_table = "survey_faculty"
        verbose_name = "факультет"
        verbose_name_plural = "факультеты"

    name = models.CharField(max_length=50, verbose_name="Название")
    is_active = models.BooleanField(default=False, verbose_name="Активен?")

    def __str__(self):
        return self.name


class SurveyQuestion(models.Model):
    class Meta:
        db_table = "survey_question"
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"

    class Type(models.TextChoices):
        TEXT_AREA = "text_area", "TextArea"
        ADAPTER_SLIDER = "adapter_slider", "AdapterSlider"
        SLIDER = "slider", "Slider"
        SELECT = "select", "Select"
        TRAINING_SELECT = "training_select", "TrainingSelect"

    component = models.CharField(max_length=15, choices=Type.choices, verbose_name="Виджет")
    text = models.CharField(max_length=200, verbose_name="Основной текст")
    help_text = models.CharField(max_length=200, blank=True, verbose_name="Дополнительный текст")
    training_text = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Второй основной текст",
        help_text="Используется для слайдера в TrainingSelect виджете",
    )
    training_help_text = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Второй дополнительный текст",
        help_text="Используется для слайдера в TrainingSelect виджете",
    )
    order = models.PositiveSmallIntegerField(verbose_name="Порядок")

    def __str__(self):
        return f"{self.component} - {self.text}"


class SurveyAnswer(models.Model):
    class Meta:
        db_table = "survey_answer"
        verbose_name = "ответ"
        verbose_name_plural = "ответы"

    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Пользователь", related_name="answers")
    adapter = models.ForeignKey(
        "adapter.Adapter", blank=True, null=True, on_delete=models.CASCADE, verbose_name="Адаптер"
    )
    question = models.ForeignKey(
        SurveyQuestion, on_delete=models.CASCADE, verbose_name="Вопрос", related_name="answers"
    )
    value = models.CharField(max_length=1000, verbose_name="Ответ")
    score = models.FloatField(blank=True, null=True, verbose_name="Балл")

    def __str__(self):
        return f"{self.value} {self.question.text}"
