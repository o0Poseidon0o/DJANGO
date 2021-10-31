from django.urls import path
from fristapp.views import index, index_3, product, products

urlpatterns = [
    path('',index),
    path('products/', products),
    path('product/<int:id_product>/',product),
    
    path('index-3',index_3)
]