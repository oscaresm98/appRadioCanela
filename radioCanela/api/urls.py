# api/urls.py
from django.urls import include, path
# rom .views import FacebookLogin, TwitterLogin, CreateUser
from . import views

urlpatterns = [
    path('hora_actual/', views.ListTime.as_view()),
    path('programa/', views.ListPrograma.as_view()),
    path('auditoria/', views.ListAuditoria.as_view()),
    path('concurso/', views.ListConcursos),
    path('emisoras/', views.emisoraList),
    path('emisoras/<int:pk>', views.emisora_detalle),
    path('usuarios/', views.usuarioList,name='usuarios-list'),
    path('torneos/', views.torneosList,name='torneos-list'),
    path('equipos/', views.equipoList ,name='equipos-list')
    #path('radio/', views.ListEmisora.as_view()),

    # path('emisoras/', views.ListEmisora.as_view()),
    
    # path('encuestasradio/', views.ListEncuestas.as_view()),
    # path('encuestas/', views.ListEncuestasActivas.as_view()),
    # path('voto/', views.CreateVoto.as_view()),
    # path('voto/<int:pk>/borrar', views.DeleteVoto.as_view()),
    # path('votaciones/', views.ListVotaciones.as_view()),
    # path('votacionesuser/<int:id_usuario>', views.ListVotacionesUsuario.as_view()),
    # path('votaciones/<int:id_encuesta>', views.ListVotacionesEncuesta.as_view()),
    # path('encuestas/<int:id_encuesta>/resultados', views.ListResultadosEncuesta.as_view()),
    # path('segmento/<int:id_segmento>/publicidad', views.ListPublicidad.as_view(), name="list_segmento_publicidad"),
    # path('emisora/<int:id_emisora>/segmentos', views.ListEmisoraSegmentos.as_view(), name="list_emisora_segmentos"),
    # path('emisora/<int:id_emisora>/segmento/<int:id_segmento>', views.ListEmisoraSegmento.as_view(), name="list_emisora_segmento"),
    # path('segmento/<int:id_segmento>/locutores', views.ListLocutores.as_view(), name="list_segmento_locutor"),
    # path('segmentos/today', views.ListSegmentosDiaActual.as_view()),
    # path('emisoras/<int:id_emisora>/segmentos/today', views.ListSegmentosEmisoraDiaActual.as_view()),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    # path('rest-auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),
    # path('rest-auth/register/', CreateUser.as_view(), name='usuario_register'),
    # path('publicidad/<int:id_publicidad>/frecuencias', views.ListFrecuencias.as_view(), name='frecuencias'),
    # path('emisoras/<int:id_emisora>/telefonos', views.ListTelefonosEmisora.as_view(), name='telefonos_emisora'),
    # path('emisoras/<int:id_emisora>/redes_sociales', views.ListRedSocialEmisora.as_view(), name='redes_sociales_emisora'),
    # path('segmentos/<int:id_segmento>/locutores', views.ListLocutoresSegmento.as_view(), name='locutores_segmento'),
    # path('imagenes/', views.ListImagenes.as_view(), name="list_imagenes"),
    # path('imagenes/<int:id_segmento>', views.ListImagenesSegmento.as_view(), name='imagenes_segmento'),
    # path('videos/', views.ListVideos.as_view(), name="list_videos"),
    # path('videos/<int:id_segmento>', views.ListVideosSegmento.as_view(), name='videos_segmento'),
    # path('favoritos/<str:usuario>', views.ListFavoritosUsuario.as_view(), name='favoritos_usuario'),
    # path('segmentos/<int:id_segmento>/encuestas', views.ListEncuestasSegmentos.as_view(), name='encuestas'),
    # path('favoritos_create/<int:id_segmento>/<str:username>', views.CreateFavoritoView, name='create_favorito'),
    # path('favoritos_delete/<int:id_segmento>/<str:username>', views.DeleteFavoritoView, name='delete_favorito'),
    # path('usuarios/<int:id_usuario>', views.ListUsuariosPorId.as_view()),
    # path('equipos', views.ListEquipos.as_view(), name="list_equipos"),
    # path('equipos/<int:id_equipo>', views.ListEquiposPorId.as_view()),
    # path('torneos', views.ListTorneos.as_view(), name="list_torneos"),

    # path('transmisiones', views.ListTransmisiones.as_view(), name="list_transmisiones"),
    # path('transmisiones/<str:fecha_evento>', views.ListTransmisionesPorFecha.as_view()),
    # path('transmisiones_fecha', views.ListTransmisionesEnFecha.as_view(), name="list_transmisiones_fecha"),

    # path('emisora/<int:id_emisora>/transmisiones', views.ListTransmisionesPorEmisora.as_view()),
    # path('transmisionemisora', views.ListTransmisionEmisora.as_view()),

    # path('galeria', views.ListGaleria.as_view(), name="list_galeria"),
    # path('emisora/<int:id_emisora>/galeria', views.ListGaleriaPorEmisora.as_view()),
    # path('galeriaemisora', views.ListGaleriaEmisora.as_view()),

    # path('podcasts', views.ListPodcasts.as_view(), name="list_podcasts"),
    # path('emisora/<int:id_emisora>/podcasts', views.ListPodcastsPorEmisora.as_view()),
    # path('podcastsemisora', views.ListPodcastsEmisora.as_view()),

    # path('contactenos/', views.CreateContacto.as_view(), name='contactenos'),
    # path('usuarios_redes/', views.CreateUserRedes.as_view(), name='userredes'),
    # path('autenticar/', views.AutenticarUsuario.as_view()),

    # path('usuarios/<int:pk>/editar', views.UpdateUsuario.as_view()),
    # path('rest-auth/reset/password/', views.ResetPassword.as_view()),

    # path('usuariosadministrador', views.ListAdminLocutores.as_view(), name='list_adminlocutores'),
    # path('usuarios', views.ListUsuarios.as_view(), name="list_usuarios"),
    # path('locutores', views.ListUsuariosLocutores.as_view(), name='list_locutores'),
    # path('clientes', views.ListUsuariosClientes.as_view(), name='list_clientes'),

]
