from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contact-us/',views.contact, name='contact'),
    path('product/<slug:slug>', views.svg_icon_detail, name='svg_icon_detail'),
    path('<str:slug>',views.staticpost, name='staticpost'),
    path('icons/search',views.search, name='search'),
    path('<str:category>/', views.category_detail, name='category_detail'),
    path('category/all/', views.all_category, name='all_category'),
]