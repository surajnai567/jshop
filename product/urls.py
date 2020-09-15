from django.urls import path
from product.api.apiview import ProductApiView, ProductApiViewCat
urlpatterns = [
    path('', ProductApiView.as_view()),
    path('<catid>/', ProductApiViewCat.as_view())
]