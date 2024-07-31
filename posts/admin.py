from django.contrib import admin
from .models import Post, Comment, Reply


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Replies"
