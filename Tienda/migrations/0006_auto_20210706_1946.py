# Generated by Django 2.2.5 on 2021-07-06 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0005_auto_20210706_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='user',
            field=models.OneToOneField(default=12, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
