from django.contrib import admin
from django_summernote.widgets import SummernoteWidget 
from django.db import models 
from .forms import ProductAdminForm
from .models import StaticPosts,NewsPosts,SocialIcons, NavMenu,AboutPage, CustomerBox, OemCustom, OemCustomBox, AddFaq,OemOdm, Oem, Faqs ,Certificate,WhatWeDo,WhatWeDoBox, HomePartners, HomePartnerImage,  SiteData, WhatGain, Ads,ProductShowImages,HomeAboutSection, Product,ProductImages , Faqs,HomeBannerImages, Category, HomeGroups
# Register static data
admin.site.register(SiteData)
# Register static post
# admin.site.register(StaticPosts)
class StaticPostsAdmin(admin.ModelAdmin): 

     formfield_overrides = { 
            models.TextField: {'widget': SummernoteWidget}, 
     } 

admin.site.register(StaticPosts,StaticPostsAdmin)
# Register News post
# admin.site.register(NewsPosts)

class NewsPostAdmin(admin.ModelAdmin): 

     formfield_overrides = { 
            models.TextField: {'widget': SummernoteWidget}, 
     } 

admin.site.register(NewsPosts,NewsPostAdmin)

# HomeAboutSection
admin.site.register(HomeAboutSection)
# Ads
admin.site.register(Ads)
#SVG
# admin.site.register(Product)
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
# admin.site.register(ProductImages)
#ProductShowImages
# admin.site.register(ProductShowImages)
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
    formfield_overrides = { 
            models.TextField: {'widget': SummernoteWidget}, 
     } 

class OemOdmAdmin(admin.ModelAdmin):
    inlines = [OemInline]

admin.site.register(OemOdm, OemOdmAdmin)



class OemCustomBoxInline(admin.TabularInline):
    model = OemCustomBox
    extra = 1

class OemCustomAdmin(admin.ModelAdmin):
    inlines = [OemCustomBoxInline]

admin.site.register(OemCustom, OemCustomAdmin)



class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 1

class ProductShowImagesInline(admin.TabularInline):
    model = ProductShowImages
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline, ProductShowImagesInline]
    form = ProductAdminForm
    list_display = ['title', 'category', 'brand', 'price']
    search_fields = ['title', 'brand', 'model']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Handle ProductImages
        images = form.cleaned_data.get('images')
        if images:
            for image in images:
                ProductImages.objects.create(heading=obj, image=image)

        # Handle ProductShowImages
        show_images = form.cleaned_data.get('show_images')
        if show_images:
            for image in show_images:
                ProductShowImages.objects.create(heading=obj, image=image)

admin.site.register(Product, ProductAdmin)



class AboutPageInline(admin.TabularInline):
    model = CustomerBox
    extra = 1
    formfield_overrides = { 
            models.TextField: {'widget': SummernoteWidget}, 
     } 

class CustomerBoxAdmin(admin.ModelAdmin):
    inlines = [AboutPageInline]
    formfield_overrides = { 
            models.TextField: {'widget': SummernoteWidget}, 
     } 

admin.site.register(AboutPage, CustomerBoxAdmin)