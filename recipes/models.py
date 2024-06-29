from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    cooking_time = models.IntegerField()
    difficulty = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
