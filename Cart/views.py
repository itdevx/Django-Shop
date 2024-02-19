from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from Cart.cart import Cart
from Product.models import Product
from django.http import JsonResponse



class CartView(View):
    template_name = 'cart.html'

    def get(self, request):
        return render(request, self.template_name)
    

def cart_add(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, request=request)
        cart_quantity = cart.__len__()
        res = JsonResponse({'qty': cart_quantity})

        return res
    

    
class CheckoutView(View):
    template_name = 'checkout.html'

    def get(self, request):
        return render(request, self.template_name)
    
    