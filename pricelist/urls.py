from django.urls import path
from .api.apiview import GetAllPrice
urlpatterns = [
    path('', GetAllPrice),

]