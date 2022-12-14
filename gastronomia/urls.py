from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('menu/', views.gastronomia, name='gastronomia'),
    path('agregar/', views.agregarGastronomia, name='agregarGastronomia'),
    path('menu/<int:id_gastronomia>', views.eliminarGastronomia, name= 'eliminarGastronomia'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)