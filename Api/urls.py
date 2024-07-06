from django.urls import path
from Api import views


app_name = 'api'


urlpatterns = [
    path('product-list', views.ProductListApi.as_view(), name='product-list-api')
]