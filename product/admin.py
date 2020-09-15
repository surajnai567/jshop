from django.contrib import admin

# Register your models here.
from .models import Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
	list_display = ['itemName', 'sellMRP', 'category', 'image_tag']