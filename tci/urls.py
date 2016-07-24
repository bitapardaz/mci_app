from django.conf.urls import url
from download_center import views
from rest_framework.urlpatterns import format_suffix_patterns

import views

urlpatterns = [
    # URLs related to homepage
    url(r'^get_bill_info_single_number/$',views.get_bill_info_single_number),
    url(r'^pay_one_bill/$',views.pay_one_bill),


]

urlpatterns = format_suffix_patterns(urlpatterns)
