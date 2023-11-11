from rest_framework import serializers

from .models import Warrior, Profession, Skill, SkillOfWarrior


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ["title", "description"]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["title"]


class SkillOfWarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillOfWarrior
        fields = ["skill", "level"]

    skill = serializers.SlugRelatedField(slug_field="title", read_only=True)


class WarriorWithProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = ("id", "name", "race", "level", "profession")

    profession = ProfessionSerializer(read_only=True)
    race = serializers.CharField(source="get_race_display", read_only=True)


class WarriorWithSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = ("id", "name", "race", "level", "skill")

    skill = serializers.SerializerMethodField("get_skill_of_warrior")
    race = serializers.CharField(source="get_race_display", read_only=True)

    @staticmethod
    def get_skill_of_warrior(obj):
        skill = SkillOfWarrior.objects.filter(warrior=obj)
        return SkillOfWarriorSerializer(skill, many=True).data


class WarriorFullInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = ("id", "name", "race", "level", "skill", "profession")

    skill = serializers.SerializerMethodField("get_skill_of_warrior")
    race = serializers.CharField(source="get_race_display", read_only=True)
    profession = ProfessionSerializer(read_only=True)

    @staticmethod
    def get_skill_of_warrior(obj):
        skill = SkillOfWarrior.objects.filter(warrior=obj)
        return SkillOfWarriorSerializer(skill, many=True).data
