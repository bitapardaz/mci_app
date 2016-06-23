from django.db import models
from mtn_rbt.models import MTN_Song

# Create your models here.
class MTN_UserProfile(models.Model):
    mobile_number = models.CharField(max_length=20)
    token = models.CharField(max_length=160, null=True,blank=True)

    def __unicode__(self):
        return str(self.mobile_number)


class MTN_RBT_Activation(models.Model):
    song = models.ForeignKey(MTN_Song)
    user = models.ForeignKey(MTN_UserProfile)

    def __unicode__(self):
        return self.song.__unicode__() + ' -- ' + self.user.__unicode__()
