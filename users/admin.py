from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        (
            ("Personal info"),
            {
                "fields": ("name", "email"),
            },
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": (
                    "wide",
                    "extrapretty",
                ),
                "fields": (
                    "username",
                    "name",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_display = ("username", "name", "is_staff")
