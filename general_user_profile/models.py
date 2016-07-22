from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GeneralProfile(models.Model):
    user = models.ForeignKey(User)

    MCI = 'MCI'
    MTN = 'MTN'
    RightTel = 'RightTel'

    operators = (
        (MCI, 'MCI'),
        (MTN, 'MTN'),
        (RightTel, 'RightTel'),
    )

    operator = models.CharField(max_length=10,choices=operators,default=MCI)

    def __unicode__(self):
        return self.user.username
