# Generated by Django 3.2 on 2024-08-13 11:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0008_auto_20240809_1613'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favourite',
            new_name='Favorite',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='rescipes/images/', verbose_name='Изображение'),
        ),
    ]