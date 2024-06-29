from django.shortcuts import render, get_object_or_404
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes_home.html', {'recipes': recipes, 'year': 2024})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})