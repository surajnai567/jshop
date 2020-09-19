from pricelist.models import PriceList
from subcategory.models import SubCategory
from django.http.response import JsonResponse


def GetAllPrice(request):
	priceList = PriceList.objects.all()
	gold = ""
	silver = ""
	for price in priceList:
		subcat = SubCategory.objects.filter(id=price.subcategory.id).get()
		if subcat.name.lower() == 'gold':
			gold = price.amount
		if subcat.name.lower() == 'silver':
			silver = price.amount
	data = {"gold": gold, "silver": silver}
	return JsonResponse(data)

