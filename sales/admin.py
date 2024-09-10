from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Sale)

class SaleAdmin(admin.ModelAdmin):
    list_display = ('date', 'product', 'quantity' , 'price')