from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('menu/', views.hospedaje, name='hospedaje'),
    path('agregar/', views.agregarHospedaje, name='agregarHospedaje'),
    path('menu/<int:id_hospedaje>', views.eliminarHospedaje, name= 'eliminarHospedaje' ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






