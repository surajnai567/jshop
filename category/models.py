from django.db import models
from django.utils.html import mark_safe
import cloudinary
# Create your models here.


class Category(models.Model):
	categoryName = models.CharField(null=False, max_length=15)
	categoryDescription = models.CharField(null=False, max_length=50)
	categoryDiscount = models.IntegerField(default=0)
	categoryImageUrl = models.ImageField(upload_to='category')
	image = cloudinary.models.CloudinaryField('image')

	def image_tag(self):
		return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.categoryImageUrl))

	image_tag.short_description = 'Image'

	def __str__(self):
		return self.categoryName
