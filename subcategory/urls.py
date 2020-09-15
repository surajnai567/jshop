from django.urls import path
from subcategory.api.apiview import SubCatApiView
urlpatterns = [
    path('', SubCatApiView.as_view()),
]