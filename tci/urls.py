from django.conf.urls import url
from download_center import views
from rest_framework.urlpatterns import format_suffix_patterns

from tci import views

urlpatterns = [
    # URLs related to homepage
    url(r'^get_bill_info_single_number/$',views.get_bill_info_single_number),
    url(r'^pay_one_bill/$',views.pay_one_bill),
    url(r'^test_header/$',views.test_header),
]

urlpatterns = format_suffix_patterns(urlpatterns)
