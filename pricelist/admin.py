from django.contrib import admin
from .models import PriceList
# Register your models here.


@admin.register(PriceList)
class PriceAdmin(admin.ModelAdmin):
	list_display = ['subcategory', 'amount', 'discount']
