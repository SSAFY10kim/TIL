from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    image = models.ImageField(blank=True)
    