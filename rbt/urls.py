from django.conf.urls import url
import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    url(r'^register/$',views.register),

    # URLs related to homepage
    url(r'^homepage/$',views.homepage),
    url(r'^ads/$',views.main_adverts),
    url(r'^rbt_cats/$',views.rbt_cats),
    #url(r'^featured_albums/',views.featured_albums),
    url(r'^latest_albums/(?P<page>[0-9]+)/',views.latest_albums),
    #url(r'^popular_albums/',views.popular_albums),

    # URLs related to each category
    url(r'^0/homepage/$',views.homepage),
    url(r'^(?P<cat_id>[0-9]+)/homepage/$',views.cat_homepage),
    url(r'^(?P<cat_id>[0-9]+)/(?P<page>[0-9]+)/$',views.cat_albums),
    url(r'^(?P<cat_id>[0-9]+)/ads/$',views.cat_adverts),

    #URLs used in the admin interface
    url(r'^filter_albums_per_cat/$',views.filter_albums_per_cat),

    # URLs related to each Album
    url(r'^album/(?P<album_id>[0-9]+)/$',views.list_album_songs),
    url(r'^album_full_information/(?P<album_id>[0-9]+)/$',views.album_full_information),



    # search functionality
    url(r'^search/$',views.search),
    url(r'^search_album_more/(?P<page>[0-9]+)/$',views.search_album_more),
    url(r'^search_song_albums_more/(?P<page>[0-9]+)/$',views.search_song_albums_more),
    url(r'^search_producer_albums_more/(?P<page>[0-9]+)/$',views.search_producer_albums_more),


    # album activation
    url(r'^activation_request/$',views.activation_request),
    url(r'^verify_activation_request/$',views.verify_activation_request),


    # the purpose of having the following url is not clear.
    url(r'^album_select/',views.album_select),



    # Depricated URLs
    url(r'^list/$',views.list),
    url(r'^list_cat/(?P<cat_name>[a-zA-Z]+)/(?P<page>[0-9]+)/$',views.list_cat),
    url(r'^popular_songs/(?P<page>[0-9]+)/$',views.popular_songs),
    url(r'^latest_songs/(?P<page>[0-9]+)/$',views.latest_songs),



]

urlpatterns = format_suffix_patterns(urlpatterns)
