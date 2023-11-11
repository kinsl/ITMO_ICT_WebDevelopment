from django.contrib import admin

from apps.adapter.models import Adapter


@admin.register(Adapter)
class AdapterAdmin(admin.ModelAdmin):
    list_display = ["get_full_name"]

    @admin.display(description="Фамилия и имя")
    def get_full_name(self, obj: Adapter) -> str:
        return f"{obj.last_name} {obj.first_name}"
