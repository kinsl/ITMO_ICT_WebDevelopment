from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from apps.oidc.models import ItmoIdProfile


class ItmoIdProfileInline(admin.StackedInline):
    model = ItmoIdProfile
    can_delete = True
    verbose_name = "профиль ITMO.ID"
    verbose_name_plural = "профили ITMO.ID"


class UserAdmin(BaseUserAdmin):
    list_display = ["username", "get_full_name", "get_isu", "get_course", "get_faculty", "get_group"]
    list_filter = ["profile__course", "profile__faculty"]
    search_fields = ["username", "last_name", "first_name", "profile__isu"]
    inlines = [ItmoIdProfileInline]

    @admin.display(description="Фамилия и имя", ordering="last_name")
    def get_full_name(self, obj: User) -> str:
        return f"{obj.last_name} {obj.first_name}"

    @admin.display(description="ИСУ")
    def get_isu(self, obj: User) -> int:
        return obj.profile.isu

    @admin.display(description="Курс")
    def get_course(self, obj: User) -> int:
        return obj.profile.course

    @admin.display(description="Факультет")
    def get_faculty(self, obj: User) -> str:
        return obj.profile.faculty

    @admin.display(description="Группа")
    def get_group(self, obj: User) -> str:
        return obj.profile.group


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
