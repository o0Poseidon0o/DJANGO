from django.urls import conf, path
from fristapp.views import index, index_3, product, products
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',index),
    path('products/', products),
    path('product/<int:id_product>/',product),
    path('index-3',index_3)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)