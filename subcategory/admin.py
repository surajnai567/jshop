from django.contrib import admin

# Register your models here.
from .models import SubCategory


@admin.register(SubCategory)
class AdminProduct(admin.ModelAdmin):
	list_display = ['name', 'category']
