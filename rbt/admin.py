from django.contrib import admin
from models import Producer, Song, Tag, Category, SongTagAssociation, Album,CatAdvert, MainAdvert, MainPageFeatured,Category_Featured

class SongInline(admin.TabularInline):
    model = Song
    fields=['song_name','song_admin_change_url','price','download_link']
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

        list_display = ('farsi_name', 'category', 'total_songs','confirmed','date_published','producer','rate')
        list_filter = ['category','date_published','confirmed']
        search_fields = ['farsi_name']


class CatAdvertAdmin(admin.ModelAdmin):

    list_display = ('category','album','miscellaneous','url')

    class Media:
        js = ("rbt/js/filter_albums.js",)


class MainAdvertAdmin(admin.ModelAdmin):

    list_display = ('album','miscellaneous','url')


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['confirmed']


class CategoryFeaturedAdmin(admin.ModelAdmin):
    list_display = ('category','album','date_published')

    class Media:
        js = ("rbt/js/filter_albums.js",)

class SongAdmin(admin.ModelAdmin):
    search_fields=['song_name']

# Register your models here.
admin.site.register(Producer)
admin.site.register(Song,SongAdmin)
admin.site.register(Tag)
admin.site.register(Category,CategoryAdmin)
admin.site.register(SongTagAssociation)
admin.site.register(Album,AlbumAdmin)
admin.site.register(CatAdvert,CatAdvertAdmin)
admin.site.register(MainAdvert,MainAdvertAdmin)
admin.site.register(MainPageFeatured)
admin.site.register(Category_Featured, CategoryFeaturedAdmin)
