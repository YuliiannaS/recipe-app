from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    cooking_time = models.IntegerField()
    ingredients = models.TextField()
    difficulty = models.TextField(default="Easy")

    def __str__(self):
        return self.name