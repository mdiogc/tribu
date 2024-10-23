from django.conf import settings
from django.db import models


# Create your models here.
class Wave(models.Model):
    content = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    echos = models.ForeignKey('echos.Echos', related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
