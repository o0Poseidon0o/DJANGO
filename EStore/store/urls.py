
from django.contrib import admin
from django.urls import path
from store.views import *


app_name='store'
urlpatterns = [
    path('', index, name='index'),
]
