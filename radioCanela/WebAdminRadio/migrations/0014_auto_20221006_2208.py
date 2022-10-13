# Generated by Django 3.2.7 on 2022-10-07 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdminRadio', '0013_alter_noticiastips_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='segmentolocutor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='segmentolocutor',
            name='id_segmento',
            field=models.ForeignKey(db_column='id_segmento', on_delete=django.db.models.deletion.CASCADE, to='WebAdminRadio.programa'),
        ),
    ]