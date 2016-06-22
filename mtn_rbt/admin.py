from django.contrib import admin
from models import MTN_Song, MTN_Category, MTN_SongTagAssociation, MTN_Album,MTN_CatAdvert, MTN_MainAdvert, MTN_MainPageFeatured,MTN_Category_Featured,MTN_Producer,MTN_Search_Activity

from django.utils.translation import ugettext_lazy as _


class MTN_SongInline(admin.TabularInline):

    model = MTN_Song
    fields=['song_name','mtn_song_admin_change_url','producer','music_studio','download_link']
    readonly_fields = ['mtn_song_admin_change_url']
    extra = 0



class MTN_AlbumAdmin(admin.ModelAdmin):
        fieldsets = [
            ('Album information',{'fields':['farsi_name','category','producer','music_studio','rate','confirmed','total_songs']}),
            ('Photo',{'fields':['photo','wide_photo']}),
        ]
        inlines = [MTN_SongInline]

        #fields = ['total_songs','farsi_name']
        readonly_fields = ['total_songs']

        list_display = ('farsi_name', 'category', 'total_songs','confirmed','date_published','producer','rate')
        list_filter = ['category','date_published','confirmed',]
        search_fields = ['farsi_name']


class MTN_CategoryFilter(admin.SimpleListFilter):

    title = _('Categories')
    parameter_name = 'category__id__exact'

    def lookups(self, request, model_admin):

        queryset = MTN_Category.objects.filter(confirmed=True)
        #queryset = model_admin.queryset(request).filter()
        return queryset.values_list('id','farsi_name')

    def queryset(self,reqeust,queryset):
        if self.value():
            return queryset.filter(category=self.value())

class MTN_CatAdvertAdmin(admin.ModelAdmin):

    list_display = ('category','album','miscellaneous','url')
    list_filter = (MTN_CategoryFilter,)

    class Media:
        js = ("rbt/js/filter_mtn_albums.js",)


class MTN_MainAdvertAdmin(admin.ModelAdmin):

    list_display = ('album','miscellaneous','url')


class MTN_CategoryAdmin(admin.ModelAdmin):
    list_filter = ['confirmed']


class MTN_CategoryFeaturedAdmin(admin.ModelAdmin):
    list_display = ('category','album','date_published')
    list_filter = (MTN_CategoryFilter,)

    class Media:
        js = ("rbt/js/filter_mtn_albums.js",)

class MTN_SongAdmin(admin.ModelAdmin):
    list_display = ('song_name', 'album', 'music_studio','producer')
    search_fields=['song_name', 'activation_code','producer__name']

class MTN_SongInlineProducer(admin.TabularInline):

    model = MTN_Song
    fields=['song_name','mtn_album_status','album','mtn_song_admin_change_url',]
    readonly_fields = ['mtn_song_admin_change_url','mtn_album_status',]
    extra = 0

class MTN_ProducerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields=['name']
    inlines = [MTN_SongInlineProducer]


# Register your models here.
admin.site.register(MTN_Song,MTN_SongAdmin)
admin.site.register(MTN_Category,MTN_CategoryAdmin)
admin.site.register(MTN_SongTagAssociation)
admin.site.register(MTN_Album,MTN_AlbumAdmin)
admin.site.register(MTN_CatAdvert,MTN_CatAdvertAdmin)
admin.site.register(MTN_MainAdvert,MTN_MainAdvertAdmin)
admin.site.register(MTN_MainPageFeatured)
admin.site.register(MTN_Category_Featured, MTN_CategoryFeaturedAdmin)
admin.site.register(MTN_Producer, MTN_ProducerAdmin)
admin.site.register(MTN_Search_Activity)
