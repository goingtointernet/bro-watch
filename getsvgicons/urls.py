"""
URL configuration for getsvgicons project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url
from django.views.static import serve
from django.views.generic.base import TemplateView 
from home.sitemap import SvgIconsSitemap, PageSitemap, NewsSitemap

sitemaps = {
    'product': SvgIconsSitemap,
    'pages': PageSitemap,
    'news': NewsSitemap,
}

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path("robots.txt",TemplateView.as_view(template_name="seo/robots.txt", content_type="text/plain")),  #add the robots.txt file
    path("ads.txt",TemplateView.as_view(template_name="seo/ads.txt", content_type="text/plain")),  #add the ads.txt file
    path('', include('home.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404= 'home.views.error_404_view'
handler400= 'home.views.error_400_view'
handler401= 'home.views.error_401_view'
handler403= 'home.views.error_403_view'
handler500= 'home.views.error_500_view'