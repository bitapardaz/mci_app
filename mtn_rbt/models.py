from rbt.models import Tag

from django.db import models
from django.core import urlresolvers

from django.contrib.staticfiles.templatetags.staticfiles import static


# Create your models here.
class MTN_Producer(models.Model):

    name = models.CharField(max_length=200)
    confirmed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering=['name']


class MTN_MusicStudio(models.Model):

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering=['name']


# Models specifically related to the MTN system.
# Some of the models use classes defined in "rbt/models."
# The classes used are Tag, Producer

class MTN_Category(models.Model):
    farsi_name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='',null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)

    def __unicode__(self):
        return  self.farsi_name



class MTN_Album(models.Model):
    farsi_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='',null=True, blank=True)
    wide_photo = models.ImageField(upload_to='',null=True, blank=True)
    rate = models.IntegerField(default=0)
    category = models.ForeignKey(MTN_Category)
    date_published = models.DateTimeField(auto_now=True, editable=True)
    confirmed = models.BooleanField(default=False)
    producer = models.ForeignKey(MTN_Producer,null=True,blank=True)
    music_studio = models.ForeignKey(MTN_MusicStudio,null=True,blank=True)

    def __unicode__(self):

        # get the number of songs in the current album.
        return self.farsi_name

    def total_songs(self):
        songs = MTN_Song.objects.filter(album=self);
        return len(songs)

    total_songs.allow_tags = True
    total_songs.short_description = 'Song Count'

    class Meta:
        ordering=['farsi_name']


class MTN_Song(models.Model):

    tone_id = models.CharField(max_length=20,default="id")
    song_name = models.CharField(max_length=200, default='name')
    activation_code = models.IntegerField(default=0)
    download_link = models.URLField(max_length=400)
    rate = models.IntegerField(default=0)
    activated = models.IntegerField(default=0)
    producer = models.ForeignKey(MTN_Producer,null=True,blank=True)
    image = models.ImageField(upload_to='',null=True, blank=True)
    price = models.IntegerField(default=300)
    album = models.ForeignKey(MTN_Album,null=True,blank=True)
    music_studio = models.ForeignKey(MTN_MusicStudio,null=True,blank=True)
    confirmed = models.BooleanField(default=False)


    def __unicode__(self):
        return self.song_name

    def mtn_song_admin_change_url(self):
        link = urlresolvers.reverse('admin:mtn_rbt_mtn_song_change',args=(self.id,))
        return u'<a href="%s">%s</a>' % (link,"Link")

    mtn_song_admin_change_url.allow_tags = True
    mtn_song_admin_change_url.short_description = 'URL'

    def mtn_album_status(self):
        if self.album == None or self.album.farsi_name.strip() == '':

            url = static('admin/img/icon_error.gif')
            return u'<img src="%s">' % url

        else:
            return u' '

    mtn_album_status.allow_tags = True
    mtn_album_status.short_description = 'Album'


class MTN_MainPageFeatured(models.Model):

    album = models.ForeignKey(MTN_Album)
    date_published = models.DateTimeField(auto_now=True, editable=True)

    def __unicode__(self):
        return self.album.farsi_name


class MTN_Category_Featured(models.Model):

    category = models.ForeignKey(MTN_Category)
    album = models.ForeignKey(MTN_Album)
    date_published = models.DateTimeField(auto_now=True, editable=True)


class MTN_SongTagAssociation(models.Model):
    song = models.ForeignKey(MTN_Song)
    tag = models.ForeignKey(Tag)

    def __unicode__(self):
        return self.song.__unicode__() + ' -- ' + self.tag.__unicode__()


class MTN_CatAdvert(models.Model):
    category = models.ForeignKey(MTN_Category,null=True,blank=True)
    album = models.ForeignKey(MTN_Album,null=True,blank=True)
    miscellaneous = models.ImageField(upload_to='',null=True,blank=True)
    url = models.URLField(null=True,blank=True)


class MTN_MainAdvert(models.Model):
    album = models.ForeignKey(MTN_Album,null=True,blank=True)
    miscellaneous = models.ImageField(upload_to='',null=True,blank=True)
    url = models.URLField(null=True,blank=True)


class MTN_Search_Activity(models.Model):
    search_term = models.CharField(max_length=20)
    time_stamp = models.DateTimeField(auto_now=True,editable=True)
    mobile_number = models.CharField(max_length=20,default=0,null=True)
    result_has_album = models.NullBooleanField(default=False)
    based_on_album = models.IntegerField(default=0,null=True)
    based_on_song = models.IntegerField(default=0,null=True)
    based_on_producer = models.IntegerField(default=0,null=True)
    location = models.CharField(max_length=200,null=True,blank=True)

    def __unicode__(self):
        return self.search_term

    def result_page_link(self):
        link="/mtnrbt/search_result_admin_internal_use/" + self.search_term + "/"
        return u'<a href="%s">%s</a>' % (link,"Result")

    result_page_link.allow_tags = True
    result_page_link.short_description = 'Result'
