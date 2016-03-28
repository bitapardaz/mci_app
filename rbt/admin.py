from django.contrib import admin
from models import Producer, Song, Tag, Category, SongTagAssociation, Album

# Register your models here.
admin.site.register(Producer)
admin.site.register(Song)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(SongTagAssociation)
admin.site.register(Album)
