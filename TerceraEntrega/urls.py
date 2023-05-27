
from django.contrib import admin
from django.urls import path, include
from PadelApp.views import inicio
from django.conf import settings
from django.conf.urls.static import static
from .views import about_me

urlpatterns = [
    path("", inicio, name="inicio" ),
    path('admin/', admin.site.urls),
    path("PadelApp/", include("PadelApp.urls")),
    path("Usuarios/", include("Usuarios.urls")),
    path("about/", about_me, name="about_me"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)