from django.contrib import admin

from .models import *


class RocketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'location', 'agency', 'is_published', 'user')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'user')
    prepopulated_fields = {"slug": ("title",)}


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class AgencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class LauncherAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'family', 'full_name')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Rocket, RocketAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Agency, AgencyAdmin)
admin.site.register(Launcher, LauncherAdmin)
admin.site.register(Event, EventAdmin)


