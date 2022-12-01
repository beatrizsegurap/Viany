from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('', views.checkList,name="checklist"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
