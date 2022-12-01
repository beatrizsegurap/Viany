from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('misitinerarios', views.misItinerarios,name="misitinerarios"),
    path('resumen', views.resumen,name="resumen"),
    path('newItinerario', views.crearItinerario,name="newItinerario"),
    path('agregardestinos', views.agregarDestinos,name="agregardestinos"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
