from django.db import models

# Create your models here.
class Phone(models.Model):
    tel_no = models.CharField(max_length=20)
