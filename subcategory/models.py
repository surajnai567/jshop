from django.db import models
from category.models import Category

# Create your models here.


class SubCategory(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(null=False, max_length=15)

	def __str__(self):
		return self.name