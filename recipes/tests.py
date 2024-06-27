from django.test import TestCase
from recipes.models import Recipe

class RecipeModelTest(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(name="Cake", cooking_time=30, ingredients="Flour,Sugar", difficulty="Easy")

    def test_recipe_creation(self):
        """Tests that the recipe is created successfully and relations are set correctly."""
        cake = Recipe.objects.get(name="Cake")
        self.assertEqual(cake.cooking_time, 30)
        self.assertEqual(cake.ingredients, "Flour,Sugar")
        self.assertEqual(cake.difficulty, "Easy")

    def test_string_representation(self):
        """Test the string representation of the Recipe."""
        cake = Recipe.objects.get(name="Cake")
        self.assertEqual(str(cake), cake.name)
