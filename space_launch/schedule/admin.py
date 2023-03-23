from django.contrib import admin

from .models import *


class RocketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'location', 'agency', 'time_launch', 'is_published', 'user')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'content', 'time_launch')
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



admin.site.register(Rocket, RocketAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Agency, AgencyAdmin)
admin.site.register(Launcher, LauncherAdmin)


