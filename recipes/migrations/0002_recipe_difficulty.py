# Generated by Django 5.0.6 on 2024-06-27 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='difficulty',
            field=models.TextField(default='Easy'),
        ),
    ]
