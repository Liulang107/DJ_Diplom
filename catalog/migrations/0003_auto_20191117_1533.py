# Generated by Django 2.2.5 on 2019-11-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20191117_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, verbose_name='Цена'),
        ),
    ]
