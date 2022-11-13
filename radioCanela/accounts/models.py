from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser, Group
from enum import Enum

# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=15, unique=True)
    descripcion = models.CharField(max_length=500)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.nombre

class Permisos(models.Model):
    id_rol = models.ForeignKey(Rol,on_delete=models.CASCADE, db_column='id_rol', blank=True, null=True)
    nombre = models.CharField(max_length=35)
    ver = models.BooleanField(default=False)
    agregar = models.BooleanField(default=False)
    actualizar = models.BooleanField(default=False)
    borrar = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)


OPCIONES_INGRESO = (
    ('email', 'EMAIL'),
    ('google', 'GOOGLE'),
    ('facebook', 'FACEBOOK'),
    ('apple', 'APPLE'),
)

class RolGroup(Group):
    """
    Modelo que tiene datos extra de los grupos de permisos
    """
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True, blank=True)

class Usuario(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    sexo = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    cedula = models.CharField(max_length=11, blank=True, null=True)
    slug = models.SlugField(unique=True)
    fechaNacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    foto = models.CharField(max_length=2080, blank=True, null=True)
    metodo_ingreso = models.CharField(max_length=20, choices=OPCIONES_INGRESO, default='email')

    def __str__(self):
        return f'Username: {self.username}' + ' - ' + \
            f'Nombres y Apellidos: {self.first_name} {self.last_name}'    

    def _obtener_permisos_por_grupo(self, grupo: Group):
        """
        Devuelve todos los permisos de un grupo en la siguiente notacion: 
        'nombre_de_app.codigo_permiso'
        """
        return map(lambda permiso: permiso.content_type.app_label + '.' + permiso.codename
            , grupo.permissions.all())

    def has_perm(self, perm, obj=None):
        """
        Sobreescritura del metodo para dar permisos mediante la tabla Groups de Django (Roles)
        """

        # Habilitamos que los super usuarios tengan todos los permisos
        if self.is_active and self.is_superuser:
            return True
        if not self.groups.all():
            return False

        for grupo_perm in self.groups.all():
            # Solo si el permiso requerido esta entre los permisos declarados en el grupo
            if perm in self._obtener_permisos_por_grupo(grupo_perm):
                return True

        return super().has_perm(self, perm)

def create_slug(instance, sender, new_slug=None):
    slug = slugify(instance.username)
    if new_slug is not None:
        slug = new_slug
    qs = sender.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, sender, new_slug=new_slug)
    return slug


@receiver(pre_save, sender=Usuario)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance, sender)