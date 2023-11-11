from django.urls import path

from .views import WarriorsWithProfessionListAPIView, WarriorsWithSkillsListAPIView, WarriorFullInfoAPIView

urlpatterns = [
    path("warriors/profession", WarriorsWithProfessionListAPIView.as_view()),
    path("warriors/skills", WarriorsWithSkillsListAPIView.as_view()),
    path("warriors/<int:pk>", WarriorFullInfoAPIView.as_view()),
]
