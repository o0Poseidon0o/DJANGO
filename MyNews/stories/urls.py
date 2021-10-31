from django.urls import conf, path
from stories.views import index
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',index),
    path('stories/',index),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)