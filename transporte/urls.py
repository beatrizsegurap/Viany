from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('menu/', views.transporte, name='menu-transporte'),
    path('agregar/', views.agregarTransporte, name='agregarTransporte')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)