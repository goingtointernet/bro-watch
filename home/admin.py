from django.contrib import admin

from .models import StaticPosts,Certificate,WhatWeDo,  SiteData, WhatGain, Ads,ProductShowImages,HomeAboutSection, Product,ProductImages , Faqs,HomeBannerImages, Category, HomeGroups
# Register static data
admin.site.register(SiteData)
# Register static post
admin.site.register(StaticPosts)
# HomeAboutSection
admin.site.register(HomeAboutSection)
# Ads
admin.site.register(Ads)
#SVG
admin.site.register(Product)
#Faqs
# admin.site.register(Faqs)
#Category
admin.site.register(Category)
#HomeGroups
# admin.site.register(HomeGroups)
#BannerImages
admin.site.register(HomeBannerImages)
#ProductImages
admin.site.register(ProductImages)
#ProductShowImages
admin.site.register(ProductShowImages)
#WhatGain
admin.site.register(WhatGain)
#Certificate
admin.site.register(Certificate)
#WhatWeDo
admin.site.register(WhatWeDo)