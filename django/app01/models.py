from django.db import models

# Create your models here.

class Picture(models.Model):
    img = models.ImageField(upload_to="", blank=True)