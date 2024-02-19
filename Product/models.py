from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    
    def __str__(self):
        return self.name
    

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Product(models.Model):
    title = models.CharField(max_length=250)    
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(default=1, decimal_places=2, max_digits=12)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='upload/products/')
    status = models.BooleanField(default=False)
    created = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:single-product', args=[self.slug])
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=400, blank=False)
    phone = models.CharField(max_length=20, blank=True)
    date = models.DateField(default=timezone.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.product.title

