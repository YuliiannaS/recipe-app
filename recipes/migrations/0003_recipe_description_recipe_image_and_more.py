# Generated by Django 5.0.6 on 2024-06-29 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipes_images/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
