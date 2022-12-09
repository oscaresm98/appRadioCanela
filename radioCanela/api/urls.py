# api/urls.py
from django.urls import include, path
# rom .views import FacebookLogin, TwitterLogin, CreateUser
from . import views
import accounts.api_views as account_api_views


app_name = 'api'

urlpatterns = [
    path('hora_actual/', views.ListTime.as_view()),
    path('programas/', views.programaList,name='programas-list'),
    path('programas/<int:pk>', views.programa_detalle,name='programas-detalle'),
    path('programas/<int:pk>/locutores', views.programaLocutorList,name='programas-detalle'),
    path('emisora/<int:id_emisora>/dia/<str:dia>/programas', views.ListProgramasDia.as_view(), name="list_programa_dia"),
    
    path('auditoria/', views.ListAuditoria.as_view()),
    path('concurso/', views.ListConcursos),
    path('emisoras/', views.emisoraList,name='emisoras-list'),
    path('emisoras/<int:pk>', views.emisora_detalle,name='emisoras-detalle'),
    path('emisora/<int:id_emisora>/programas', views.ListEmisoraProgramas.as_view(), name="list_emisora_programas"),
    path('emisora/<int:id_emisora>/transmisiones', views.ListEmisoraTrasmisiones.as_view(), name="list_emisora_transmisiones"),
    path('segmentoemisora/', views.SegmentoEmisoraList.as_view(),name='segmento_emisora-list'),
    path('horarios/', views.HorariosList.as_view(),name='horarios-list'),
    path('usuarios/', views.usuarioList,name='usuarios-list'),
    
    path('registro/', views.RegisterView.as_view(),name='registro-view'),
    path('login/', views.LoginView.as_view(),name='login-view'),
    path('social_login/', account_api_views.SocialLoginView.as_view(), name='social-login-view'),
    path('user/', views.UserView.as_view(),name='usuario-view'),
    path('logout/', views.LogoutView.as_view(),name='logout-view'),
    path('update_profile/', views.UpdateProfileView.as_view(),name='update-view'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password_view'),
    
    # path('roles/', views.rolesList,name='roles-list'),
    path('roles/', views.ListRoles.as_view(), name='roles-list'),
    
    path('permisos/', views.permisosList,name='permisos-list'),

    path('torneos/', views.torneosList,name='torneos-list'),
    
    path('equipos/', views.equipoList ,name='equipos-list'),
    path('equipos/<int:pk>', views.EquipoPorId.as_view()),
    
    path('partidos', views.ListPartidoTransmisiones.as_view(), name="partidos-list"), # URL para obtener todos los partidos
    path('partidos_jugados', views.ListPartidosJugados.as_view(), name="partidos-list-jugados"), # URL para obtener los partidos ya jugados
    path('partidos_por_jugar', views.ListPartidosPorJugar.as_view(), name="partidos-list-por-jugar"), # URL para obtener los partidos por jugar
    
    path('radios/',views.radio_List,name='radio-list'),
    path('radios/<int:pk>',views.radio_detalle,name='radio-detalle'),
    path('redsocial/',views.redsocial.as_view(),name='redsocial-list'),
    path('redsocial/<int:pk>',views.redsocial_detalle,name='redsocial-detalle-list'),
    path('redsocialequipo/',views.redsocialequipo.as_view(),name='redsocial-equipo-list'),
    
    path('locutores/',views.LocutorList,name='locutores-list'),
    path('locutores/<int:pk>', views.Locutor_detalle, name='locutor-detalle'),
    
    path('radio/<int:id_radio>/publicidad',views.ListPublicidad.as_view(), name="list_radio_publicidad"),
    path('radio/<int:id_radio>/emisoras',views.ListRadioEmisoras.as_view(), name="list_radio_emisora"),
    
    path('noticias/',views.NoticiasList.as_view(),name='noticias-list'),
    path('noticia/<int:pk>', views.Noticia_detalle.as_view(), name='noticia-detalle'),
    path('emisora/<int:id_emisora>/noticia',views.ListNoticia.as_view(), name="list_emisora_noticia"),
    path('noticia/<str:tipo>', views.NoticiaTipo.as_view(), name="list_noticia_tipo"),

    path('podcasts', views.ListPodcasts,name='podcast-list'),
    path('emisora/<int:id_emisora>/podcasts', views.Emisora_Podcast_list,name='list_emisora_podcast'),
    path('podcasts/<int:id_podcast>',views.podcast_Detalle,name='podcast_Detalle'),
    # path('podcastsemisora', views.ListPodcastsEmisora.as_view()),
    
    path('galerias', views.GaleriaList, name='galeria-list'),
    path('emisora/<int:id_emisora>/galeria', views.Galeria_detalle, name='galeria_detalle'),
    path('emisora/<int:id_emisora>/galeria/imagenes', views.GaleriaImagenes_detalle, name='galeriaImagenes_detalle'),
    path('emisora/<int:id_emisora>/galeria/videos', views.GaleriaVideos_detalle, name='galeriaVideos_detalle'),
    path('multimedia', views.ImagenesVideosList, name='videos_imagenes'),
    # path('multimedia', views.ImagenesVideosList, name='videos_imagenes'),

    path('politicas', views.ListPoliticas.as_view(), name='politicas'),
    path('politica_vigente', views.politicas_privacidad_vigente, name='politica_vigente'),

    
    #path('radio/', views.ListEmisora.as_view()),

    # path('emisoras/', views.ListEmisora.as_view()),
    
    path('emisora/<int:id_emisora>/encuestas',views.EncuestaEmisora,name='encuesta-emisora'),
    path('encuestas/', views.EncuestaListActivas,name='encuesta-list'),
    path('encuestas/<int:id_encuesta>/pregunta',views.PreguntaEcuestas,name='encuesta-pregunta'),
    path('encuestas/<int:id_encuesta>/pregunta/<int:id_pregunta>/opcion',views.OpcionesPreguntas,name='pregunta-opciones'),

    path('encuestas_app/', views.ListEncuestaAppView.as_view(),name='encuesta-list'),

    
    # path('voto/', views.CreateVoto.as_view()),
    # path('voto/<int:pk>/borrar', views.DeleteVoto.as_view()),
    # path('votaciones/', views.ListVotaciones.as_view()),
    # path('votacionesuser/<int:id_usuario>', views.ListVotacionesUsuario.as_view()),
    # path('votaciones/<int:id_encuesta>', views.ListVotacionesEncuesta.as_view()),
    # path('encuestas/<int:id_encuesta>/resultados', views.ResultadosEncuestaList.as_view(),name='encuesta-resultados'),
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
    # path('torneos', views.ListTorneos.as_view(), name="list_torneos"),

    # path('transmisiones', views.ListTransmisiones.as_view(), name="list_transmisiones"),
    # path('transmisiones/<str:fecha_evento>', views.ListTransmisionesPorFecha.as_view()),
    # path('transmisiones_fecha', views.ListTransmisionesEnFecha.as_view(), name="list_transmisiones_fecha"),

    # path('emisora/<int:id_emisora>/transmisiones', views.ListTransmisionesPorEmisora.as_view()),
    # path('transmisionemisora', views.ListTransmisionEmisora.as_view()),

    # path('galeria', views.ListGaleria.as_view(), name="list_galeria"),
    # path('emisora/<int:id_emisora>/galeria', views.ListGaleriaPorEmisora.as_view()),
    # path('galeriaemisora', views.ListGaleriaEmisora.as_view()),

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
