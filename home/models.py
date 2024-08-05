from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

# Banner Image
class HomeBannerImages(models.Model):
    image = models.ImageField(_('image'), upload_to = 'Banner', null = True, blank = True)
    
# ProductImages
class ProductImages(models.Model):
    image = models.ImageField(_('image'), upload_to = 'Product', null = True, blank = True)

# ProductShowImages
class ProductShowImages(models.Model):
    image = models.ImageField(_('image'), upload_to = 'Product', null = True, blank = True)

# Category
class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('name'), max_length=160, unique=True),
        category_box_image = models.ImageField(_('category_box_image'), upload_to = 'category', null = True, blank = True),
        category_banner_img = models.ImageField(_('category_banner_img'), upload_to = 'category', null = True, blank = True),
    )
    def __str__(self):
        return self.name
    

# WhatGain
class WhatGain(TranslatableModel):
    translations = TranslatedFields(
    title = models.CharField(_('title'), max_length=160, unique= True),
    paragraph = models.CharField(_('paragraph'), max_length=260),
    )
    image = models.ImageField(_('image'), upload_to = 'WhatGain', null = True, blank = True)
    def __str__(self):
        return self.title
    
# Certificate 
class Certificate(models.Model):
    certificate_image = models.ImageField(_('certificate_image'), upload_to = 'Certificate')

# What we do 
class WhatWeDo(TranslatableModel):
    translations = TranslatedFields(
    title = models.CharField(_('title'),max_length=160, unique= True),
    paragraph = models.CharField(_('paragraph'),max_length=260),
    )
    banner_image = models.ImageField(_('banner_image'), upload_to = 'WhatWeDo')

#Faqs
class AddFaq(TranslatableModel):
    translations = TranslatedFields(
    heading = models.CharField(_('heading'),max_length=160)
    )
    def __str__(self):
        return self.heading

class Faqs(TranslatableModel):
    translations = TranslatedFields(
    question = models.CharField(_('question'),max_length=260),
    answer = models.TextField(_('answer'),),
    )
    heading = models.ForeignKey(AddFaq, related_name='faqs', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.question
    


#OEM/ODM
class OemOdm(TranslatableModel):
    banner_image = models.ImageField(_('banner_image'), upload_to = 'oemodm', null=True)
    translations = TranslatedFields(
    heading = models.CharField(_('heading'),max_length=160),
    paragraph = models.TextField(_('paragraph'),),
    )

    def __str__(self):
        return self.heading

class Oem(TranslatableModel):
    translations = TranslatedFields(
    heading = models.CharField(_('heading'),max_length=260),
    text = models.TextField(_('text'),),
    )
    image = models.ImageField(_('image'), upload_to = 'oemodm', null=True)
    main_heading = models.ForeignKey(OemOdm, related_name='oemodm', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.heading
    

class OemCustom(TranslatableModel):
    banner_image = models.ImageField(_('banner_image'), upload_to = 'oemodm', null=True)
    translations = TranslatedFields(
        heading = models.CharField(_('heading'),max_length=160),
    )

    def __str__(self):
        return self.heading

class OemCustomBox(TranslatableModel):
    translations = TranslatedFields(
    heading = models.CharField(_('heading'),max_length=260),
    text = models.TextField(_('text'),),
    )
    image = models.ImageField(_('image'), upload_to = 'oemodm', null=True)
    main_heading = models.ForeignKey(OemCustom, related_name='oemcustombox', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.heading

# SVG Details.
class Product(TranslatableModel):
    category = models.ForeignKey(Category, verbose_name=_('category'), on_delete=models.CASCADE, null=True),
    product_images = models.ManyToManyField(ProductImages, verbose_name=_('product_images'), blank=False),
    product_show_images = models.ManyToManyField(ProductShowImages, verbose_name=_('product_show_images'), blank=False),
    translations = TranslatedFields(
    title = models.CharField(_('title'),max_length=160),
    meta_desc = models.CharField(_('meta_desc'),max_length=160),
    meta_key = models.CharField(_('meta_key'),max_length=260),
    brand = models.CharField(_('brand'),max_length=160, default=""),
    model = models.CharField(_('model'),max_length=160, default=""),
    weight = models.CharField(_('weight'),max_length=160, default=""),
    waterproof = models.CharField(_('waterproof'),max_length=160, default=""),
    feature = models.CharField(_('feature'),max_length=160, default=""),
    details = models.TextField(_('details'),),
    price = models.CharField(_('price'), max_length=160, default=""),
    )
    # faqs_content = models.ManyToManyField(Faqs, blank=True)
    slug = models.CharField(_('slug'), max_length=70, unique=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("svg_icon_detail",args=[self.slug])

# Static-Pages.
class StaticPosts(TranslatableModel):
    translations = TranslatedFields(
    title = models.CharField(_('title'),max_length=160),
    meta_desc = models.CharField(_('meta_desc'),max_length=160),
    meta_key = models.CharField(_('meta_key'),max_length=260),
    page_name = models.CharField(_('page_name'),max_length=70),
    content = models.TextField(_('content'),),
    )
    slug = models.CharField(_('slug'),max_length=70, unique=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("staticpost",args=[self.slug])
    

# Static-Pages.
class NewsPosts(TranslatableModel):
    banner_image = models.ImageField(_('banner_image'), upload_to = 'news', null=True)
    translations = TranslatedFields(
    title = models.CharField(_('title'),max_length=160),
    meta_desc = models.CharField(_('meta_desc'),max_length=160),
    meta_key = models.CharField(_('meta_key'),max_length=260),
    content = models.TextField(_('content'),),
    )
    slug = models.CharField(_('slug'), max_length=70, unique=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("newspost",args=[self.slug])
    


# Site-Data.
class SiteData(TranslatableModel):
    logo = models.ImageField(_('logo'), upload_to = 'logo', null = True, blank = True)
    white_text_logo = models.ImageField(_('white_text_logo'), upload_to = 'logo', null = True, blank = True)
    fav_icon = models.ImageField(_('fav_icon'), upload_to = 'logo', null = True, blank = True)
    sidebar_contact_banner = models.ImageField(_('sidebar_contact_banner'), upload_to = 'Contact', null = True, blank = True)
    translations = TranslatedFields(
    title = models.CharField(_('title'), max_length=160, default=""),
    meta_desc = models.CharField(_('meta_desc'), max_length=160,default=""),
    meta_key = models.CharField(_('meta_key'),max_length=260, default=""),
    email = models.CharField(_('email'),max_length=160, default=""),
    phone = models.CharField(_('phone'),max_length=160, default=""),
    whatsapp_link = models.CharField(_('whatsapp_link'),max_length=160, default=""),
    address = models.CharField(_('address'),max_length=260, default=""),
    facebook = models.CharField(_('facebook'),max_length=160,  default="", blank=True, null=True),
    instagram = models.CharField(_('instagram'),max_length=160,  default="", blank=True, null=True),
    twitter = models.CharField(_('twitter'),max_length=160,default="", blank=True, null=True),
    author = models.CharField(_('author'),max_length=160,default="", blank=True, null=True),
    site_name = models.CharField(_('site_name'),max_length=160,default=""),
    site_url = models.CharField(_('site_url'),max_length=160,default=""),
    made_by = models.CharField(_('made_by'),max_length=160,default=""),
    copyright = models.CharField(_('copyright'),max_length=160,default=""),
    search_key = models.CharField(_('search_key'),max_length=160, default=""),
    search_desc = models.CharField(_('search_desc'),max_length=160, default=""),
    custome_css = models.TextField(_('custome_css'),default="", blank=True, null=True),
    head_script = models.TextField(_('head_script'),default="", blank=True, null=True),
    bodyend_script = models.TextField(_('bodyend_script'),default="", blank=True, null=True),
    show_ads= models.BooleanField(_('show_ads'),'show all ad', default=False),
    )

#Home About.
class HomeAboutSection(TranslatableModel):
    translations = TranslatedFields(
    heading = models.CharField(_('heading'), max_length=260, default=""),
    paragrph = models.TextField(_('paragrph'), default=""),)
    video_file = models.FileField(_('video_file'), upload_to='videos/', blank=True, null=True)
    def __str__(self):
        return self.heading
    

class WhatWeDoBox(TranslatableModel):
    img = models.ImageField( _('img'),upload_to = 'whatwedo', null = True, blank = True)
    translations = TranslatedFields(
    heading = models.CharField(_('heading'),max_length=260, default=""),
    paragrph = models.TextField(_('paragrph'), default=""),
    )
    def __str__(self):
        return self.heading

#Ads
class Ads(models.Model):
    head_ad = models.TextField(_('head_ad'),default="")
    footer_ad = models.TextField(_('footer_ad'),default="")



#Home Groups
class HomeGroups(TranslatableModel):
    translations = TranslatedFields(
    heading =  models.CharField(_('heading'),max_length=260,  default="", blank=True, null=True)
    )
    category = models.ForeignKey(Category, verbose_name=_('category'), on_delete=models.CASCADE, null=True)
    slug = models.CharField(_('slug'),max_length=70, unique=True, default="")
    def __str__(self):
        return self.heading
    
#home partners
class HomePartners(TranslatableModel):
    translations = TranslatedFields(
    heading =  models.CharField(_('heading'),max_length=260,  default="Contact Us", blank=True, null=True),
    paragraph =  models.TextField(_('paragraph'), default=""),
    )
    BackgroundImg = models.ImageField(_('BackgroundImg'), upload_to = 'partners', null = True, blank = True)
    def __str__(self):
        return self.heading
    
class HomePartnerImage(models.Model):
    home_partner = models.ForeignKey(HomePartners, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(_('image'), upload_to='home_partner_images')
    
    def __str__(self):
        return f"Image for {self.home_partner.heading}"