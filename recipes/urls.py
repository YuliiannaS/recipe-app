from django.urls import path
from .views import home, recipe_list, recipe_detail, search_recipes, recipe_charts

urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipes/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('search/', search_recipes, name='search_recipes'),
    path('charts/', recipe_charts, name='recipe_charts'),
]
