from django.db import models
from category.models import Category
from subcategory.models import SubCategory
from django.utils.html import mark_safe
from pricelist.models import PriceList
from cloudinary.models import CloudinaryField

# Create your models here.


class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
	itemName = models.CharField(null=False, max_length=15)
	itemShortDesc = models.CharField(max_length=60)
	itemDetail = models.CharField(max_length=50)
	MRP = models.IntegerField(blank=True, null=True)
	#MRP = models.ForeignKey(PriceList, on_delete=models.CASCADE)
	discount = models.IntegerField(blank=True, null=True)
	sellMRP = models.IntegerField(blank=True, null=True)
	quantity = models.IntegerField(default=0)
	#imageUrl = models.ImageField(upload_to='product')
	imageUrl = CloudinaryField('image')
	orderId = models.CharField(max_length=10)
	weight = models.DecimalField(decimal_places=2, max_digits=8)

	def image_tag(self):
		return mark_safe('<img src="%s" width="150" height="150" />' % (self.imageUrl.url))

	image_tag.short_description = 'Image'

	def __str__(self):
		return self.itemName

