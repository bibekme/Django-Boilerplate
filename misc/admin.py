from django.contrib import admin

from .models import Config


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ["idx", "app", "key", "value", "created_on"]
    search_fields = ["app", "key", "value"]
    list_filter = ["created_on", "app"]
    readonly_fields = ["created_on", "modified_on"]
