from django.db import models
from subcategory.models import SubCategory

# Create your models here.


class PriceList(models.Model):
	subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
	amount = models.IntegerField()
	discount = models.IntegerField(default=0)
