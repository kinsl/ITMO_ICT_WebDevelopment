from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.survey.models import SurveyQuestion
from apps.adapter.models import Adapter
from apps.adapter.serializers import AdapterSerializer
from apps.oidc.models import ItmoIdProfile


class SurveyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestion
        fields = ["id", "component", "text", "help_text", "training_text", "training_help_text", "adapters"]

    component = serializers.SerializerMethodField()
    adapters = serializers.SerializerMethodField()

    def get_component(self, obj: SurveyQuestion) -> SurveyQuestion.Type:
        return obj.get_component_display()

    def get_adapters(self, obj: SurveyQuestion) -> list[dict[str, str | int]]:
        request = self.context.get("request")
        if request and hasattr(request, "user") and obj.component == SurveyQuestion.Type.ADAPTER_SLIDER:
            group = ItmoIdProfile.objects.filter(user=request.user).values_list("group", flat=True)[0]
            adapters = Adapter.objects.filter(groups__name=group)
            return AdapterSerializer(adapters, many=True).data
        return []


class AdapterSliderValueSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    value = serializers.IntegerField()

    class Meta:
        fields = ("id", "value")


class SurveyAnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    value = serializers.JSONField()

    class Meta:
        fields = ("id", "value")

    def validate_id(self, value):
        question_exists = SurveyQuestion.objects.filter(id=value).exists()
        if not question_exists:
            raise ValidationError("The question ID does not exist!")
        return value

    def validate_value(self, value):
        if isinstance(value, int) or isinstance(value, str):
            return value
        elif isinstance(value, list) and all(isinstance(item, dict) for item in value):
            value_serializer = AdapterSliderValueSerializer(data=value, many=True)
            if value_serializer.is_valid(raise_exception=True):
                return value_serializer.validated_data
            else:
                raise ValidationError("Invalid value for Adapter Slider!")
        else:
            raise ValidationError(
                "The value must be an integer, a string, or a list of dictionaries with integer keys and values!"
            )
