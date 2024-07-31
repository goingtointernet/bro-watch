from django.db import models
from django.urls import reverse

# Banner Image
class HomeBannerImages(models.Model):
    image = models.ImageField( upload_to = 'Banner', null = True, blank = True)
    
# ProductImages
class ProductImages(models.Model):
    image = models.ImageField( upload_to = 'Product', null = True, blank = True)

# ProductShowImages
class ProductShowImages(models.Model):
    image = models.ImageField( upload_to = 'Product', null = True, blank = True)

# Category
class Category(models.Model):
    name = models.CharField(max_length=160, unique= True)
    category_box_image = models.ImageField( upload_to = 'category', null = True, blank = True)
    category_banner_img = models.ImageField( upload_to = 'category', null = True, blank = True)
    def __str__(self):
        return self.name
    

# WhatGain
class WhatGain(models.Model):
    title = models.CharField(max_length=160, unique= True)
    paragraph = models.CharField(max_length=260)
    image = models.ImageField( upload_to = 'WhatGain', null = True, blank = True)
    def __str__(self):
        return self.title
    
# Certificate 
class Certificate(models.Model):
    certificate_image = models.ImageField( upload_to = 'Certificate')

# What we do 
class WhatWeDo(models.Model):
    title = models.CharField(max_length=160, unique= True)
    paragraph = models.CharField(max_length=260)
    banner_image = models.ImageField( upload_to = 'WhatWeDo')

#Faqs
class AddFaq(models.Model):
    heading = models.CharField(max_length=160)

    def __str__(self):
        return self.heading

class Faqs(models.Model):
    question = models.CharField(max_length=260)
    answer = models.TextField()
    heading = models.ForeignKey(AddFaq, related_name='faqs', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.question

# SVG Details.
class Product(models.Model):
    title = models.CharField(max_length=160)
    meta_desc = models.CharField(max_length=160)
    meta_key = models.CharField(max_length=260)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    product_images = models.ManyToManyField(ProductImages, blank=False)
    brand = models.CharField(max_length=160, default="")
    model = models.CharField(max_length=160, default="")
    weight = models.CharField(max_length=160, default="")
    waterproof = models.CharField(max_length=160, default="")
    feature = models.CharField(max_length=160, default="")
    details = models.TextField()
    price = models.CharField(max_length=160, default="")
    product_show_images = models.ManyToManyField(ProductShowImages, blank=False)
    # faqs_content = models.ManyToManyField(Faqs, blank=True)
    slug = models.CharField(max_length=70, unique=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("svg_icon_detail",args=[self.slug])

# Static-Pages.
class StaticPosts(models.Model):
    title = models.CharField(max_length=160)
    meta_desc = models.CharField(max_length=160)
    meta_key = models.CharField(max_length=260)
    page_name = models.CharField(max_length=70)
    content = models.TextField()
    slug = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("staticpost",args=[self.slug])
    

# Static-Pages.
class NewsPosts(models.Model):
    banner_image = models.ImageField( upload_to = 'news', null=True)
    title = models.CharField(max_length=160)
    meta_desc = models.CharField(max_length=160)
    meta_key = models.CharField(max_length=260)
    content = models.TextField()
    slug = models.CharField(max_length=70, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("newspost",args=[self.slug])
    


# Site-Data.
class SiteData(models.Model):
    title = models.CharField(max_length=160, default="")
    meta_desc = models.CharField(max_length=160,default="")
    meta_key = models.CharField(max_length=260, default="")
    logo = models.ImageField( upload_to = 'logo', null = True, blank = True)
    white_text_logo = models.ImageField( upload_to = 'logo', null = True, blank = True)
    fav_icon = models.ImageField( upload_to = 'logo', null = True, blank = True)
    email = models.CharField(max_length=160, default="")
    phone = models.CharField(max_length=160, default="")
    whatsapp_link = models.CharField(max_length=160, default="")
    address = models.CharField(max_length=260, default="")
    facebook = models.CharField(max_length=160,  default="", blank=True, null=True)
    instagram = models.CharField(max_length=160,  default="", blank=True, null=True)
    twitter = models.CharField(max_length=160,default="", blank=True, null=True)
    author = models.CharField(max_length=160,default="", blank=True, null=True)
    site_name = models.CharField(max_length=160,default="")
    site_url = models.CharField(max_length=160,default="")
    made_by = models.CharField(max_length=160,default="")
    copyright = models.CharField(max_length=160,default="")
    sidebar_contact_banner = models.ImageField( upload_to = 'Contact', null = True, blank = True)
    search_key = models.CharField(max_length=160, default="")
    search_desc = models.CharField(max_length=160, default="")
    custome_css = models.TextField(default="", blank=True, null=True)
    head_script = models.TextField(default="", blank=True, null=True)
    bodyend_script = models.TextField(default="", blank=True, null=True)
    show_ads= models.BooleanField('show all ad', default=False)

#Home About.
class HomeAboutSection(models.Model):
    heading = models.CharField(max_length=260, default="")
    paragrph = models.TextField( default="")
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    def __str__(self):
        return self.heading
    

class WhatWeDoBox(models.Model):
    img = models.ImageField( upload_to = 'whatwedo', null = True, blank = True)
    heading = models.CharField(max_length=260, default="")
    paragrph = models.TextField( default="")
    def __str__(self):
        return self.heading

#Ads
class Ads(models.Model):
    head_ad = models.TextField(default="")
    footer_ad = models.TextField(default="")



#Home Groups
class HomeGroups(models.Model):
    heading =  models.CharField(max_length=260,  default="", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    slug = models.CharField(max_length=70, unique=True, default="")
    def __str__(self):
        return self.heading
    
#home partners
class HomePartners(models.Model):
    heading =  models.CharField(max_length=260,  default="Contact Us", blank=True, null=True)
    BackgroundImg = models.ImageField( upload_to = 'partners', null = True, blank = True)
    paragraph =  models.TextField( default="")
    def __str__(self):
        return self.heading
    
class HomePartnerImage(models.Model):
    home_partner = models.ForeignKey(HomePartners, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='home_partner_images')
    
    def __str__(self):
        return f"Image for {self.home_partner.heading}"