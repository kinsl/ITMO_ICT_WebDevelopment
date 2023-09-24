from django.contrib import admin
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe

from .models import Airline, Flight, Booking, Feedback


admin.site.site_title = "Админ-панель Авиаперелётов"
admin.site.site_header = "Админ-панель Авиаперелётов"


@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ("name", "get_flights_count")
    search_fields = ("name",)
    readonly_fields = ("get_flights",)

    @admin.display(description="Количество рейсов")
    def get_flights_count(self, obj):
        return f"{obj.flights.count()}"

    @admin.display(description="Рейсы")
    def get_flights(self, obj):
        formatted_flights = []

        for flight in obj.flights.select_related("airline").all():
            flight_url = reverse(f"admin:{flight._meta.app_label}_{flight._meta.model_name}_change", args=(flight.pk,))
            type_ = flight.get_type_display()
            gate = flight.gate
            date = timezone.localtime(flight.date)

            formatted_flights.append(
                f"<a href='{flight_url}'>{type_}, {gate} - {date.strftime('%d.%m.%y %H:%M')}</a>"
            )

        return mark_safe("<br>".join(formatted_flights))


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ("airline", "type", "gate", "date")
    search_fields = ("airline__name",)
    list_filter = ["airline", "type", "gate"]
    readonly_fields = ("get_bookings",)

    @admin.display(description="Брони")
    def get_bookings(self, obj):
        formatted_bookings = []

        for booking in obj.bookings.select_related("user").all():
            booking_url = reverse(
                f"admin:{booking._meta.app_label}_{booking._meta.model_name}_change", args=(booking.pk,)
            )
            user_full_name = f"{booking.user.last_name} {booking.user.first_name}"
            user_username = booking.user.username
            user = f"<a href='{booking_url}'>{user_full_name if user_full_name != ' ' else user_username}</a>"
            registered = "✅" if booking.registered else "❌"
            ticket = str(booking.ticket) if booking.ticket else ""

            formatted_bookings.append(f"{user} ({registered}{', ' + ticket if ticket else ''})")

        return mark_safe("<br>".join(formatted_bookings))


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("get_user", "get_airline", "get_type", "get_gate", "get_date", "registered", "ticket")
    search_fields = ("user__last_name", "user__first_name", "flight__airline")
    list_filter = ["flight__airline", "flight__type", "flight__gate", "registered"]
    list_editable = ("registered", "ticket")

    @admin.display(ordering="user__last_name", description="Пассажир")
    def get_user(self, obj):
        full_name = f"{obj.user.last_name} {obj.user.first_name}"
        return full_name if full_name != " " else obj.user.username

    @admin.display(ordering="flight__airline", description="Авиакомпания")
    def get_airline(self, obj):
        return obj.flight.airline

    @admin.display(ordering="flight__type", description="Тип")
    def get_type(self, obj):
        return obj.flight.get_type_display()

    @admin.display(ordering="flight__gate", description="Гейт")
    def get_gate(self, obj):
        return obj.flight.gate

    @admin.display(ordering="flight__date", description="Дата")
    def get_date(self, obj):
        return obj.flight.date


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("get_user", "get_airline", "get_type", "get_gate", "get_date", "text", "rating", "date")
    search_fields = ("user__last_name", "user__first_name", "flight__airline")
    list_filter = ["flight__airline", "flight__type", "flight__gate", "rating"]

    @admin.display(ordering="user__last_name", description="Пассажир")
    def get_user(self, obj):
        return f"{obj.user.last_name} {obj.user.first_name}"

    @admin.display(ordering="flight__airline", description="Авиакомпания")
    def get_airline(self, obj):
        return obj.flight.airline

    @admin.display(ordering="flight__type", description="Тип")
    def get_type(self, obj):
        return obj.flight.get_type_display()

    @admin.display(ordering="flight__gate", description="Гейт")
    def get_gate(self, obj):
        return obj.flight.gate

    @admin.display(ordering="flight__date", description="Дата рейса")
    def get_date(self, obj):
        return obj.flight.date
