from django.conf import settings
from django.db import models
from django.utils import timezone
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

class Voetbalspelers(models.Model):
    name = models.CharField(max_length=20)
    club = models.CharField(max_length=20)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    last_change_date = (22-1-2026)

    
def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.titl

