from django.db import models
from category.models import Category
from subcategory.models import SubCategory
from django.utils.html import mark_safe

# Create your models here.


class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
	itemName = models.CharField(null=False, max_length=15)
	itemShortDesc = models.CharField(max_length=60)
	itemDetail = models.CharField(max_length=50)
	MRP = models.IntegerField()
	discount = models.IntegerField(default=0)
	sellMRP = models.IntegerField(null=False)
	quantity = models.IntegerField()
	imageUrl = models.ImageField(upload_to='product')
	orderId = models.CharField(max_length=10)
	weight = models.DecimalField(decimal_places=2, max_digits=5)

	def image_tag(self):
		return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.imageUrl))

	image_tag.short_description = 'Image'

	def __str__(self):
		return self.itemName

