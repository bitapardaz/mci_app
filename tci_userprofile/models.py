from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User)
    # if a user enters wrong pin2 three times in a row, then the
    # is_active becomes false, and the user cannot proceed to payment
    # any more.
    is_active = models.BooleanField(default=True)
    last_visit = models.DateTimeField()
    sms_verified = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username

class MobileDevice(models.Model):
    imei = models.CharField(max_length=20)
    user_profile = models.ForeignKey(UserProfile)

    token_string = models.CharField(max_length=160, null=True,blank=True)
    sms_verification_code = models.CharField(max_length=10)
    sms_code_expiery = models.DateTimeField()
