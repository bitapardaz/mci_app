from django.conf.urls import url
import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^list/$',views.list),
    url(r'^list_cat/(?P<cat_name>[a-zA-Z]+)/(?P<page>[0-9]+)/$',views.list_cat),
]

urlpatterns = format_suffix_patterns(urlpatterns)
