from django.urls import path
from .views import PostOrderData
urlpatterns = [
    path('', PostOrderData),
]