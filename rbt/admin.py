from django.contrib import admin
from models import Producer, Song, Tag, Category, SongTagAssociation, Album,CatAdvert

class SongInline(admin.TabularInline):
    model = Song
    fields=['song_name','song_admin_change_url','producer','price','download_link']
    readonly_fields = ['song_admin_change_url']
    extra = 0


class AlbumAdmin(admin.ModelAdmin):
        fieldsets = [
            ('Album information',{'fields':['farsi_name','category','producer','pseudo_producer','rate','confirmed','total_songs']}),
            ('Photo',{'fields':['photo','wide_photo']}),
        ]
        inlines = [SongInline]

        #fields = ['total_songs','farsi_name']
        readonly_fields = ['total_songs']


        list_display = ('farsi_name', 'category', 'total_songs','confirmed','date_published')
        list_filter = ['category','date_published','confirmed']
        search_fields = ['farsi_name']


class CatAdvertAdmin(admin.ModelAdmin):

    list_display = ('category','album')
    list_filter = ['category']
    search_fields = ['category__english_name']



# Register your models here.
admin.site.register(Producer)
admin.site.register(Song)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(SongTagAssociation)
admin.site.register(Album,AlbumAdmin)
admin.site.register(CatAdvert,CatAdvertAdmin)
