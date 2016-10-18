from django.db import models

# Create your models here.
class UserDownload(models.Model):
    mobile_number = models.CharField(max_length=20)


    def __unicode__(self):
        return self.mobile_number


class DownloadCounter(models.Model):
    counter =  models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.counter)
