from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import ItiViews

urlpatterns = [
                  path('', ItiViews.dash),
                  path('paso2', ItiViews.dash2),
                  path('resumen', ItiViews.resumen),
                  path('listar', ItiViews.listar),
                  path('escanear', ItiViews.escanear)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
