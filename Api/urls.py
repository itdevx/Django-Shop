from django.urls import path
from Api import views
from rest_framework.routers import DefaultRouter



app_name = 'api'


router = DefaultRouter()

urlpatterns = [
    path('product-list', views.ProductListApi.as_view(), name='product-list-api')
]


router.register('products', views.ProductViewSet, basename='productsviewset')

urlpatterns = router.urls