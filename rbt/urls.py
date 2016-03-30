from django.conf.urls import url
import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^register/$',views.register),

    url(r'^rbt_cats/$',views.rbt_cats),
    url(r'^(?P<cat_id>[0-9]+)/(?P<page>[0-9]+)/$',views.cat_albums),
    url(r'^(?P<cat_id>[0-9]+)/popular/$',views.cat_popular_albums),
    url(r'^(?P<cat_id>[0-9]+)/new/$',views.cat_new_albums),
    url(r'^(?P<cat_id>[0-9]+)/ads/$',views.cat_adverts),

    url(r'^list/$',views.list),
    url(r'^list_cat/(?P<cat_name>[a-zA-Z]+)/(?P<page>[0-9]+)/$',views.list_cat),
    url(r'^popular_songs/(?P<page>[0-9]+)/$',views.popular_songs),
    url(r'^latest_songs/(?P<page>[0-9]+)/$',views.latest_songs),



]

urlpatterns = format_suffix_patterns(urlpatterns)
