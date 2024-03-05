from django.contrib import admin
from .models import Files

# Register your models here.

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'caption', 'url', 'mimetype', 'user', 'job', 'created_at', 'updated_at', 'deleted_at')

admin.site.register(Files, FileAdmin)