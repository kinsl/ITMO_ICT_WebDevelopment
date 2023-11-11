from django.contrib.auth.models import User
from django.db import models


class ItmoIdProfile(models.Model):
    class Meta:
        db_table = "itmo_id_profile"
        verbose_name = "профиль ITMO.ID"
        verbose_name_plural = "профили ITMO.ID"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", verbose_name="Пользователь")
    isu = models.PositiveIntegerField(null=True, blank=True, verbose_name="ИСУ")
    course = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Курс")
    faculty = models.CharField(blank=True, max_length=50, verbose_name="Факультет")
    group = models.CharField(blank=True, max_length=7, verbose_name="Группа")

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name} {'(' + str(self.isu) + ')' if self.isu else ''}"
