from django.shortcuts import render, HttpResponse
import json
from product.models import Product
from .models import OrderModel

# Create your views here.

def PostOrderData(request):
	if request.POST:
		try:
			data = json.loads(request.body.decode('utf-8'))
			print(data)
			listproduct = []
			for dat in data:
				try:
					id = int(dat)
					print(id)
					product = Product.objects.filter(id=id).get()
					listproduct.append([product.itemName, product.category, product.subCategory, data[dat]])

				except:
					pass
			print(listproduct)
			order = OrderModel.objects.create(phone=data['phone'], address=data['address'],
											  orderBy=data['name'], products=listproduct)
			order.save()


		except Exception as e:
			print(e)
	return HttpResponse('Success')