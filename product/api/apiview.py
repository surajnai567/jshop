from .serializer import ProductSerializer
from rest_framework.views import APIView, Response
from product.models import Product
from subcategory.models import SubCategory
from pricelist.models import PriceList
import math


class ProductApiView(APIView):
	def get(self, request):
		products = Product.objects.all()
		data = ProductSerializer(products, many=True).data
		for da in data:
			da['imageUrl'] = "https://res.cloudinary.com/hhua8dgho/" + da['imageUrl']
			sub = SubCategory.objects.filter(id=da['subCategory'])
			weight = da['weight']
			priceobj = PriceList.objects.filter(subcategory=da['subCategory'])[0]
			discount = priceobj.discount
			if(len(sub)):
				da['subCatName'] = sub[0].name
				da['MRP'] = math.ceil(float(weight) / 10 * int(priceobj.amount))
				da['discount'] = discount
				da['sellMRP'] = math.ceil(float(weight) / 10 * int(priceobj.amount) - (
						float(weight) / 10 * int(priceobj.amount)) * int(discount) / 100)
		return Response(data)


class ProductApiViewCat(APIView):
	def get(self, request, catid):
		products = Product.objects.filter(category=catid)
		data = ProductSerializer(products, many=True).data
		for da in data:
			da['imageUrl'] = "https://res.cloudinary.com/hhua8dgho/" + da['imageUrl']
			sub = SubCategory.objects.filter(id=da['subCategory'])
			weight = da['weight']
			priceobj = PriceList.objects.filter(subcategory=da['subCategory'])[0]
			discount = priceobj.discount
			if (len(sub)):
				da['subCatName'] = sub[0].name
				da['MRP'] = math.ceil(float(weight)/10*int(priceobj.amount))
				da['discount'] = discount
				da['sellMRP'] = math.ceil(float(weight)/10*int(priceobj.amount) - (float(weight)/10*int(priceobj.amount))*int(discount)/100)
		return Response(data)
