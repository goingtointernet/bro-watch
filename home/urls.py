from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contact-us/',views.contact, name='contact'),
    path('news/',views.news, name='news'),
    path('faqs/',views.faqs, name='faqs'),
    path('about-us/',views.aboutus, name='aboutus'),
    path('all-products/',views.allproducts, name='allproducts'),
    path('oemodm/',views.oemodm, name='oemodm'),
    path('product/<slug:slug>', views.svg_icon_detail, name='svg_icon_detail'),
    path('<str:slug>',views.staticpost, name='staticpost'),
    path('news/<str:slug>',views.newspost, name='newspost'),
    path('icons/search',views.search, name='search'),
    path('<str:category>/', views.category_detail, name='category_detail'),
    path('category/all/', views.all_category, name='all_category'),
]