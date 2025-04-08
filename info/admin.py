from django.db import models
from django.contrib import admin
from .models import FAQ
from unfold.admin import ModelAdmin, StackedInline, TabularInline
from unfold.contrib.forms.widgets import WysiwygWidget



@admin.register(FAQ)
class FAQAdmin(ModelAdmin):
    list_display = ('question',)
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
    warn_unsaved_form = True
    compressed_fields = True
    change_form_show_cancel_button = True
