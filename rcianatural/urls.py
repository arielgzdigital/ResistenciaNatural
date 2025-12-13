from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name = 'path_home'),
    path('nosotros/', views.Nosotros, name = 'path_nosotros'),   
    path('resistencia/', views.Resistencia, name = 'path_resistencia'),
    path('contacto/', views.Contacto, name = 'path_contacto'),

    #enlazar a las url de la app
    path('donde_ir/', include('articulos_ir.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('comentarios/', include('comentarios.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
