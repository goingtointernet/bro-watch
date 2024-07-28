from django.contrib.sitemaps import Sitemap
from .models import Product, StaticPosts, NewsPosts
from django.urls import reverse


class SvgIconsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Product.objects.all()
    
class PageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return StaticPosts.objects.all()
         

class NewsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return NewsPosts.objects.all()