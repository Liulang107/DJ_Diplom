# Generated by Django 2.2.5 on 2019-11-17 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('created',), 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
