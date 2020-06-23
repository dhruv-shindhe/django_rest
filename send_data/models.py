from django.db import models

# Create your models here.

class data_store(models.Model):
    value = models.IntegerField()
