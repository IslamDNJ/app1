# Generated by Django 4.2.16 on 2024-10-23 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_products_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='slur',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='slur',
            new_name='slug',
        ),
    ]
