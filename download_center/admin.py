from django.contrib import admin
from models import Album, MusicStudio,Singer,Track,MainAdvert,TopChart


class SingerAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields=['name',]


class TrackAlbumInline(admin.TabularInline):
    model = Track.album.through
    extra = 0


class MainAdvertAdmin(admin.ModelAdmin):

    list_display = ('album','ranking','miscellaneous','url')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title','dj_image','banner_image','thumbnail','date_published','singer')
    search_fields=['title',]
    inlines = (TrackAlbumInline,)


class TrackAdmin(admin.ModelAdmin):
    list_display = ('title','date_published','music_studio','played','downloaded','liked')
    search_fields=['title',]
    inlines = (TrackAlbumInline,)
    exclude=('album',)

class TopChartAdmin(admin.ModelAdmin):
    list_display = ('album',)


#class DownloadLog(admin.ModelAdmin):
#    list_display = ('user_profile','track','time_stamp','active')
#    search_fields = (track)


# Register your models here.
admin.site.register(TopChart,TopChartAdmin)
admin.site.register(MusicStudio)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Singer,SingerAdmin)
admin.site.register(Track,TrackAdmin)
admin.site.register(MainAdvert,MainAdvertAdmin)
