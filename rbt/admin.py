from django.contrib import admin
from models import Producer, Song, Tag, Category, SongTagAssociation, Album

class SongInline(admin.TabularInline):
    model = Song
    fields=['song_name','song_admin_change_url','producer','price']
    readonly_fields = ['song_admin_change_url',]
    extra = 0




class AlbumAdmin(admin.ModelAdmin):
        fieldsets = [
            ('Album information',{'fields':['farsi_name','category','rate','confirmed','total_songs']}),
            ('Photo',{'fields':['photo','wide_photo']}),
        ]
        inlines = [SongInline]

        #fields = ['total_songs','farsi_name']
        readonly_fields = ['total_songs']


        list_display = ('farsi_name', 'category', 'total_songs','confirmed','date_published')
        list_filter = ['category','date_published','confirmed']
        search_fields = ['farsi_name']


# Register your models here.
admin.site.register(Producer)
admin.site.register(Song)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(SongTagAssociation)
admin.site.register(Album,AlbumAdmin)
