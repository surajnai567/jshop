from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.html import format_html

# Create your models here.

class OrderModel(models.Model):
	phone = models.CharField(max_length=12)
	address = models.CharField(max_length=60)
	orderBy = models.CharField(max_length=30)
	orderTime = models.DateTimeField(auto_now_add=True)
	delivered = models.BooleanField(default=False)
	products = ArrayField(
		ArrayField(
			models.CharField(max_length=20)
		)
	)

	def ordered_products(self):
		data = ""
		for list in self.products:
			data += "<li>{}</li>".format(list)
		return format_html(data)

	class Meta:
		ordering = ['delivered']



