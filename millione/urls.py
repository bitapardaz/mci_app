from django.conf.urls import url
import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^top_up/$',views.top_up),
    url(r'^sign_up/$',views.sign_up),
    url(r'^Top_up_2/$',views.Top_up_edit.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
