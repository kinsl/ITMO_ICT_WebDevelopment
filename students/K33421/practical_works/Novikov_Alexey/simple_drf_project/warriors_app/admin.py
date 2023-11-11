from django.contrib import admin

from .models import Warrior, Profession, Skill, SkillOfWarrior


@admin.register(Warrior)
class WarriorAdmin(admin.ModelAdmin):
    list_display = ("name", "race", "level", "profession")


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("title", )


@admin.register(SkillOfWarrior)
class SkillOfWarriorAdmin(admin.ModelAdmin):
    list_display = ("skill", "warrior", "level")
