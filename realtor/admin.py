from django.contrib import admin
from django.utils.html import format_html

from .models import *


# ----------------------------------------
# Inline для модели EstateImage
class EstateImageInline(admin.TabularInline):  # Или admin.StackedInline
    model = EstateImage
    extra = 1  # Количество пустых форм для добавления
    readonly_fields = ('display_image',)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return "No Image"

    display_image.short_description = 'Фото'


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    inlines = [EstateImageInline]  # Добавляем inline
    prepopulated_fields = {"slug": ("operation","category", "type", "name")} # формируем поле "slug" автоматически из полей "id", "type" и "category"
    list_display = ('id', 'operation', 'name', 'category', 'type', 'status', 'city', 'district', 'time_create', 'time_update',)
    readonly_fields = ['creator', 'modifier', ]
    list_display_links = ('name',)
    # list_editable = ('name',)
    list_per_page = 10
    search_fields = ('name', 'category',)
    list_filter = ('category', 'status', 'city', 'district',)
    save_on_top = True

    def save_model(self, request, obj, form, change):
        if not obj.creator_id:  # Если поле user не заполнено
            obj.creator = request.user  # Заполняем текущим пользователем
        obj.modifier = request.user  # Заполняем текущим пользователем
        super().save_model(request, obj, form, change)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_id')
    list_display_links = ('id', 'name')
    list_filter = ('category_id__name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    # list_display = ('id', 'name', 'city_id__name')
    list_display = ('id', 'name', 'city_id')
    list_display_links = ('id', 'name')
    list_filter = ('city_id__name',)