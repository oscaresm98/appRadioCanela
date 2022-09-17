from django.urls import path
from . import views



urlpatterns = [
    path('', views.administrador, name='administrador'),  # Muestra la pantalla principal /webadmin/
    path('emisoras/', views.emisoras, name='emisoras'),
    path('emisoras/agregar/', views.agregar_emisora, name="agregar_emisora"), # Muestra la pantalla para agregar emisora
    path('emisoras/<int:pk>/editar/', views.editar_emisora, name="editar_emisora"), # Muestra la pantalla para agregar emisora
    path('equipos', views.equipos, name='equipos'), # URL para ver los equipos del sistema,
    path('equipos/agregar', views.agregar_equipo, name='agregar_equipo'), # Muestra la pantalla para agregar equipo
    # path('programas', views.segmentos, name='segmentos'), # Página principal donde se muestran los segmentos
    # path('programas/agregar', views.agregar_segmento, name="agregar_segmento"), # Muestra la pantalla para agregar segmento
    # path('programas/<int:id_segmento>', views.ver_segmento, name="ver_segmento"), # Muestra la información un segmento
    # path('programas/<int:id_segmento>/editar', views.modificar_segmento, name="editar_segmento"), # Muestra la pantalla para modificar un segmento
    # path('programas/<int:id_segmento>/eliminar', views.borrar_segmento, name="borrar_segmento"), # URL para borrar un segmento
    
    
]
