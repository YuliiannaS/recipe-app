from django.urls import path
from .views import home, recipe_list, recipe_detail

urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipes/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
]
