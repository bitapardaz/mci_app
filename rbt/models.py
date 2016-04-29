from django.db import models
from django.core import urlresolvers

# Create your models here.

class Producer(models.Model):

    name = models.CharField(max_length=200)
    confirmed = models.BooleanField(default=False)


    def __unicode__(self):
        return self.name


class Category(models.Model):
    farsi_name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='',null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)


    def __unicode__(self):
        return self.farsi_name



class PseudoProducer(models.Model):

    name = models.CharField(max_length=200)
    confirmed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Album(models.Model):
    farsi_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='',null=True, blank=True)
    wide_photo = models.ImageField(upload_to='',null=True, blank=True)
    rate = models.IntegerField(default=0)
    category = models.ForeignKey(Category)
    date_published = models.DateTimeField(auto_now=True, editable=True)
    confirmed = models.BooleanField(default=False)
    producer = models.ForeignKey(Producer,null=True,blank=True)
    pseudo_producer = models.ForeignKey(PseudoProducer,null=True,blank=True)

    def __unicode__(self):

        # get the number of songs in the current album.
        return self.farsi_name

    def total_songs(self):
        songs = Song.objects.filter(album=self);
        return len(songs)

    total_songs.allow_tags = True
    total_songs.short_description = 'Song Count'


class Song(models.Model):

    song_name = models.CharField(max_length=200, default='name')
    activation_code = models.IntegerField(default=0)
    download_link = models.URLField(max_length=400)
    rate = models.IntegerField(default=0)
    activated = models.IntegerField(default=0)
    producer = models.ForeignKey(Producer,null=True,blank=True)
    image = models.ImageField(upload_to='',null=True, blank=True)
    price = models.IntegerField(default=300)
    album = models.ForeignKey(Album,null=True,blank=True)
    confirmed = models.BooleanField(default=False)


    def __unicode__(self):
        return self.song_name

    def song_admin_change_url(self):
        link = urlresolvers.reverse('admin:rbt_song_change',args=(self.id,))
        return u'<a href="%s">%s</a>' % (link,"Link")

    song_admin_change_url.allow_tags = True
    song_admin_change_url.short_description = 'URL'


class MainPageFeatured(models.Model):

    album = models.ForeignKey(Album)
    date_published = models.DateTimeField(auto_now=True, editable=True)

    def __unicode__(self):
        return self.album.farsi_name


class Category_Featured(models.Model):

    category = models.ForeignKey(Category)
    song = models.ForeignKey(Song)

    def __unicode__(self):
        return song.__unicode__() + ' -- ' + category.__unicode__()


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class SongTagAssociation(models.Model):
    song = models.ForeignKey(Song)
    tag = models.ForeignKey(Tag)

    def __unicode__(self):
        return self.song.__unicode__() + ' -- ' + self.tag.__unicode__()



class CatAdvert(models.Model):
    category = models.ForeignKey(Category)
    album = models.ForeignKey(Album)
    miscellaneous = models.ImageField(upload_to='',null=True,blank=True)
    url = models.URLField(null=True,blank=True)


class MainAdvert(models.Model):
    album = models.ForeignKey(Album,null=True,blank=True)
    miscellaneous = models.ImageField(upload_to='',null=True,blank=True)
    url = models.URLField(null=True,blank=True)
