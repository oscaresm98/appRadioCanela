from django.urls import path
from . import views
from .custom_views import roles_views, usuarios_views

urlpatterns = [
    path('', views.administrador, name='administrador'),  # Muestra la pantalla principal /webadmin/
    path('emisora', views.emisoras, name='emisoras'),
    path('emisoras/agregarEmisora/', views.agregar_emisora, name="agregar_emisora"), # Muestra la pantalla para agregar emisora
    path('emisoras/agregarRadio/', views.agregar_radio, name="agregar_radio"), # Muestra la pantalla para agregar radio
    path('emisoras/<int:id_emisora>/editarEmisora/', views.editar_emisora, name="editar_emisora"), # Muestra la pantalla para agregar emisora
    path('emisoras/<int:id_emisora>/eliminar/', views.borrar_emisora, name="borrar_emisora"), # Muestra la pantalla para agregar emisora

    path('torneos', views.torneos, name='torneos'),
    path('torneos/agregarTorneo', views.agregar_torneo, name='agregar_torneo'),
    path('torneos/<int:id_torneo>/editar', views.modificar_torneo, name='editar_torneo'),
    path('torneos/<int:id_torneo>/eliminar', views.eliminar_torneo, name='eliminar_torneo'),

    
    path('equipos', views.equipos, name='equipos'), # URL para ver los equipos del sistema,
    path('equipos/agregar', views.agregar_equipo, name='agregar_equipo'), # Muestra la pantalla para agregar equipo
    path('equipos/<int:id_equipo>', views.ver_equipo, name='ver_equipo'), # URL para ver la informacion del equipo
    path('equipos/<int:id_equipo>/eliminar', views.borrar_equipo, name='borrar_equipo'), # URL para eliminar un equipo
    path('equipos/<int:id_equipo>/editar', views.modificar_equipo, name='editar_equipo'), # URL para editar equipos
    
    path('partidos', views.partidos, name='partidos'), # URL para ver los partidos 
    path('partidos/agregar', views.agregar_partido, name='agregar_partido'), # URL para agregar un partido
    path('partidos/<int:id_partido>', views.ver_partido, name='partidos'), # URL para ver informacion del partido
    path('partidos/<int:id_partido>/editar', views.editar_partido, name='editar_partido'), # URL para editar un partido
    path('partidos/<int:id_partido>/eliminar', views.eliminar_partido, name='eliminar_partido'), # URL para agregar un partido

    # path('usuarios',views.usuarios,name="lista_usuarios"),
    # path('usuarios/agregar', views.agregar_usuario, name='agregar_usuario'), # Form para agregar un usuario nuevo
    # path('usuarios/editar/<int:id_usuario>', views.editar_usuario, name='editar_usuario'),
    # path('usuarios/<int:id_usuario>/eliminar',views.borrar_usuario,name='eliminar_usuario'),

    path('usuarios',usuarios_views.usuarios,name="lista_usuarios"),
    path('usuarios/agregar', usuarios_views.agregar_usuario, name='agregar_usuario'), # Form para agregar un usuario nuevo
    path('usuarios/editar/<int:id_usuario>', usuarios_views.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:id_usuario>/eliminar',usuarios_views.borrar_usuario,name='eliminar_usuario'),

    # CAMBIO
    path('roles', roles_views.roles, name="lista_roles"),
    path('roles/agregar', roles_views.agregar_roles, name="agregar_rol"),
    path('roles/<int:id_rol>/editar',roles_views.editar_rol,name="editar_rol"),
    path('roles/<int:id_rol>/eliminar',roles_views.borrar_rol,name="eliminar_rol"),

    
    path('programas', views.programas, name='programas'), # Página principal donde se muestran los programas
    path('programas/agregar', views.agregar_programa, name="agregar_programa"), # Muestra la pantalla para agregar programa
    path('programas/<int:id_programa>', views.ver_programa, name="ver_programa"), # Muestra la información un programa
    path('programas/<int:id_programa>/editar', views.modificar_programa, name="editar_programa"), # Muestra la pantalla para modificar un segmento
    path('programas/<int:id_programa>/eliminar', views.borrar_programa, name="borrar_programa"), # URL para borrar un programa
    
    path('locutores', views.locutores, name='locutores'), # Muestra todos los locutores de la radio
    path('locutores/agregar', views.agregar_Locutor, name='agregar_locutor'), # Form para agregar un locutor nuevo
    path('locutores/<int:id_locutor>', views.ver_locutor, name='locutor'), # URL para ver informacion del partido
    path('locutores/<int:id_locutor>/eliminar', views.eliminar_locutor, name='eliminar_locutor'), # URL para eliminar un locutor
    path('locutores/<int:id_locutor>/editar', views.editar_locutor, name='editar_locutor'), # URL para editar un locutor
    
    path('publicidad', views.publicidad, name='publicidad'), #Pagina principal donde se muestra la publicidad.
    path('publicidad/agregar', views.agregar_publicidad, name = 'agregar_publicidad'), #Muestra la pantalla para agregar publicidad.
    path('publicidad/<int:id_publicidad>', views.ver_publicidad, name = 'ver_publicidad'), # Muestra la pantalla de informacion de la publicidad.
    path('publicidad/<int:id_publicidad>/editar', views.modificar_publicidad, name = 'editar_publicidad'), # Muestra la pantalla para editar una de la publicidad.
    path('publicidad/<int:id_publicidad>/eliminar', views.borrar_publicidad, name="borrar_publicidad"), # URL para borrar una publicidad
    
    path('noticia', views.noticia, name='noticia'), #Pagina principal donde se muestra la noticias.
    path('noticia/agregar', views.agregar_noticia, name = 'agregar_noticia'), #Muestra la pantalla para agregar noticia.
    path('noticia/<int:id_noticia>', views.ver_noticia, name = 'ver_noticia'), # Muestra la pantalla de informacion de la noticia.
    path('noticia/<int:id_noticia>/editar', views.modificar_noticia, name = 'editar_noticia'), # Muestra la pantalla para editar una de la noticia.
    path('noticia/<int:id_noticia>/eliminar', views.borrar_noticia, name="borrar_noticia"), # URL para borrar un noticia
    
    
    path('transmision', views.transmision, name='transmision'), #Pagina principal donde se muestra lss transmisiones.
    path('transmision/agregar', views.agregar_transmision, name = 'agregar_transmision'), #Muestra la pantalla para agregar transmision.
    path('transmision/<int:id_transmision>/editar', views.modificar_transmision, name = 'editar_transmision'), # Muestra la pantalla para editar una de la transmision.
    path('transmision/<int:id_transmision>/eliminar', views.borrar_transmision, name="borrar_transmision"), # URL para borrar un transmision

    path('podcasts',views.podcasts,name='podcasts'),# Pagina principal donde se muestran los podcasts
    path('podcasts/agregar',views.agregar_podcasts,name='agregar_podcasts'),#Muestra la pantalla para agregar podcasts
    path('podcasts/<int:id_podcast>/editar',views.editar_podcast,name='editar_podcast'),#Muestra la pantalla para editar podcast
    path('podcasts/<int:id_podcast>/eliminar',views.borrar_podcast,name='borrar_podcast'),#Muestra la pantalla para editar podcast
]
