from django.db import models

# Create your models here.
class Covid(models.Model):
    observationdate = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    lastupdate = models.CharField(max_length=30)
    confirmed = models.CharField(max_length=30)
    death = models.CharField(max_length=30)
    recovered = models.CharField(max_length=30)