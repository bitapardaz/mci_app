from django.db import models

# Create your models here.
class UserDownload(models.Model):
    mobile_number = models.CharField(max_length=20)

    
