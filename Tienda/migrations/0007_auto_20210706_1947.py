# Generated by Django 2.2.5 on 2021-07-06 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0006_auto_20210706_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='productos',
        ),
        migrations.RemoveField(
            model_name='carrito',
            name='user',
        ),
    ]
