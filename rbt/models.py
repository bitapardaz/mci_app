from django.db import models

# Create your models here.

class Producer(models.Model):

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name



class Song(models.Model):

    song_name = models.CharField(max_length=200, default='name')
    activation_code = models.IntegerField(default=0)
    download_link = models.URLField(max_length=400)
    rate = models.IntegerField(default=0)
    activated = models.IntegerField(default=0)
    producer = models.ForeignKey(Producer,null=True,blank=True)
    image = models.ImageField(upload_to='images/',null=True, blank=True)


    def __unicode__(self):
        return self.song_name + " -- " + self.producer.__unicode__()
