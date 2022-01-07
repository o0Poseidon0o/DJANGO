from django.urls import path
from customer.views import *


app_name = 'customer'
urlpatterns = [
    path('login/', login_customer, name='login'),
    path('logout/', logout_customer, name='logout'),
    path('users/', users, name='users'),
    path('logout-user/', logout_user, name='logout_user'),
]
