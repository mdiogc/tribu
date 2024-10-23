from django.db import models


# Create your models here.
class Echos(models.Model):
    content = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
