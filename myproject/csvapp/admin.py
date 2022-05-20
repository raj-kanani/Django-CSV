from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'name', 'detail', 'price', 'created']


# Register your models here.
@admin.register(Customer)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password', 'password1']
