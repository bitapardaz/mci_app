from django.contrib import admin
from models import Producer, Song, Tag, Category, SongTagAssociation, Album,CatAdvert, MainAdvert, MainPageFeatured,Category_Featured, Search_Activity
from django.utils.translation import ugettext_lazy as _


class SongInline(admin.TabularInline):

    model = Song
    fields=['song_name','song_admin_change_url','producer','download_link']
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


class CategoryFilter(admin.SimpleListFilter):

    title = _('Categories')
    parameter_name = 'category__id__exact'

    def lookups(self, request, model_admin):

        #return [
        #            ('80s', _('in the eighties')),
        #            ('90s', _('in the nineties')),
        #        ]

        queryset = Category.objects.filter(confirmed=True)
        #queryset = model_admin.queryset(request).filter()
        return queryset.values_list('id','farsi_name')

    def queryset(self,reqeust,queryset):
        if self.value():
            return queryset.filter(category=self.value())

class CatAdvertAdmin(admin.ModelAdmin):

    list_display = ('category','album','miscellaneous','url')
    list_filter = (CategoryFilter,)

    class Media:
        js = ("rbt/js/filter_albums.js",)


class MainAdvertAdmin(admin.ModelAdmin):

    list_display = ('album','miscellaneous','url')


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['confirmed']


class CategoryFeaturedAdmin(admin.ModelAdmin):
    list_display = ('category','album','date_published')
    list_filter = (CategoryFilter,)



    class Media:
        js = ("rbt/js/filter_albums.js",)

class SongAdmin(admin.ModelAdmin):
    list_display = ('song_name', 'producer', 'album')
    search_fields=['song_name', 'activation_code','producer__name']

class SongInlineProducer(admin.TabularInline):

    model = Song
    fields=['song_name','album_status','album','song_admin_change_url',]
    readonly_fields = ['song_admin_change_url','album_status',]
    extra = 0

class ProducerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields=['name']
    inlines = [SongInlineProducer]


class SearchActivityAdmin(admin.ModelAdmin):
    list_display=('search_term','time_stamp',)
    search_fields=['search_term']

# Register your models here.
admin.site.register(Producer,ProducerAdmin)
admin.site.register(Song,SongAdmin)
admin.site.register(Tag)
admin.site.register(Category,CategoryAdmin)
admin.site.register(SongTagAssociation)
admin.site.register(Album,AlbumAdmin)
admin.site.register(CatAdvert,CatAdvertAdmin)
admin.site.register(MainAdvert,MainAdvertAdmin)
admin.site.register(MainPageFeatured)
admin.site.register(Category_Featured, CategoryFeaturedAdmin)
admin.site.register(Search_Activity,SearchActivityAdmin)
