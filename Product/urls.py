from django.urls import path
from Product.views import *

app_name = 'product'

urlpatterns = [
    path(
        '', IndexView.as_view(), name='index'
    ),
    path(
        'single-product/<slug>', SinglProductView.as_view(), name='single-product'
    ),
    path(
        'about', AboutView.as_view(), name='about'
    ),
    path(
        'contact', ContactView.as_view(), name='contact'
    ),
    path(
        'shop', ShopView.as_view(), name='shop'
    ),
    path('search', SearchView.as_view(), name='search')
]