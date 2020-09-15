from django.urls import path
from category.api.apiview import CategoryApiView
urlpatterns = [
    path('', CategoryApiView.as_view()),
]