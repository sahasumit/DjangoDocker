from django.db import models
import datetime
# Create your models here.
class Store(models.Model):
    key=models.TextField(blank=False,unique=True,primary_key=True)
    value=models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
