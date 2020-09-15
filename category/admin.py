from django.contrib import admin

# Register your models here.
from .models import Category


@admin.register(Category)
class AdminProduct(admin.ModelAdmin):
	list_display = ['categoryName', 'categoryDiscount', 'image_tag']