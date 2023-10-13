from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from accounts.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    image = models.ImageField(blank=True)
    genre = models.CharField(max_length=50)
    score = models.FloatField()

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)