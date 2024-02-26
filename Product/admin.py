from django.contrib import admin
from Product.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'status', 'category']
    prepopulated_fields = {
        'slug': ('title', )
    }
    list_filter = ['title', 'status', 'price']
    list_editable = ['status', 'price']
    ordering = ['-id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {
        'slug': ('name',)
    }
    ordering = ['-id']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']
    list_filter = ['phone', 'email']
    list_editable = ['phone', 'email']

admin.site.register(Order)
admin.site.register(Payment)
