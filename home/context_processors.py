from django.conf import settings
from .models import StaticPosts,SiteData, Ads, Category, Product

#Static-Page-Post
def pages(request):
    pages = StaticPosts.objects.all()
    return {"pages": pages}

#Site Data
def sitedata(request):
    sitedata = SiteData.objects.all().first()
    return {"sitedata": sitedata}

#Ads Data
def ads(request):
    ads = Ads.objects.all().first()
    return {"ads": ads}

#Category Data
def category(request):
    category = Category.objects.all()
    return {"category": category}

#Recent Data
def recent(request):
    recentProduct = Product.objects.all().order_by("-pk")
    return {"recentProduct": recentProduct}