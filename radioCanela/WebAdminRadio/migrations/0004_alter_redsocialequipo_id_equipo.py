# Generated by Django 3.2.7 on 2022-09-21 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdminRadio', '0003_auto_20220921_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redsocialequipo',
            name='id_equipo',
            field=models.ForeignKey(db_column='id_equipo', on_delete=django.db.models.deletion.CASCADE, to='WebAdminRadio.equipo'),
        ),
    ]
