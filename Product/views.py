from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView, ListView
from Product.models import Product, Category
from django.core.paginator import Paginator
from django.db.models import Q


class IndexView(View):
    template_name = 'index.html'

    def get(self, requset):
        product = Product.objects.filter(status=True)[:3]
        context = {
            'product':product
        }
        return render(requset, self.template_name, context)
    

class AboutView(View):
    template_name = 'about.html'

    def get(self, requset):
        return render(requset, self.template_name)
    

class ContactView(View):
    template_name = 'contact.html'

    def get(self, requset):
        return render(requset, self.template_name)
    

class ShopView(View):
    template_name = 'shop.html'

    def get(self, requset):
        products = Product.objects.filter(status=True)
        category = Category.objects.all()
        paginator = Paginator(products, 12)
        page_number = requset.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'products': page_obj,
            'category': category
        }
        return render(requset, self.template_name, context)
    

class SinglProductView(DetailView):
    template_name = 'single-product.html'
    model = Product
    slug_url_kwarg = 'slug'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, status=True, slug=self.kwargs['slug'])
        context['realted_product'] = Product.objects.filter(category__product=product, status=True).exclude(slug=self.kwargs['slug'])[:3]
        return context
    


class SearchView(ListView):
    template_name = 'shop.html'
    context_object_name = 'products'
    
    def get_queryset(self) -> QuerySet[Any]:
        request = self.request
        query = request.GET.get('search')
        if query is not None:
            product_query = Q(title__icontains=query) | Q(description__icontains=query)
            return Product.objects.filter(product_query, status=True).distinct()
        