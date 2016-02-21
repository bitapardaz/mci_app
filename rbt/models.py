from django.db import models

# Create your models here.

class Producer(models.Model):

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    farsi_title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='',null=True, blank=True)

    def __unicode__(self):
        return self.name


class Song(models.Model):

    song_name = models.CharField(max_length=200, default='name')
    activation_code = models.IntegerField(default=0)
    download_link = models.URLField(max_length=400)
    rate = models.IntegerField(default=0)
    activated = models.IntegerField(default=0)
    producer = models.ForeignKey(Producer,null=True,blank=True)
    image = models.ImageField(upload_to='',null=True, blank=True)
    category = models.ForeignKey(Category)
    price = models.IntegerField(default=0)
    date_published = models.DateTimeField(auto_now=True, editable=True)


    def __unicode__(self):
        return self.song_name + " -- " + self.producer.__unicode__()


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
