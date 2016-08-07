from django.conf.urls import url
from download_center import views
from rest_framework.urlpatterns import format_suffix_patterns

from tci import views
from tci_userprofile import views as user_profile_views

urlpatterns = [

    # urls related to website
    url(r'^web_homepage/$',views.web_homepage),
    url(r'^kitchen/$',views.kitchen),
    url(r'^my_bill/$',views.my_bill),

    # URLs related to homepage
    url(r'^get_bill_info_single_number/$',views.get_bill_info_single_number),
    url(r'^pay_one_bill/$',views.pay_one_bill),

    # user registration
    url(r'^register/$',user_profile_views.register),
    url(r'^registeration_verfication/$',user_profile_views.registeration_verification),


]

urlpatterns = format_suffix_patterns(urlpatterns)
