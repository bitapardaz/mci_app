from django.db import models

class MusicStudio(models.Model):
    name = models.CharField(max_length=200,default="name")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering=['name']

class Singer(models.Model):
    name = models.CharField(max_length=100,default="name")
    image = models.ImageField(upload_to='',null=True, blank=True)

    def __unicode__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100,default="title")
    banner_image = models.ImageField(upload_to='',null=True, blank=True)
    dj_image = models.ImageField(upload_to='',null=True, blank=True)
    thumbnail = models.ImageField(upload_to='',null=True, blank=True)
    date_published = models.DateTimeField(auto_now=True, editable=True,null=True)
    singer = models.OneToOneField(Singer,null=True,blank=True)


    # fields required for deriving the top charts
    view = models.IntegerField(default = 0)
    expert_opinion = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length=100)
    date_published = models.DateTimeField(auto_now=True, editable=True,null=True)
    album = models.ManyToManyField(Album)
    music_studio = models.ForeignKey(MusicStudio,null=True)

    photo = models.ImageField(upload_to='',null=True, blank=True)
    wide_photo = models.ImageField(upload_to='',null=True, blank=True)

    # fields required for rating and deriving the top charts
    played = models.IntegerField(default=0)
    downloaded = models.IntegerField(default=0)
    liked = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class MainAdvert(models.Model):
    album = models.ForeignKey(Album,null=True,blank=True)
    miscellaneous = models.ImageField(upload_to='',null=True,blank=True)
    url = models.URLField(null=True,blank=True)
    ranking = models.IntegerField(default=0)


class TopChart(models.Model):
    album = models.ForeignKey(Album)



#class DownloadLog(models.Model):

#    user_profile = models.ForeignKey(UserProfile)
#    track = models.ForeignKey(Track)
#    time_stamp = models.DateTimeField(auto_now=True, editable=True,blank=True,null=True)

    # represents the link through which the user reached the
    # albums of interest and pushed the activation button.
#    where_i_am = models.CharField(max_length=100,null=True,blank=True)

    # represents whether this songs was actually activated or not
    # after the user sent his request.
    # on iOS it is always False
#    active = models.BooleanField(default=True,blank=True)


#    def __unicode__(self):
#        return self.user_profile.__unicode__() + " - " + self.song.__unicode__()
