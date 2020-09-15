from .serializer import SubCatApiSerializer
from rest_framework.views import APIView, Response
from subcategory.models import SubCategory


class SubCatApiView(APIView):
	def get(self, request):
		sub = SubCategory.objects.all()
		data = SubCatApiSerializer(sub, many=True).data
		return Response(data)