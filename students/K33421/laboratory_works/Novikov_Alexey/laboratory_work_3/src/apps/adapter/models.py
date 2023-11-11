from django.db import models


class Adapter(models.Model):
    class Meta:
        db_table = "adapter"
        verbose_name = "адаптер"
        verbose_name_plural = "адаптеры"

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
