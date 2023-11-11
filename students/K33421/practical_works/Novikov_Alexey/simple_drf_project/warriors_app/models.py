from django.db import models


class Warrior(models.Model):
    class Race(models.TextChoices):
        STUDENT = "s", "student"
        DEVELOPER = "d", "developer"
        TEAMLEAD = "t", "teamlead"

    race = models.CharField(max_length=1, choices=Race.choices, verbose_name="Раса")
    name = models.CharField(max_length=120, verbose_name="Имя")
    level = models.IntegerField(default=0, verbose_name="Уровень")
    skill = models.ManyToManyField(
        "Skill", through="SkillOfWarrior", related_name="warrior_skils", verbose_name="Умения"
    )
    profession = models.ForeignKey(
        "Profession", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Профессия"
    )


class Profession(models.Model):
    title = models.CharField(max_length=120, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")


class Skill(models.Model):
    title = models.CharField(max_length=120, verbose_name="Наименование")

    def __str__(self):
        return self.title


class SkillOfWarrior(models.Model):
    skill = models.ForeignKey("Skill", on_delete=models.CASCADE, verbose_name="Умение")
    warrior = models.ForeignKey("Warrior", on_delete=models.CASCADE, verbose_name="Воин")
    level = models.IntegerField(verbose_name="Уровень освоения умения")
