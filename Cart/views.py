from django.shortcuts import render
from django.views.generic import View


class CartView(View):
    template_name = 'cart.html'

    def get(self, request):
        return render(request, self.template_name)
    
    
class CheckoutView(View):
    template_name = 'checkout.html'

    def get(self, request):
        return render(request, self.template_name)
    
    