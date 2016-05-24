from django.db import models
from rbt.models import Song



class UserProfile(models.Model):
    mobile_number = models.CharField(max_length=20)
    imei = models.CharField(max_length=36)

    def __unicode__(self):
        return str(self.mobile_number)


class RBT_Activation(models.Model):
    song = models.ForeignKey(Song)
    user = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return self.song.__unicode__() + ' -- ' + self.user.__unicode__()
