from pricelist.models import PriceList
from subcategory.models import SubCategory
from django.http.response import HttpResponse


def GetAllPrice(request):
	priceList = PriceList.objects.all()
	gold = ""
	silver = ""
	for price in priceList:
		subcat = SubCategory.objects.filter(id=price.subcategory).get()[0]
		if subcat.name is 'gold':
			gold = price.amount
		if subcat.name is 'silver':
			silver = price.amount
	return HttpResponse({"gold": gold,
			            "silver": silver})

