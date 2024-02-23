from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from Cart.cart import Cart
from Product.models import Product
from django.http import JsonResponse
from Cart.models import Cart as C


class CartView(View):
    template_name = 'cart.html'

    def get(self, request):
        cart = Cart(request)
        cart_products = cart.get_products()
        context = {
            'cart_products': cart_products
        }
        return render(request, self.template_name, context)
    

def cart_add(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, request=request)
        cart_quantity = cart.__len__()
        res = JsonResponse({'qty': cart_quantity})
        return res
    


def add_to_cart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            p_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=p_id)
            if product_check:
                if not C.objects.filter(user=request.user, product_id=p_id):
                    product_qyt = 1
                    C.objects.create(user=request.user, product_id=p_id, quantity=product_qyt)
                    return JsonResponse({'status': 'Product added successfuly'})
                else:
                    return JsonResponse({'status': 'Product is Already in Cart'})
            else:
                return JsonResponse({'status': 'No such Product found'})

        else:
            return JsonResponse({'status': 'Login to continue'})



class CheckoutView(View):
    template_name = 'checkout.html'

    def get(self, request):
        return render(request, self.template_name)
    
    