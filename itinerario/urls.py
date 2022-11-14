from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.dash, name='dash'),
    path('dash2/', views.dash2, name='dash2')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)