from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import HomeBannerImages,OemCustom, NewsPosts,AddFaq,OemOdm, HomeAboutSection,HomePartners, WhatWeDoBox, Product, StaticPosts,Certificate ,WhatWeDo , HomeGroups, Category, WhatGain
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import Paginator
from django.conf import settings

# Index
def index(request):
    home_groups = HomeGroups.objects.all()
    recent = Product.objects.all().order_by('-pk')
    news = NewsPosts.objects.all().order_by('-pk')
    category = Category.objects.all().order_by('-pk')
    whatgain = WhatGain.objects.all()
    certificate = Certificate.objects.all()
    whatwedo = WhatWeDo.objects.all().first()
    whatwedobox = WhatWeDoBox.objects.all().order_by("-pk")
    banner = HomeBannerImages.objects.all().order_by("-pk")
    homeabout = HomeAboutSection.objects.all().first()
    home_partner = HomePartners.objects.first()
    
    
    
    
    grouped_products = []
    for group in home_groups:
        products = Product.objects.filter(category=group.category)
        grouped_products.append({'group': group, 'products': products})
    
    context = {'grouped_products': grouped_products, 'news':news, 'home_partner':home_partner, 'banner':banner, 'whatwedobox':whatwedobox, 'homeabout':homeabout, 'category':category, 'recent':recent, 'whatgain':whatgain,'whatwedo':whatwedo, 'certificate':certificate}
    return render(request, 'home/index.html', context)


def faqs(request):
    faqs = AddFaq.objects.all().order_by('-pk')
    return render(request, 'home/faqs.html', {'faqs':faqs})


def oemodm(request):
    oemodm = OemOdm.objects.all().first()
    oemcutome = OemCustom.objects.all().first()
    return render(request, 'home/oem-odm.html', {'oemodm':oemodm, 'oemcutome':oemcutome})

#Product
def svg_icon_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }
    return render(request, 'home/product.html', context)

def all_category(request):
    all_category = Category.objects.all().order_by('-pk')
    print(all_category)
    context = {'all_category': all_category}
    return render(request, 'home/all-category.html', context)

#404
def error_404_view(request, exception):
    return render(request, '404.html')
#400
def error_400_view(request, exception):
    return render(request, '400.html')
#401
def error_401_view(request, exception):
    return render(request, '401.html')
#403
def error_403_view(request, exception):
    return render(request, '403.html')
#500
def error_500_view(request, exception=None):
    return render(request, '500.html')


#Search
def search(request):
    search=request.GET['search']
    
    if len(search)>78:
        product_data = []
    else:    
        product_title = Product.objects.filter(title__icontains=search)
        product_slug = Product.objects.filter(slug__icontains=search)
        product_meta_key = Product.objects.filter(meta_key__icontains=search)
        product_category = Product.objects.filter(category__name__icontains=search)
        p =  Paginator(product_title.union(product_slug).union(product_meta_key).union(product_category).order_by('-pk'), 15)
        page = request.GET.get('page')
        pagination = p.get_page(page)
        product_data=pagination
        current_numer = pagination.number
        total_number = pagination.paginator.num_pages
        if current_numer == total_number and current_numer != 0:
            current_numer = current_numer - 1
        if total_number == 1:
             page_range = 1
        else:
            page_range =(current_numer, total_number)


    params={'products':  product_data, 'pagination':pagination, 'search':search, 'page_range':page_range}
    return render(request, 'home/search.html', params)


#News
def news(request):
    p =  Paginator(NewsPosts.objects.all().order_by('-pk'), 12)
    page = request.GET.get('page')
    pagination = p.get_page(page)
    product_data=pagination
    current_numer = pagination.number
    total_number = pagination.paginator.num_pages
    if current_numer == total_number and current_numer != 0:
        current_numer = current_numer - 1
    if total_number == 1:
        page_range = 1
    else:
        page_range =(current_numer, total_number)


    params={'news':  product_data, 'pagination':pagination, 'page_range':page_range}
    return render(request, 'home/all-news.html', params)

#Static-post
def staticpost(request,slug):
    staticpost = get_object_or_404(StaticPosts, slug=slug)
    allpost = StaticPosts.objects.all()
    
    context = {'allpost': allpost,'staticpost':staticpost}
    return render(request, 'home/static-post.html', context)


def newspost(request,slug):
    staticpost = get_object_or_404(NewsPosts, slug=slug)
    allpost = NewsPosts.objects.all()
    
    context = {'allpost': allpost,'staticpost':staticpost}
    return render(request, 'home/news-post.html', context)


def category_detail(request, category):
    try:
        categoryObj =  Category.objects.filter(id=category).first()
        categoryName = categoryObj.name
        p = Paginator(Product.objects.filter(category=category).order_by('-pk'), 15)
        page = request.GET.get('page')
        pagination = p.get_page(page)
        product_data=pagination
        current_numer = pagination.number
        total_number = pagination.paginator.num_pages
        if current_numer == total_number and current_numer != 0:
            current_numer = current_numer - 1
        if total_number == 1:
            page_range = 1
        else:
            page_range =(current_numer, total_number)

        params={'products':  product_data, 'pagination':pagination, 'page_range':page_range, "categoryName":categoryName, "categoryObj":categoryObj}
        return render(request, 'home/category-product.html', params)
    except Exception as e:
        print("error", e)
        return render(request, '404.html')
    

#==Contact-Page==========================#
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        data = {
            'name':name,
            'email':email,
            'phone':phone,
            'message':message,
        }
        message = '''
        Client Name: {}
        Client Email: {}
        Client Phone Number: {}
        Client Message:{}
        '''.format(data['name'], data['email'], data['phone'], data['message'])
        send_mail("Inquiry Message - Contact", message, '',[settings.EMAIL_HOST_USER], fail_silently=False,)
        messages.success(request, '*Sent Successfully')
    return render(request, 'home/contact.html')