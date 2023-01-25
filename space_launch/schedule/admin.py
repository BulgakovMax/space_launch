from django.contrib import admin

from .models import *


class RocketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'time_launch', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'content', 'time_launch')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Rocket, RocketAdmin)
admin.site.register(Type, TypeAdmin)
