# Generated by Django 2.2.5 on 2019-11-17 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='Изображение'),
        ),
    ]
