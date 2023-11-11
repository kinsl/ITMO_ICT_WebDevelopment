import logging

import requests
from django.conf import settings
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import generics, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SurveyQuestionSerializer, SurveyAnswerSerializer
from .models import SurveyQuestion, SurveyFaculty, SurveyGroup, SurveyAnswer


logger = logging.getLogger("root")

BE_BASE_URL = settings.BE_BASE_URL


class SurveyQuestionList(generics.ListAPIView):
    """Get survey's questions with all needed information"""

    queryset = SurveyQuestion.objects.order_by("order").all()
    serializer_class = SurveyQuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {"request": self.request}


class SurveyCheckUserView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Get the user's suitability to take the survey",
        responses={
            status.HTTP_200_OK: inline_serializer(
                name="SurveyCheckUser",
                fields={
                    "access": serializers.BooleanField(),
                    "is_first_course": serializers.BooleanField(),
                    "is_faculty_active": serializers.BooleanField(),
                    "has_adapters": serializers.BooleanField(),
                    "is_done": serializers.BooleanField(),
                },
            ),
            status.HTTP_404_NOT_FOUND: inline_serializer(
                name="SurveyCheckUserNotFound",
                fields={"error": serializers.CharField()},
            ),
        },
    )
    def get(self, request: Request):
        user = request.user
        if not hasattr(user, "profile"):
            return Response({"error": "Profile does not exist!"}, status.HTTP_404_NOT_FOUND)

        is_first_course = user.profile.course and user.profile.course == 1
        is_faculty_active = (
            SurveyFaculty.objects.filter(name=user.profile.faculty).values_list("is_active", flat=True).first()
        )
        has_adapters = SurveyGroup.objects.filter(name=user.profile.group, adapters__isnull=False).exists()
        is_done = SurveyAnswer.objects.filter(user=user).exists()
        return Response(
            {
                "access": all((is_first_course, is_faculty_active, has_adapters, not is_done)),
                "is_first_course": is_first_course,
                "is_faculty_active": is_faculty_active,
                "has_adapters": has_adapters,
                "is_done": is_done,
            }
        )


class CreateSurveyAnswersView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SurveyAnswerSerializer(many=True)

    @extend_schema(
        summary="Save user's answers and calculate scores",
        responses={
            status.HTTP_200_OK: inline_serializer(
                name="CreateSurveyAnswers",
                fields={
                    "status": serializers.CharField(),
                },
            ),
            status.HTTP_400_BAD_REQUEST: SurveyAnswerSerializer,
            status.HTTP_404_NOT_FOUND: inline_serializer(
                name="SurveyCheckUserProfileNotFound",
                fields={"error": serializers.CharField()},
            ),
            status.HTTP_409_CONFLICT: inline_serializer(
                name="SurveyCheckUserConflict",
                fields={"error": serializers.CharField()},
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: inline_serializer(
                name="SurveyCheckUserServerError",
                fields={"error": serializers.CharField()},
            ),
        },
    )
    def post(self, request: Request):
        user = request.user
        if not hasattr(user, "profile"):
            return Response({"error": "Profile does not exist!"}, status.HTTP_404_NOT_FOUND)

        response = requests.get(f"{BE_BASE_URL}/api/survey/user/check/", headers=request.headers)
        response.raise_for_status()

        if not response.json().get("access", False):
            return Response({"error": "The survey checks has not been passed!"}, status=status.HTTP_409_CONFLICT)

        serializer = SurveyAnswerSerializer(data=request.data, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        answers = serializer.validated_data
        answers_to_create = []

        for answer in answers:
            question_id = answer["id"]
            value = answer["value"]

            question = SurveyQuestion.objects.filter(id=question_id).first()
            if not question:
                continue

            question_type = SurveyQuestion.Type(question.component)

            if question_type == SurveyQuestion.Type.TEXT_AREA:
                answers_to_create.append(SurveyAnswer(user=request.user, question=question, value=str(value), score=0))

            elif question_type in SurveyQuestion.Type.SELECT:
                answers_to_create.append(
                    SurveyAnswer(user=request.user, question=question, value=value, score=5 if value == "Да" else 0)
                )

            elif question_type in [SurveyQuestion.Type.SLIDER, SurveyQuestion.Type.TRAINING_SELECT]:
                answers_to_create.append(SurveyAnswer(user=request.user, question=question, value=value, score=value))

            elif question_type == SurveyQuestion.Type.ADAPTER_SLIDER:
                answers_to_create.extend(
                    SurveyAnswer(
                        user=request.user,
                        question=question,
                        adapter_id=adapter["id"],
                        value=str(adapter["value"]),
                        score=adapter["value"],
                    )
                    for adapter in value
                )

            else:
                continue

        try:
            SurveyAnswer.objects.bulk_create(answers_to_create)
        except Exception as exc:
            logger.exception(exc)
            return Response(
                {"error": "An error occurred while creating answers!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response({"status": "success"})
