from django.urls import path, re_path
from firstapp import views

app_name = 'firstapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact),
    path('index-2/', views.index_2),
    path('index-3/', views.index_3),
    path('products/', views.products),
    path('product/<int:id_product>/', views.product),
    path('tinh-tong/<int:a>/<int:b>/', views.tinh_tong),
    re_path('read-year/(?P<year>[0-9]{4})/$', views.read_year),
    path('demo-static/', views.demo_static),
    path('websites/', views.read_websites),
    path('contents/', views.read_contents),
    path('contents/<int:pk>/', views.contents_by_web, name='contents_by_web'),
    path('register/', views.register,name='register')
]