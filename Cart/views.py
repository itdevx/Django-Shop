from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from Cart.cart import Cart
from Product.models import Product
from django.http import JsonResponse
from Cart.models import Cart as C
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin


class CartView(LoginRequiredMixin, View):
    template_name = 'cart.html'
    login_url = 'account:sign-in'

    def get(self, request):
        # cart = Cart(request)
        # cart_products = cart.get_products()
        cart_items = C.objects.filter(user=request.user).all()
        total_price = 0
        if cart_items:
            for item in cart_items:
                total_price += item.product.price

        context = {
            # 'cart_products': cart_products,
            'qty': C.objects.filter(user=request.user).count(),
            'cart_items': cart_items,
            'total_price': total_price,
        }

        return render(request, self.template_name, context)
    

# session
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
    if request.user.is_authenticated:
        if request.method == 'POST':
            p_id = request.POST.get('product_id')
            product_check = Product.objects.get(id=p_id)
            if product_check:
                if C.objects.filter(user=request.user, product_id=p_id):
                    return JsonResponse({'status': 'Product is Already in Cart'})
                else:
                    product_qyt = 1
                    C.objects.create(user=request.user, product_id=p_id, quantity=product_qyt)
                    return JsonResponse({'status': 'Product added successfuly', 'qty': C.objects.filter(user=request.user).count()})
            else:
                return JsonResponse({'status': 'No such Product found'})

    else:
        return JsonResponse({'status': 'Login to continue'})


def remove_product(request):
    if request.user.is_authenticated:
        cart_items = C.objects.filter(user=request.user).all()
        total_price = 0
        if cart_items:
            for item in cart_items:
                total_price += item.product.price
        if request.method == 'POST':
            p_id = request.POST.get('product_id')
            product = get_object_or_404(Product, id=p_id)
            cart = get_object_or_404(C, product=product, user=request.user)
            cart.delete()

            return JsonResponse({'status': 'Product Deleted from your Cart!', 'qty': C.objects.filter(user=request.user).count(), 'total_price':total_price})                


class CheckoutView(View):
    template_name = 'checkout.html'

    def get(self, request):
        return render(request, self.template_name)
    
    