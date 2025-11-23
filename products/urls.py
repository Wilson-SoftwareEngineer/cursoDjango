from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products_list'),  # http://127.0.0.1:8000/products/   
]