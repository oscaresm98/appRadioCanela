# Generated by Django 3.2.7 on 2022-12-14 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdminRadio', '0021_auto_20221213_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encuesta',
            old_name='dia_fin',
            new_name='fecha_hora_fin',
        ),
        migrations.RenameField(
            model_name='encuesta',
            old_name='dia_inicio',
            new_name='fecha_hora_inicio',
        ),
        migrations.RemoveField(
            model_name='encuesta',
            name='hora_fin',
        ),
        migrations.RemoveField(
            model_name='encuesta',
            name='hora_inicio',
        ),
    ]