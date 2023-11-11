from rest_framework import generics

from .models import Warrior
from .serializers import WarriorWithProfessionSerializer, WarriorWithSkillsSerializer, WarriorFullInfoSerializer


class WarriorsWithProfessionListAPIView(generics.ListAPIView):
    serializer_class = WarriorWithProfessionSerializer
    queryset = Warrior.objects.all()


class WarriorsWithSkillsListAPIView(generics.ListAPIView):
    serializer_class = WarriorWithSkillsSerializer
    queryset = Warrior.objects.all()


class WarriorFullInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WarriorFullInfoSerializer
    queryset = Warrior.objects.all()
