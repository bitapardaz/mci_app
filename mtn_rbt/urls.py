from django.conf.urls import url
from mtn_rbt import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^register/$',views.register),

    # URLs related to homepage
    url(r'^homepage/$',views.homepage),
    url(r'^latest_albums/(?P<page>[0-9]+)/',views.latest_albums),


    # URLs related to each category
    url(r'^0/homepage/$',views.homepage),
    url(r'^(?P<cat_id>[0-9]+)/homepage/$',views.cat_homepage),
    url(r'^(?P<cat_id>[0-9]+)/(?P<page>[0-9]+)/$',views.cat_albums),

    # URLs related to each Album
    url(r'^album/(?P<album_id>[0-9]+)/$',views.list_album_songs),
    url(r'^album_full_information/(?P<album_id>[0-9]+)/$',views.album_full_information),


    #URLs used in the admin interface
    url(r'^filter_albums_per_cat/$',views.filter_albums_per_cat),

    # urls related to search functionality
    url(r'^search/$',views.search),
    url(r'^search_album_more/(?P<page>[0-9]+)/$',views.search_album_more),
    url(r'^search_song_albums_more/(?P<page>[0-9]+)/$',views.search_song_albums_more),
    url(r'^search_producer_albums_more/(?P<page>[0-9]+)/$',views.search_producer_albums_more),

    # search utility used in the admin interface.
    url(r'^search_result_admin_internal_use/(?P<term>(.+))/$',views.search_result_admin_internal_use),



    # search utility used in the admin interface.
    url(r'^search_result_admin_internal_use/(?P<term>(.+))/$',views.search_result_admin_internal_use),


    # album activation
    url(r'^activation_request/$',views.activation_request),
    #url(r'^verify_activation_request/$',views.verify_activation_request),


]

urlpatterns = format_suffix_patterns(urlpatterns)
