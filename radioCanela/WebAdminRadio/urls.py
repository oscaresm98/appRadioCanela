from django.urls import path
from . import views


urlpatterns = [
    path('', views.administrador, name='administrador'),  # Muestra la pantalla principal /webadmin/
    path('emisoras', views.emisoras, name='emisoras'),
    path('emisoras/agregar', views.agregar_emisora, name="agregar_emisora"), # Muestra la pantalla para agregar emisora
    path('equipos', views.equipos, name='equipos'), # URL para ver los equipos del sistema,
    path('equipos/agregar', views.agregar_equipo, name='agregar_equipo'), # Muestra la pantalla para agregar equipo
    
]
