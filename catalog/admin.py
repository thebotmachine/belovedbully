from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline, TabularInline
from .models import Dog, DogImage, Litter, LitterImage


class DogImageInline(StackedInline):
    model = DogImage
    extra = 1
    ordering = ['-id']
    fields = ['image']


@admin.register(Dog)
class DogAdmin(ModelAdmin):
    list_display = ['name', 'gender', 'category','birth_date', 'status', 'created_at', 'updated_at']
    search_fields = ['name', 'color', 'pedigree']
    list_filter = ['category', 'gender', 'color', 'status', 'created_at', 'updated_at' ]
    ordering = ['-id']
    warn_unsaved_form = True
    compressed_fields = True
    change_form_show_cancel_button = True
    raw_id_fields = ['litter']
    conditional_fields = {
        "status": "category == 'puppy'",
        "price": "category == 'puppy'",
        "litter": "category == 'puppy'",
    }

    readonly_fields = ["id", "slug", "created_at", "updated_at"]

    fieldsets = (
        ('Идентификаторы', {
            'fields': ('id', "slug", 'created_at', 'updated_at'),
        }),
        ('Основная информация', {
            'fields': ('name', 'gender', 'birth_date', 'category', 'status', 'price', 'litter')
        }),
        ('Дополнительно', {
            'fields': ('color', 'dog_type', 'pedigree', 'description')
        }),
    )

    inlines = [DogImageInline]


class LitterImageInline(StackedInline):
    model = LitterImage
    extra = 1
    ordering = ['-id']
    fields = ['image']


@admin.register(Litter)
class LitterAdmin(ModelAdmin):
    list_display = ['father', 'mother', 'birth_date']
    search_fields = ['birth_date']
    list_filter = ['father', 'mother', 'birth_date']
    ordering = ['-id']
    warn_unsaved_form = True
    compressed_fields = True
    change_form_show_cancel_button = True
    readonly_fields = ["id", "slug", "created_at", "updated_at"]
    raw_id_fields = ['father', 'mother']

    fieldsets = (
        ('Идентификаторы', {
            'fields': ('id', "slug", 'created_at', 'updated_at'),
        }),
        ('Основная информация', {
            'fields': ('father', 'mother', 'birth_date')
        }),

    )

    inlines = [LitterImageInline]
