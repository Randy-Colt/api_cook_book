# Generated by Django 3.2 on 2024-10-01 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_rename_ingredients_recipe__ingredients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='_ingredients',
            new_name='ingredients',
        ),
    ]
