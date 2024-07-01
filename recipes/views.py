from django.shortcuts import render, get_object_or_404
from .models import Recipe
from .forms import SearchForm
from django.db.models import Q, Count
from django.urls import reverse
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt
import base64

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes_home.html', {'recipes': recipes, 'year': 2024})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def search_recipes(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        recipes = Recipe.objects.filter(Q(name__icontains=query) | Q(ingredients__icontains=query))
        df = pd.DataFrame(list(recipes.values('id', 'name', 'ingredients','description','image')))
        df['url'] = df['id'].apply(lambda x: reverse('recipe_detail', args=[x]))
        df['name'] = df.apply(lambda row: f'<a href="{row["url"]}">{row["name"]}</a>', axis=1)
        return render(request, 'search/search_results.html', {
            'form': form,
            'dataframe': df[['name', 'ingredients','description','image']].to_html(escape=False, index=False, classes='dataframe'),
        })
    else:
        return render(request, 'search/search_form.html', {'form': form})
    
def recipe_charts(request):
    recipes = Recipe.objects.all()
    ingredient_list = []
    for recipe in recipes:
        ingredient_list.extend(recipe.ingredients.split(', '))
    ingredient_df = pd.Series(ingredient_list).value_counts().head(10)

    plt.figure(figsize=(10, 5))
    ingredient_df.plot(kind='bar')
    plt.title('Most Popular Ingredients')
    plt.xlabel('Ingredients')
    plt.ylabel('Number of Recipes')
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    bar_graph = base64.b64encode(buf.getvalue()).decode('utf-8')

    difficulty_counts = Recipe.objects.values_list('difficulty').annotate(total=Count('difficulty'))
    difficulty_df = pd.DataFrame(list(difficulty_counts), columns=['Difficulty', 'Total'])

    plt.figure(figsize=(8, 8))
    plt.pie(difficulty_df['Total'], labels=difficulty_df['Difficulty'], autopct='%1.1f%%')
    plt.title('Recipe Distribution by Difficulty')
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    pie_chart = base64.b64encode(buf.getvalue()).decode('utf-8')

    return render(request, 'recipes/recipe_charts.html', {'bar_graph': bar_graph, 'pie_chart': pie_chart})