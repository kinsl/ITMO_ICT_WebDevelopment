from django.db import models


class CarOwner(models.Model):
    class Meta:
        db_table = "car_owner"
        verbose_name = "автовладелец"
        verbose_name_plural = "автовладельцы"

    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    first_name = models.CharField(max_length=30, verbose_name="Имя")
    birth_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")

    @property
    def full_name(self) -> str:
        return f"{self.last_name} {self.first_name}"

    full_name.fget.short_description = "Фамилия и Имя"

    def __str__(self):
        return self.full_name


class Car(models.Model):
    class Meta:
        db_table = "car"
        verbose_name = "автомобиль"
        verbose_name_plural = "автомобили"

    number = models.CharField(max_length=15, verbose_name="Государственный номер")
    brand = models.CharField(max_length=20, verbose_name="Марка")
    model = models.CharField(max_length=20, verbose_name="Модель")
    color = models.CharField(max_length=30, verbose_name="Цвет")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.number})"


class Ownership(models.Model):
    class Meta:
        db_table = "ownership"
        verbose_name = "владение"
        verbose_name_plural = "владения"

    owner = models.ForeignKey(
        CarOwner, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Владелец", related_name="ownerships"
    )
    car = models.ForeignKey(
        Car, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Автомобиль", related_name="ownerships"
    )
    start_date = models.DateTimeField(verbose_name="Дата начала")
    end_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата конца")

    def __str__(self):
        return f"{self.owner} - {self.car}"


class DrivingLicence(models.Model):
    class Meta:
        db_table = "driving_licence"
        verbose_name = "водительское удостоверение"
        verbose_name_plural = "водительские удостоверения"

    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE, verbose_name="Владелец", related_name="licences")
    number = models.CharField(max_length=10, verbose_name="Номер удостоверения")
    type = models.CharField(max_length=10, verbose_name="Тип")
    issue_date = models.DateTimeField(verbose_name="Дата выдачи")

    def __str__(self):
        return f"{self.owner} ({self.number})"
