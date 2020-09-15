from .serializer import ProductSerializer
from rest_framework.views import APIView, Response
from product.models import Product
from subcategory.models import SubCategory


class ProductApiView(APIView):
	def get(self, request):
		products = Product.objects.all()
		data = ProductSerializer(products, many=True).data
		for da in data:
			da['imageUrl'] = "http://192.168.43.222:8080" + da['imageUrl']
			sub = SubCategory.objects.filter(id=da['subCategory'])
			if(len(sub)):
				da['subCatName'] = sub[0].name
		return Response(data)


class ProductApiViewCat(APIView):
	def get(self, request, catid):
		products = Product.objects.filter(category=catid)
		data = ProductSerializer(products, many=True).data
		for da in data:
			da['imageUrl'] = "jshop-api-backend.herokuapp.com" + da['imageUrl']
			sub = SubCategory.objects.filter(id=da['subCategory'])
			if (len(sub)):
				da['subCatName'] = sub[0].name
		return Response(data)
