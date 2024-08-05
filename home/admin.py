from django.contrib import admin

from .models import StaticPosts,NewsPosts,OemCustom, OemCustomBox, AddFaq,OemOdm, Oem, Faqs ,Certificate,WhatWeDo,WhatWeDoBox, HomePartners, HomePartnerImage,  SiteData, WhatGain, Ads,ProductShowImages,HomeAboutSection, Product,ProductImages , Faqs,HomeBannerImages, Category, HomeGroups
from parler.admin import TranslatableAdmin
# Register static data
admin.site.register(SiteData, TranslatableAdmin)
# Register static post
admin.site.register(StaticPosts, TranslatableAdmin)
# Register News post
admin.site.register(NewsPosts, TranslatableAdmin)
# HomeAboutSection
admin.site.register(HomeAboutSection, TranslatableAdmin)
# Ads
admin.site.register(Ads)
#SVG
admin.site.register(Product, TranslatableAdmin)
#Faqs
# admin.site.register(Faqs)
#Category
admin.site.register(Category, TranslatableAdmin)
#HomeGroups
# admin.site.register(HomeGroups)
#BannerImages
admin.site.register(HomeBannerImages)
#ProductImages
admin.site.register(ProductImages)
#ProductShowImages
admin.site.register(ProductShowImages)
#WhatGain
admin.site.register(WhatGain, TranslatableAdmin)
#Certificate
admin.site.register(Certificate)
#WhatWeDo
admin.site.register(WhatWeDo, TranslatableAdmin)
admin.site.register(WhatWeDoBox, TranslatableAdmin)


class HomePartnerImageInline(admin.TabularInline):
    model = HomePartnerImage
    extra = 1

class HomePartnersAdmin(TranslatableAdmin, admin.ModelAdmin):
    inlines = [HomePartnerImageInline]

admin.site.register(HomePartners, HomePartnersAdmin)


class FaqsInline(admin.TabularInline):
    model = Faqs
    extra = 1

class AddFaqAdmin(TranslatableAdmin, admin.ModelAdmin):
    inlines = [FaqsInline]

admin.site.register(AddFaq, AddFaqAdmin)


class OemInline(admin.TabularInline):
    model = Oem
    extra = 1

class OemOdmAdmin(TranslatableAdmin, admin.ModelAdmin):
    inlines = [OemInline]

admin.site.register(OemOdm, OemOdmAdmin)


class OemCustomBoxInline(admin.TabularInline):
    model = OemCustomBox
    extra = 1

class OemCustomAdmin(TranslatableAdmin, admin.ModelAdmin):
    inlines = [OemCustomBoxInline]

admin.site.register(OemCustom, OemCustomAdmin)