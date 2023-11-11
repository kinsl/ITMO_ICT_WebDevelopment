import csv
from collections import defaultdict

from django.contrib import admin
from django.db.models import Q, Avg, QuerySet
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from requests import Request

from apps.survey.models import SurveyGroup, SurveyFaculty, SurveyQuestion, SurveyAnswer


@admin.register(SurveyGroup)
class SurveyGroupAdmin(admin.ModelAdmin):
    list_display = ["name", "students_count", "get_pass_count"]
    search_fields = ["name"]
    filter_horizontal = ["adapters"]
    readonly_fields = ["get_adapter_scores"]
    actions = ["export_adapter_scores_as_csv"]

    @admin.display(description="Количество прошедших")
    def get_pass_count(self, obj: SurveyGroup) -> int:
        return SurveyAnswer.objects.filter(user__profile__group=obj.name).distinct("user").count()

    @staticmethod
    def convert_score(score: int | float) -> int | float:
        if 0 <= score < 2:
            return 0
        elif 2 <= score < 4:
            return 0.5
        elif 4 <= score <= 5:
            return 1

    @admin.display(description="Баллы адаптеров")
    def get_adapter_scores(self, obj: SurveyGroup) -> str:
        if not obj.students_count:
            return "Не указано количество студентов!"

        pass_rate = (
            SurveyAnswer.objects.filter(user__profile__group=obj.name).distinct("user").count() / obj.students_count
        )
        general_score = 0
        general_scores_by_questions = []

        general_questions = SurveyQuestion.objects.filter(
            ~Q(component__in=[SurveyQuestion.Type.ADAPTER_SLIDER, SurveyQuestion.Type.TEXT_AREA])
        ).all()
        for question in general_questions:
            score = SurveyQuestion.objects.filter(id=question.id, answers__user__profile__group=obj.name).aggregate(
                average_score=Avg("answers__score")
            )["average_score"]
            converted_score = self.convert_score(score)
            general_score += converted_score
            general_scores_by_questions.append(f"{question.get_component_display()}: {converted_score}")

        adapters = obj.adapters.all()
        adapter_scores = defaultdict(float)
        adapter_scores_by_questions = defaultdict(list)

        adapter_questions = SurveyQuestion.objects.filter(component=SurveyQuestion.Type.ADAPTER_SLIDER).all()
        for question in adapter_questions:
            for adapter in adapters:
                score = question.answers.filter(adapter=adapter, user__profile__group=obj.name).aggregate(
                    average_score=Avg("score")
                )["average_score"]
                converted_score = self.convert_score(score)
                adapter_scores[f"{adapter.last_name} {adapter.first_name}"] += converted_score
                adapter_scores_by_questions[f"{adapter.last_name} {adapter.first_name}"].append(
                    f"{question.get_component_display()}: {converted_score}"
                )

        formatted_scores = []
        for adapter, scores in adapter_scores_by_questions.items():
            main_score = (adapter_scores[adapter] + general_score + 1) * pass_rate + pass_rate
            main_criteria = f"Оценка: {main_score}"
            sum_score = f"Сумма: {main_score + adapter_scores[adapter] + general_score}"
            formatted_scores.append(
                f"<b>{adapter}</b>:<br>"
                f"{'<br>'.join([main_criteria] + scores + general_scores_by_questions + [sum_score])}"
            )
        return mark_safe("<br>⎯<br>".join(formatted_scores))

    @admin.action(description="Экспортировать результаты опроса")
    def export_adapter_scores_as_csv(self, request: Request, queryset: QuerySet[SurveyGroup]) -> HttpResponse:
        meta = self.model._meta

        fields = ["Группа", "Количество студентов", "Количество прошедших", "Результат"]
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename={}.csv".format(meta)
        writer = csv.DictWriter(response, fieldnames=fields, delimiter=";")
        writer.writeheader()

        for group in queryset:
            pass_count = SurveyAnswer.objects.filter(user__profile__group=group.name).distinct("user").count()
            row = {
                "Группа": group.name,
                "Количество студентов": group.students_count,
                "Количество прошедших": pass_count,
                "Результат": self.get_adapter_scores(group).replace("<br>", "\n"),
            }
            writer.writerow(row)

        return response


@admin.register(SurveyFaculty)
class SurveyFacultyAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["name"]
    list_editable = ["is_active"]


@admin.register(SurveyQuestion)
class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ["component", "text", "order"]
    ordering = ["order"]
    list_filter = ["component"]
    search_fields = ["text", "help_text"]


@admin.register(SurveyAnswer)
class SurveyAnswerAdmin(admin.ModelAdmin):
    list_display = ["get_type", "get_text", "value", "score"]
    list_filter = ["question__component", "score"]
    search_fields = ["question__text", "question__help_text", "value"]

    @admin.display(ordering="question__component", description="Тип виджета")
    def get_type(self, obj: SurveyAnswer) -> str:
        return obj.question.get_component_display()

    @admin.display(ordering="question__text", description="Вопрос")
    def get_text(self, obj: SurveyAnswer) -> str:
        return obj.question.text
