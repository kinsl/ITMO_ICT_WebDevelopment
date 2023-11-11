from django.urls import path
from .views import SurveyQuestionList, SurveyCheckUserView, CreateSurveyAnswersView

urlpatterns = [
    path("questions/", SurveyQuestionList.as_view(), name="surveyquestion-list"),
    path("answers/", CreateSurveyAnswersView.as_view(), name="surveyanswers-create"),
    path("user/check/", SurveyCheckUserView.as_view(), name="surveyuser-check"),
]
