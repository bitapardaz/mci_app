from django.db import models

# Create your models here.
class Phone(models.Model):
    tel_no = models.CharField(max_length=20)

    def __unicode__(self):
        return self.tel_no
