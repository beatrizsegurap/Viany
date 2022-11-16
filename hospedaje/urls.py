from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('menu/', views.hospedaje, name='menu-hospedaje'),
    path('agregar/', views.agregarHospedaje, name='agregar-hospedaje')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






