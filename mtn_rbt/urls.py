from django.conf.urls import url
from mtn_rbt import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^register/$',views.register),


]

urlpatterns = format_suffix_patterns(urlpatterns)
