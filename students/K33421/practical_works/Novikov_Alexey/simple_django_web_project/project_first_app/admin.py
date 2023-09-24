from django.contrib import admin

from .models import CarOwner, Car, Ownership, DrivingLicence


admin.site.site_title = 'Админ-панель АвтоВладений'
admin.site.site_header = 'Админ-панель АвтоВладений'


@admin.register(CarOwner)
class CarOwnerAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "birth_date")
    search_fields = ("last_name", "first_name")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("number", "brand", "model", "color")
    search_fields = ("number", "brand", "model", "color")
    list_filter = ["brand", "model", "color"]


@admin.register(Ownership)
class OwnershipAdmin(admin.ModelAdmin):
    list_display = ("get_owner", "get_car", "start_date", "end_date")
    search_fields = ("owner__last_name", "owner__first_name", "car__number", "car__brand", "car__model", "car__color")
    list_filter = ["car__brand", "car__model", "car__color"]

    @admin.display(ordering="owner__last_name", description="Владелец")
    def get_owner(self, obj):
        return f"{obj.owner}"

    @admin.display(ordering="car_brand", description="Автомобиль")
    def get_car(self, obj):
        return f"{obj.car}"


@admin.register(DrivingLicence)
class DrivingLicenceAdmin(admin.ModelAdmin):
    list_display = ("get_owner", "number", "type", "issue_date")
    search_fields = ("owner__last_name", "owner__first_name", "number", "type")
    list_filter = ["type"]

    @admin.display(ordering="owner__last_name", description="Владелец")
    def get_owner(self, obj):
        return f"{obj.owner}"
