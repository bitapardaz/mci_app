from django.db import models
from rbt.models import Song
from django.contrib.auth.models import User

class UserProfile(models.Model):
    mobile_number = models.CharField(max_length=20)
    token = models.CharField(max_length=160, null=True,blank=True)
    user = models.ForeignKey(User,null=True,blank=True)

    def __unicode__(self):
        return str(self.mobile_number)


class ActivationRequest(models.Model):

    user_profile = models.ForeignKey(UserProfile)
    song = models.ForeignKey(Song)
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
