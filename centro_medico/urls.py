from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_bienvenida, name='pagina_bienvenida'),
    path('seleccionar_perfil/', views.seleccionar_perfil, name='seleccionar_perfil'),
    path('registro/paciente/', views.registro_paciente, name='registro_paciente'),
    path('inicio_sesion_paciente/', views.inicio_sesion_paciente, name='inicio_sesion_paciente'),
    path('inicio_paciente/', views.inicio_paciente, name='inicio_paciente'),
    path('registro/medico/', views.registro_medico, name='registro_medico'),
    path('inicio_sesion_medico/', views.inicio_sesion_medico, name='inicio_sesion_medico'),
    path('inicio_medico/', views.inicio_medico, name='inicio_medico'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
