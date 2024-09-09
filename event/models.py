from django import forms
from django.db import models
from django.utils import timezone
# Create your models here.
class event_details(models.Model):
    def __str__(self):
        return self.event_name
    event_name = models.CharField(max_length=200)
    event_date = models.DateField()
    event_time = models.TimeField(default=timezone.now)
    event_desp = models.TextField()
    event_image = models.ImageField(max_length=1000)