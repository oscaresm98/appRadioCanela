# Generated by Django 3.2.7 on 2022-09-23 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdminRadio', '0007_auto_20220923_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partidotransmision',
            name='imagen',
        ),
    ]
