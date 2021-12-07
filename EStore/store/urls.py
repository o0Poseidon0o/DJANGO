from django.urls import path
from store.views import *


app_name = 'store'
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('subcategory/<int:pk>/', subcategory, name='subcategory'),
]
