from django.contrib import admin
from .models import Reply


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    pass
