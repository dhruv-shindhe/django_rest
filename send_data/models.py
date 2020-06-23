from django.db import models

# Create your models here.

class data_store(models.Model):
    amplitude = models.FloatField(null=True)
    time = models.FloatField(null=True)
