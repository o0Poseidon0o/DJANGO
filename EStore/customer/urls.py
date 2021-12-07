from django.urls import path
from customer.views import *


app_name = 'customer'
urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
