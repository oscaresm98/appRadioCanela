from django.db import models
from accounts.models import Usuario,Rol, Permisos
# Create your models here.

class Auditoria(models.Model):
    accion = models.CharField(max_length=150, blank=True, null=True)
    tabla = models.CharField(max_length=2080, blank=True, null=True)
    data_nueva = models.CharField(max_length=2080, blank=True, null=True)
    data_actual = models.CharField(max_length=2080, blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    estado = models.BooleanField(default=True)


class Concursos(models.Model):
    titulo = models.CharField(max_length=50, blank=True, null=True)
    imagen = models.CharField(max_length=2080, blank=True, null=True)
    link = models.CharField(max_length=2080, blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)


class Equipo(models.Model):
    equipo = models.CharField(max_length=30, blank=True, null=True)
    ciudad = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.CharField(max_length=2080, blank=True, null=True)
    estado = models.BooleanField(default=True)

    def get_redes_sociales_equipo(self):
        return RedSocialEquipo.objects.filter(id_equipo=self.id)

class Locutor(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.CharField(max_length=2080, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(db_column='fecha_Nacimiento', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(default=True)

    def get_redes_sociales_locutor(self):
        return RedSocialLocutor.objects.filter(id_locutor=self.id)



class Notificacion(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(blank=True, null=True)
    hora_envio = models.TimeField(blank=True, null=True)
    envio_correo = models.IntegerField()
    tipo_notificacion = models.CharField(max_length=30)
    tipos_usuarios = models.CharField(max_length=30)
    estado = models.BooleanField(default=True)


class PoliticasPriv(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    url = models.CharField(max_length=2080, blank=True, null=True)
    fecha_creado = models.DateField(blank=True, null=True)
    estado = models.BooleanField(default=True)


class Programa(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=True)
    imagen = models.CharField(max_length=2080, blank=True, null=True)
    estado = models.BooleanField(default=True)
    
    # Esta función retorna todos los horarios del segmento
    def get_horarios(self):
        return Horario.objects.filter(id_programa=self.pk).values('dia','hora_inicio', 'hora_fin')
    
    # Esta función retorna todo 
    def get_emisora(self):
        return SegmentoEmisora.objects.filter(segmento=self.pk).values('emisora')
    
    # Esta función retorna todo 
    def get_locutores(self):
        return Locutor.objects.filter(pk__in=SegmentoLocutor.objects.filter(id_segmento=self.pk).values('id_locutor')).values('id', 'nombre', 'imagen')


class Radio(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.CharField(max_length=2080, blank=True, null=True)
    logotipo = models.CharField(max_length=2080, blank=True, null=True)
    sitio_web = models.CharField(max_length=2080, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)


class RedSocial(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    logo_red_social = models.CharField(max_length=2080, blank=True, null=True)
    estado = models.BooleanField(default=True)


class Suscripcion(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    dias_suscripcion = models.IntegerField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    estado = models.BooleanField(default=True)


class Torneo(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    lugar = models.CharField(max_length=100, blank=True, null=True)
    estado = models.BooleanField(default=True)


class AnunciosRadio(models.Model):
    id_radio = models.ForeignKey(Radio, on_delete=models.CASCADE, db_column='id_radio')
    titulo = models.CharField(max_length=30)
    imagen = models.CharField(max_length=2080, blank=True, null=True)
    estado = models.BooleanField(default=True)


class Compra(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    id_suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE, db_column='id_suscripcion')
    valor_compra = models.FloatField(blank=True, null=True)
    iva = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    fecha_compra = models.DateField(blank=True, null=True)


class Emisora(models.Model):
    # id = models.IntegerField(primary_key=True, null=False)
    id_radio = models.ForeignKey(Radio, on_delete=models.CASCADE, db_column='id_radio')
    frecuencia_dial = models.CharField(max_length=30, blank=True, null=True)
    tipo_frecuencia = models.CharField(max_length=30, blank=True, null=True)
    slug = models.SlugField(unique=True, null=True)
    url_streaming = models.CharField(max_length=2080, blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    ciudad = models.CharField(max_length=30, blank=True, null=True)
    provincia = models.CharField(max_length=30, blank=True, null=True)
    estado = models.BooleanField(default=True)


class Encuesta(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.CharField(max_length=2080, blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    dia_inicio = models.DateField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    dia_fin = models.DateField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    id_emisora = models.ForeignKey(Radio, on_delete=models.CASCADE, db_column='id_emisora', blank=True, null=True)


class Pregunta(models.Model):
    titulo = models.CharField(max_length=150)
    id_encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, db_column='id_encuesta')


class Favorito(models.Model):
    id_segmento = models.ForeignKey(Programa, on_delete=models.CASCADE, db_column='id_segmento')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')


class Galeria(models.Model):
    id_emisora = models.ForeignKey(Emisora, on_delete=models.CASCADE, db_column='id_emisora')
    nombre = models.CharField(max_length=30)
    imagen = models.CharField(max_length=2080, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)

    def get_imagenes_videos_galeria(self):
        return VideoImagen.objects.filter(id_galeria=self.id)

class Hilochat(models.Model):
    id_emisora = models.ForeignKey(Emisora, on_delete=models.CASCADE, db_column='id_emisora')
    dia = models.CharField(max_length=10, blank=True, null=True)


class Horario(models.Model):
    id_programa = models.ForeignKey(Programa, on_delete=models.CASCADE, db_column='id_programa')
    dia = models.CharField(max_length=9)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    
    # Esta función retorna todo 
    def get_programa(self):
        return Programa.objects.filter(id=self.id_programa.id).values('nombre', 'descripcion', 'imagen')


class Mensajechat(models.Model):
    mensaje = models.TextField()
    fecha_hora_envia = models.DateTimeField()
    id_hilochat = models.ForeignKey(Hilochat, on_delete=models.CASCADE, db_column='id_hilochat')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')


class NoticiasTips(models.Model):
    id_emisora = models.ForeignKey(Emisora, on_delete=models.CASCADE, db_column='id_emisora')
    titulo = models.CharField(max_length=300)
    fecha_subida = models.DateTimeField(blank=True, null=True)
    imagen = models.CharField(max_length=2080, blank=True, null=True)
    likes = models.IntegerField(default=0)
    compartidos = models.IntegerField(default=0)
    visualizacion = models.IntegerField(default=0)
    tipo = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    estado = models.BooleanField(default=True)
    
    def get_radio(self):
        return f"{self.id_emisora.id_radio.nombre} {self.id_emisora.frecuencia_dial}"


class OpcionPregunta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    enunciado = models.TextField()
    numero_votos = models.IntegerField(blank=True, null=True)


class PartidoTransmision(models.Model):
    # id_emisora = models.ForeignKey(Emisora, on_delete=models.CASCADE, db_column='id_emisora')
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, db_column='id_torneo')
    id_equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, db_column='id_equipo_local', related_name='equipolocal')
    id_equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, db_column='id_equipo_visitante', related_name='equipovisitante')
    hora_inicio = models.TimeField(blank=True, null=True)
    fecha_evento = models.DateTimeField(blank=True, null=True)
    lugar = models.CharField(max_length=50, blank=True, null=True)
    estadio= models.CharField(max_length=100, blank=True, null=True, default='')
    descripcion = models.TextField(blank=True, null=True)
    marcador = models.CharField(max_length=20, blank=True, null=True)
    ptos_equipo_local = models.SmallIntegerField(blank=True, null=True)
    ptos_equipo_visitante = models.SmallIntegerField(blank=True, null=True)
    url_partido = models.CharField(max_length=2080, blank=True, null=True)
    plataforma = models.CharField(max_length=30, blank=True, null=True)
    estado = models.BooleanField(default=True)

    def get_emisoras(self):
        id_emisoras = PartidoTransmisionEmisora.objects.filter(id_partido=self.pk).values('id_emisora')
        return Emisora.objects.filter(pk__in=id_emisoras)

    def get_equipo_local(self):
        return Equipo.objects.filter(id=self.id_equipo_local)
    
    def get_equipo_visitante(self):
        return Equipo.objects.filter(id=self.id_equipo_visitante)

class PartidoTransmisionEmisora(models.Model):
    id_partido = models.ForeignKey(PartidoTransmision, on_delete=models.CASCADE, db_column='id_partido')
    id_emisora = models.ForeignKey(Emisora, on_delete=models.CASCADE, db_column='id_emisora')

class Podcast(models.Model):
    id_emisora = models.ForeignKey(Emisora, on_delete=models.CASCADE, db_column='id_emisora')
    nombre = models.CharField(max_length=30)
    autores = models.CharField(max_length=30)
    audio = models.CharField(max_length=2080, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    imagen = models.CharField(max_length=2080, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)
    estado = models.BooleanField(default=True)


class Publicidad(models.Model):
    id_radio = models.ForeignKey(Radio, on_delete=models.CASCADE, db_column='id_radio')
    titulo = models.CharField(max_length=30, blank=True, null=True)
    cliente = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.CharField(max_length=2080, blank=True, null=True)
    url = models.CharField(max_length=2080, blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    creada = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)


class RedSocialEmisora(models.Model):
    id_emisora = models.OneToOneField(Emisora, on_delete=models.CASCADE, db_column='id_emisora', primary_key=True)
    id_red_social = models.ForeignKey(RedSocial, on_delete=models.CASCADE, db_column='id_red_social')
    username = models.CharField(max_length=30, blank=True, null=True)
    link = models.CharField(max_length=2080, blank=True, null=True)


class RedSocialEquipo(models.Model):
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, db_column='id_equipo')
    id_red_social = models.ForeignKey(RedSocial, on_delete=models.CASCADE, db_column='id_red_social')
    link = models.CharField(max_length=2080, blank=True, null=True)
    estado = models.BooleanField(default=True)
    username = models.CharField(max_length=30, blank=True, null=True)


class RedSocialLocutor(models.Model):
    id_locutor = models.ForeignKey(Locutor, on_delete=models.CASCADE, db_column='id_locutor')
    id_red_social = models.ForeignKey(RedSocial, on_delete=models.CASCADE, db_column='id_red_social')
    username = models.CharField(max_length=150, blank=True, null=True)
    estado = models.BooleanField(default=True)
    link = models.CharField(max_length=2080, blank=True, null=True)


class SegmentoEmisora(models.Model):
    emisora = models.ForeignKey(Emisora, on_delete=models.CASCADE, blank=True, null=True)
    segmento = models.ForeignKey(Programa, on_delete=models.CASCADE, blank=True, null=True)


class SegmentoLocutor(models.Model):
    id_segmento = models.ForeignKey(Programa, on_delete=models.CASCADE, db_column='id_segmento')
    id_locutor = models.ForeignKey(Locutor, on_delete=models.CASCADE, db_column='id_locutor')

    def get_locutores(fk):
        listrelations = SegmentoLocutor.objects.filter(id_segmento=fk).values('id_locutor')
        locutores = []
        for i in range(len(listrelations)):
            id = listrelations[i]['id_locutor']
            locutores.append(Locutor.objects.get(id=id))
        return locutores


class SugerenciaReclamos(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario', blank=True, null=True)
    id_radio = models.ForeignKey(Radio, on_delete=models.CASCADE, db_column='id_radio', blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    fecha_envio = models.DateTimeField(blank=True, null=True)
    archivo = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    tipo = models.CharField(max_length=30, blank=True, null=True)


class TelefonoEmisora(models.Model):
    id_emisora = models.ForeignKey(Emisora, on_delete=models.CASCADE, db_column='id_emisora')
    telefono = models.CharField(max_length=15, blank=True, null=True)
    estado = models.BooleanField(default=True)


class Transmision(models.Model):
    id_emisora = models.ForeignKey(Emisora, on_delete=models.CASCADE, db_column='id_emisora')
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    
    def get_plataforma(self):
        return PlataformaTransmision.objects.filter(id_transmision=self.pk).values('url', 'plataforma')


class PlataformaTransmision(models.Model):
    id_transmision = models.ForeignKey(Transmision, on_delete=models.CASCADE, db_column='id_transimision')
    url = models.CharField(max_length=2080, blank=True, null=True)
    plataforma = models.CharField(max_length=30, blank=True, null=True)
    estado = models.BooleanField(default=True)


class UsuarioConcursos(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    id_concurso = models.ForeignKey(Concursos, on_delete=models.CASCADE, db_column='id_concurso')


class UsuarioEncuesta(models.Model):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, db_column='encuesta')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='usuario')
    fecha = models.DateTimeField(blank=True, null=True)


class UsuariosNotificacion(models.Model):
    id_notificacion = models.OneToOneField(Notificacion, on_delete=models.CASCADE, db_column='id_notificacion', primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')


class VideoImagen(models.Model):
    id_galeria = models.ForeignKey(Galeria, on_delete=models.CASCADE, db_column='id_galeria')
    fecha_creacion = models.DateTimeField()
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=300)
    likes = models.IntegerField()
    tipo = models.CharField(max_length=20, blank=True, null=True)
    estado = models.BooleanField(default=True)
