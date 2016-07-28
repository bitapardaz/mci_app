from django.db import models

# Create your models here.
class UserProfile(models.Model):
    is_active = models.BooleanField(default=True)
    imei = models.CharField(max_length=20)
    last_visit = models.DateTimeField()
