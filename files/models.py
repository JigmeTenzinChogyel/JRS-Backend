from django.db import models
from users.models import CustomUser
from jobs.models import Jobs

# Create your models here.

class Files(models.Model):
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    mimetype = models.CharField(max_length=256)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='files')
    job = models.ForeignKey(Jobs, on_delete=models.SET_NULL, null=True, related_name='files')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name