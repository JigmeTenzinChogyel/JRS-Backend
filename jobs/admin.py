from django.contrib import admin
from .models import Jobs, Applications

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'user', 'created_at')

admin.site.register(Jobs, JobAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'job', 'created_at')

admin.site.register(Applications, ApplicationAdmin)