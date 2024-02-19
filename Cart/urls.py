from django.urls import path
from Cart.views import *

app_name = 'cart'

urlpatterns = [
    path(
        'cart', CartView.as_view(), name='cart'
    ),
    path(
        'checkout', CheckoutView.as_view(), name='checkout'
    ),
    path(
        'cart_add', cart_add, name='cart_add'
    )
]