from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.utils import timezone


class Airline(models.Model):
    class Meta:
        db_table = "airline"
        verbose_name = "авиакомпания"
        verbose_name_plural = "авиакомпании"

    name = models.CharField(max_length=50, verbose_name="Название")

    def __str__(self):
        return self.name


class Flight(models.Model):
    class Meta:
        db_table = "flight"
        verbose_name = "рейс"
        verbose_name_plural = "рейсы"

    class Type(models.TextChoices):
        DEPARTURE = "departure", "Отлёт"
        ARRIVAL = "arrival", "Прилёт"

    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name="flights", verbose_name="Авиакомпания")
    type = models.CharField(max_length=9, choices=Type.choices, verbose_name="Тип")
    gate = models.CharField(max_length=5, verbose_name="Гейт")
    date = models.DateTimeField(verbose_name="Время отправления")

    def __str__(self):
        return (
            f"{self.airline} ({self.get_type_display()}), "
            f"{self.gate} - {timezone.localtime(self.date).strftime('%d.%m.%y %H:%M')}"
        )


class Booking(models.Model):
    class Meta:
        db_table = "booking"
        verbose_name = "бронь"
        verbose_name_plural = "брони"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings", verbose_name="Пассажир")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="bookings", verbose_name="Рейс")
    registered = models.BooleanField(default=False, verbose_name="Зарегистрирован?")
    ticket = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Номер билета")

    def __str__(self):
        user_full_name = f"{self.user.last_name} {self.user.first_name}"
        return f"{user_full_name if user_full_name != ' ' else self.user.username} - {self.flight}"


class Feedback(models.Model):
    class Meta:
        db_table = "feedback"
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks", verbose_name="Пассажир")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="feedbacks", verbose_name="Рейс")
    text = models.TextField(verbose_name="Текст")
    rating = models.PositiveSmallIntegerField(
        validators=[validators.MinValueValidator(1), validators.MaxValueValidator(10)], verbose_name="Рейтинг"
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name} - {self.flight}"
