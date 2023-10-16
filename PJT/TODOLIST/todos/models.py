from django.db import models
import datetime
from django.conf import settings

# Create your models here.
class Todolist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    target_day = models.DateField(null=True, blank=True)


class Comment(models.Model):
    todo = models.ForeignKey(Todolist, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)