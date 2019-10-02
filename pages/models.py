from django.db import models

# Create your models here.
class Page(models.Model):
    myname = models.CharField(max_length=50)
    myage = models.IntegerField()