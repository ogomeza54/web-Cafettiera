# Generated by Django 3.0.7 on 2020-06-13 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200613_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pages',
            options={'ordering': ['title'], 'verbose_name': 'página', 'verbose_name_plural': 'páginas'},
        ),
    ]
