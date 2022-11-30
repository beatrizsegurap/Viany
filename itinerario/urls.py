from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
                  path('misitinerarios', views.misItinerarios,name="misitinerarios"),
                  path('paso2', views.agregarDestinos,name="agregardestinos"),
                  path('resumen', views.resumen,name="resumen"),
                  path('nuevo', views.crearItinerario,name="newItinerario"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
