from django.conf.urls import url
from download_center import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # URLs related to homepage
    url(r'^homepage/$',views.homepage),

]

urlpatterns = format_suffix_patterns(urlpatterns)
