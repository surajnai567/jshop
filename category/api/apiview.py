from rest_framework.views import APIView
from .serializer import CategorySerializer
from category.models import Category
from rest_framework.views import Response

class CategoryApiView(APIView):
	def get(self, request):
		cat = Category.objects.all()
		data = CategorySerializer(cat, many=True).data
		for da in data:
			da['categoryImageUrl'] = "http://192.168.43.222:8080"+da['categoryImageUrl']
		return Response(data)

