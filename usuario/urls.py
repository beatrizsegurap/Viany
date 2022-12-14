from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('dashboard-user/', views.dashboarduser, name='dashboarduser'),
    path('cerrarsesion/', views.cerrarSesion, name='cerrarsesion'),
    path('hospedaje/', include('hospedaje.urls')),
    path('itinerario/', include('itinerario.urls')),
    path('transporte/', include('transporte.urls')),
    path('checklist/', include('checklist.urls')),
     path('presupuesto/', include('presupuesto.urls')),
      path('actividades/', include('actividades.urls')),
       path('gastronomia/', include('gastronomia.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)