from django.urls import path
from . import views



urlpatterns = [
    path('', views.administrador, name='administrador'),  # Muestra la pantalla principal /webadmin/
    path('emisoras/', views.emisoras, name='emisoras'),
    path('emisoras/agregarEmisora/', views.agregar_emisora, name="agregar_emisora"), # Muestra la pantalla para agregar emisora
    path('emisoras/agregarRadio/', views.agregar_radio, name="agregar_radio"), # Muestra la pantalla para agregar radio
    path('emisoras/<int:id_emisora>/editarEmisora/', views.editar_emisora, name="editar_emisora"), # Muestra la pantalla para agregar emisora
    path('emisoras/<int:id_emisora>/eliminarEmisora/', views.borrar_emisora, name="borrar_emisora"), # Muestra la pantalla para agregar emisora
    path('emisoras/<int:id_radio>/eliminarRadio/', views.borrar_radio, name="borrar_radio"), # Muestra la pantalla para agregar emisora
    path('equipos', views.equipos, name='equipos'), # URL para ver los equipos del sistema,
    path('equipos/agregar', views.agregar_equipo, name='agregar_equipo'), # Muestra la pantalla para agregar equipo
    path('equipos/<int:id_equipo>', views.ver_equipo, name='ver_equipo'), # URL para ver la informacion del equipo
    path('equipos/<int:id_equipo>/eliminar', views.borrar_equipo, name='borrar_equipo'), # URL para eliminar un equipo
    path('equipos/<int:id_equipo>/editar', views.modificar_equipo, name='editar_equipo'), # URL para editar equipos
    path('usuarios/agregar', views.agregar_usuario, name='agregar_usuario'), # Form para agregar un usuario nuevo
    path('usuarios/editar/<int:id_usuario>', views.editar_usuario, name='editar_usuario'),
    path('programas', views.programas, name='programas'), # Página principal donde se muestran los programas
    path('programas/agregar', views.agregar_programa, name="agregar_programa"), # Muestra la pantalla para agregar programa
    
]
