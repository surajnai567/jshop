from django.contrib import admin

# Register your models here.
from .models import OrderModel


@admin.register(OrderModel)
class AdminOrder(admin.ModelAdmin):
	list_display = ['orderBy', 'phone', 'address', 'orderTime', 'ordered_products', 'delivered'] #'products']
