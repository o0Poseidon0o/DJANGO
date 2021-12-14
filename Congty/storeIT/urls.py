
from django.contrib import admin
from django.urls import path
from storeIT.views import *

app_name='storeIT'
urlpatterns = [
    path('', index, name='index'),
   
]
