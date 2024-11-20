from django.urls import path
from Api import views
from rest_framework.routers import DefaultRouter



app_name = 'api'


router = DefaultRouter()
    
# urlpatterns = [
#     path('product-list', views.ProductListApi.as_view(), name='product-list-api'),

# ]

router.register('products', views.ProductViewSet, basename='productsviewset')
router.register('create-category', views.CategoryViewSet, basename='create-category')
router.register('carts', views.CartViewSet, basename='carts')
router.register('cart-item', views.CartItemViewSet, basename='cart-item')
urlpatterns = router.urls