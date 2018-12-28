from django.contrib import admin
from .models import Client, Task, Version


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ['name', 'current_task']
    readonly_fields = ['mac_address', 'public_key', 'created', 'updated']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ['script_id', 'script', 'client', 'assigned', 'completed']

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    fields = ['release_url', 'os_version']
    readonly_fields = ['version_id', 'created']
