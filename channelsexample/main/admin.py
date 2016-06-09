from django.contrib.admin import ModelAdmin, register

from main.models import (
    Asset,
    Project,
)


@register(Asset)
class AssetAdmin(ModelAdmin):
    list_display = ('name', 'project', )


@register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ('name', )
