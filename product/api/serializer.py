from rest_framework.serializers import ModelSerializer
from product.models import Product
from rest_framework import serializers


class ProductSerializer(ModelSerializer):
	class Meta:
		fields = '__all__'
		model = Product