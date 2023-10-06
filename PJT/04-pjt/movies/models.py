from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    # movie_image = models.ImageField(blank=True)
