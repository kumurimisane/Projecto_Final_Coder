from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from .views import *
from . import views

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('cartas/', cartas, name='Cartas'),
    path('crear-cartas/', crearCartas, name='crearCartas'),
    path('eliminar-cartas/<int:id>', eliminarCartas, name='eliminarCartas'),
    path('edita-cartas/<int:id>', editarCartas, name='editarCartas'),
    path('cartas-detail/<int:pk>', CartasDetail.as_view(), name='cartasDetail'),
    path('torneo/', torneo, name='torneo'),
    path('crear-torneo/', crearTorneo, name='crearTorneo'),
    path('eliminar-torneo/<int:id>', eliminarTorneo, name='eliminarTorneo'),
    path('edita-torneo/<int:id>', editarTorneo, name='editarTorneo'),
    path('torneo-detail/<int:pk>', TorneoDetail.as_view(), name='torneoDetail'),
    path('mazos/', MazoList.as_view(), name='Mazos'),
    path('mazos-detail/<int:pk>', MazoDetail.as_view(), name='mazoDetail'),
    path('mazos-create/', MazoCreate.as_view(), name='crearMazo'),
    path('mazos-update/<int:pk>', MazoUpdate.as_view(), name='editarMazo'),
    path('mazos-delete/<int:pk>', MazoDelete.as_view(), name='eliminarMazo'),
    path('contactenos/', Contactenos.as_view(), name='Contactenos'),
    path('about/', about, name='About'),
    
    #Login-Logout-Register
    path('login/', loginView, name='login'),
    path('registro/', register, name='register'), 
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editar-perfil/', editarPerfil, name='editarPerfil'),
    
    path('<str:page>/', views.no_pages, name='no_pages'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)