# Generated by Django 3.2.7 on 2022-10-28 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdminRadio', '0016_publicidad_creada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transmision',
            name='plataforma',
        ),
        migrations.RemoveField(
            model_name='transmision',
            name='url',
        ),
        migrations.CreateModel(
            name='PlataformaTransmision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=2080, null=True)),
                ('plataforma', models.CharField(blank=True, max_length=30, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('id_transmision', models.ForeignKey(db_column='id_transimision', on_delete=django.db.models.deletion.CASCADE, to='WebAdminRadio.transmision')),
            ],
        ),
    ]
