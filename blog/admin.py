from django.db import models
from django.contrib import admin
from .models import News, Article, ArticleImage
from unfold.admin import ModelAdmin, StackedInline, TabularInline
from unfold.contrib.forms.widgets import WysiwygWidget


class ArticleImageInline(StackedInline):
    model = ArticleImage
    extra = 1
    ordering = ['-id']
    fields = ['image']
    max_num = 1

@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
    warn_unsaved_form = True
    compressed_fields = True
    change_form_show_cancel_button = True

    readonly_fields = ["id", "slug", "created_at", "updated_at"]

    fieldsets = (
        ('Идентификаторы', {
            'fields': ('id', "slug", 'created_at', 'updated_at'),
        }),
        ('Основная информация', {
            'fields': ('title', 'content',)
        }),
    )

    inlines = [ArticleImageInline]