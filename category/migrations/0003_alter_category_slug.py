# Generated by Django 5.2.4 on 2025-07-21 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='default-slug', max_length=200, unique=True),
        ),
    ]
