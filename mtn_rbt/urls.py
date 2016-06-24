from django.conf.urls import url
from mtn_rbt import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^register/$',views.register),

    # URLs related to homepage
    url(r'^homepage/$',views.homepage),

    # URLs related to each category
    url(r'^0/homepage/$',views.homepage),
    url(r'^(?P<cat_id>[0-9]+)/homepage/$',views.cat_homepage),

    


]

urlpatterns = format_suffix_patterns(urlpatterns)
