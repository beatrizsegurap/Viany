from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('menu/', views.actividades, name='actividad'),
    path('agregar/', views.agregarActividad, name='agregarActividad')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
