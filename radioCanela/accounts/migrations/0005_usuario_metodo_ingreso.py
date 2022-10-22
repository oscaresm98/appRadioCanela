# Generated by Django 3.2.7 on 2022-10-22 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_permisos_id_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='metodo_ingreso',
            field=models.CharField(choices=[('email', 'EMAIL'), ('google', 'GOOGLE'), ('facebook', 'FACEBOOK'), ('apple', 'APPLE')], default='email', max_length=20),
        ),
    ]
