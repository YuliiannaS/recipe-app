from django.test import TestCase
from .models import Ingredient

class IngredientModelTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        Ingredient.objects.create(name="Flour", description="Used for baking")

    def test_ingredient_creation(self):
        """Tests that the ingredient creation works and stores data correctly."""
        flour = Ingredient.objects.get(name="Flour")
        self.assertEqual(flour.name, "Flour")
        self.assertEqual(flour.description, "Used for baking")

    def test_string_representation(self):
        """Test the string representation of the Ingredient."""
        flour = Ingredient.objects.get(name="Flour")
        self.assertEqual(str(flour), flour.name)

