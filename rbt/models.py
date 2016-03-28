from django.db import models

# Create your models here.

class Producer(models.Model):

    name = models.CharField(max_length=200)
    confirmed = models.BooleanField(default=False)


    def __unicode__(self):
        return self.name


class Category(models.Model):
    farsi_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='',null=True, blank=True)
    confirmed = models.BooleanField(default=False)


    def __unicode__(self):
        return self.farsi_name



class Album(models.Model):
    farsi_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='',null=True, blank=True)
    wide_photo = models.ImageField(upload_to='',null=True, blank=True)
    rate = models.IntegerField(default=0)
    category = models.ForeignKey(Category)
    date_published = models.DateTimeField(auto_now=True, editable=True)
    confirmed = models.BooleanField(default=False)



    def __unicode__(self):
        return self.farsi_name



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
        return str(self.activation_code) + " -- " + self.song_name + " -- " + self.producer.__unicode__()


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
