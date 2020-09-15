from rest_framework.serializers import ModelSerializer
from subcategory.models import SubCategory


class SubCatApiSerializer(ModelSerializer):
	class Meta:
		fields = '__all__'
		model = SubCategory