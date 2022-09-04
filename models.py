from statistics import mode
from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=50)
    notes = models.CharField(max_length=5000)
    created_at = models.CharField(null=True,max_length=50)
