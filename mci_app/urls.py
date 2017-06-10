"""mci_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from website import views as website_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mcirbt/',include('rbt.urls')),
    url(r'^mtnrbt/',include('mtn_rbt.urls')),
    url(r'^tci/',include('tci.urls')),
    url(r'^download_center/',include('download_center.urls')),
    url(r'^google450805d50c86330d.html$', website_views.google_index ),
    url(r'^pfm_promotion/',include('pfm_promotion.urls')),
    url(r'^millione/',include('millione.urls')),
    url(r'^$',website_views.homepage),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
