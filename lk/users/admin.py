from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    #add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
    list_display = ["username", "inn", "snils", "birthday"]

    fieldsets = UserAdmin.fieldsets + (
        ("Реквизиты 1С", {"fields": ("snils", "inn", "birthday", "surname")}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Реквизиты 1С", {"fields": ("snils", "inn", "birthday", "surname",)}),
    )

    search_fields = ("snils", "inn", "birthday")
    ordering = ("snils", "inn", "birthday")
