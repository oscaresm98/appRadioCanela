from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(AbstractUser):
    username = models.CharField(max_length=30, blank=True, null=True, unique=True)
    sexo = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    cedula = models.CharField(max_length=11, blank=True, null=True)
    slug = models.SlugField(unique=True)
    fechaNacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    rol = models.CharField(max_length=50, blank=True, null=True)
    foto = models.CharField(max_length=2080, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Rol(models.Model):
    nombre = models.CharField(max_length=15, unique=True)
    descripcion = models.CharField(max_length=500)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


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
