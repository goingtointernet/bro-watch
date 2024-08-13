from django.contrib import admin

from .models import StaticPosts,NewsPosts,SocialIcons, NavMenu, OemCustom, OemCustomBox, AddFaq,OemOdm, Oem, Faqs ,Certificate,WhatWeDo,WhatWeDoBox, HomePartners, HomePartnerImage,  SiteData, WhatGain, Ads,ProductShowImages,HomeAboutSection, Product,ProductImages , Faqs,HomeBannerImages, Category, HomeGroups
# Register static data
admin.site.register(SiteData)
# Register static post
admin.site.register(StaticPosts)
# Register News post
admin.site.register(NewsPosts)
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
#Category
admin.site.register(SocialIcons)
#Category
admin.site.register(NavMenu)
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
admin.site.register(WhatWeDoBox)


class HomePartnerImageInline(admin.TabularInline):
    model = HomePartnerImage
    extra = 1

class HomePartnersAdmin(admin.ModelAdmin):
    inlines = [HomePartnerImageInline]

admin.site.register(HomePartners, HomePartnersAdmin)


class FaqsInline(admin.TabularInline):
    model = Faqs
    extra = 1

class AddFaqAdmin(admin.ModelAdmin):
    inlines = [FaqsInline]

admin.site.register(AddFaq, AddFaqAdmin)


class OemInline(admin.TabularInline):
    model = Oem
    extra = 1

class OemOdmAdmin(admin.ModelAdmin):
    inlines = [OemInline]

admin.site.register(OemOdm, OemOdmAdmin)


class OemCustomBoxInline(admin.TabularInline):
    model = OemCustomBox
    extra = 1

class OemCustomAdmin(admin.ModelAdmin):
    inlines = [OemCustomBoxInline]

admin.site.register(OemCustom, OemCustomAdmin)