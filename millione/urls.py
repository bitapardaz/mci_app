from django.conf.urls import url
import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^top_up/$',views.top_up),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
