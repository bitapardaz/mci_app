from django.conf.urls import url
from download_center import views
from rest_framework.urlpatterns import format_suffix_patterns

import views


urlpatterns = [

    # urls related to website
    url(r'^pfm_download/$',views.pfm_download),
    url(r'^download_page/$',views.download_page),
]

urlpatterns = format_suffix_patterns(urlpatterns)
