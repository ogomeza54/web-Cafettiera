# Generated by Django 3.0.7 on 2020-06-12 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['name'], 'verbose_name': 'enlaces', 'verbose_name_plural': 'enlaces'},
        ),
    ]
