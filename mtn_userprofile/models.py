from django.db import models
from mtn_rbt.models import MTN_Song
from django.contrib.auth.models import User
from general_user_profile.models import GeneralProfile


# Create your models here.
class MTN_UserProfile(models.Model):
    mobile_number = models.CharField(max_length=20)
    token = models.CharField(max_length=160, null=True,blank=True)
    general_profile = models.ForeignKey(GeneralProfile,null=True,blank=True)


    def __unicode__(self):
        return str(self.mobile_number)


class MTN_ActivationRequest(models.Model):

    user_profile = models.ForeignKey(MTN_UserProfile)
    song = models.ForeignKey(MTN_Song)
    time_stamp = models.DateTimeField(auto_now=True, editable=True,blank=True,null=True)

    # represents the link through which the user reached the
    # albums of interest and pushed the activation button.
    where_i_am = models.CharField(max_length=100,null=True,blank=True)

    # represents whether this songs was actually activated or not
    # after the user sent his request.
    # on iOS it is always False
    activated = models.BooleanField(default=False,blank=True)


    def __unicode__(self):
        return self.user_profile.__unicode__() + " - " + self.song.__unicode__()
