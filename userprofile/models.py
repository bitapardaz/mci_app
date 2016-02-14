from django.db import models
from rbt.models import Song



class UserProfile(models.Model):
    mobile_number = models.IntegerField(default=0)

    def __unicode__(self):
        return str(mobile_number)



class RBT_Activation(models.Model):
    song = models.ForeignKey(Song)
    user = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return song.__unicode__ + ' -- ' + user.__unicode__()
