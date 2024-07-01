from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe
from django.contrib.auth.models import User
from .forms import SearchForm

class RecipeTestCase(TestCase):
    def setUp(self):
        self.recipe1 = Recipe.objects.create(
            name="Chicken Soup", 
            ingredients="Chicken, Water, Salt", 
            description="A warm soothing soup.", 
            difficulty="Easy",
            image="soup.jpg",
            cooking_time=30
        )
        self.recipe2 = Recipe.objects.create(
            name="Beef Stew", 
            ingredients="Beef, Tomato, Potato", 
            description="Rich beef stew.", 
            difficulty="Medium",
            image="stew.jpg",
            cooking_time=120
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes_home.html')
        self.assertContains(response, '2024')

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_list.html')
        expected_recipes = list(Recipe.objects.all())
        self.assertListEqual(list(response.context['recipes']), expected_recipes, "The recipes context should contain the recipes.")


    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe_detail', args=[self.recipe1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_detail.html')
        self.assertContains(response, 'Chicken Soup')

    def test_search_recipes_view_form_valid(self):
        response = self.client.get(reverse('search_recipes'), {'query': 'soup'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Chicken Soup', response.context['dataframe'])

    def test_recipe_charts_view(self):
        response = self.client.get(reverse('recipe_charts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_charts.html')
        self.assertIn('Most Popular Ingredients', str(response.content))
        self.assertIn('Recipe Distribution by Difficulty', str(response.content))

class SearchFormTest(TestCase):
    def test_form_valid(self):
        """ Test the form with valid input """
        form = SearchForm(data={'query': 'chicken'})
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        """ Test the form with empty input which should be invalid """
        form = SearchForm(data={'query': ''})
        self.assertFalse(form.is_valid())

    def test_form_max_length_exceeded(self):
        """ Test the form with input exceeding max_length """
        form = SearchForm(data={'query': 'x' * 101})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['query'][0], 'Ensure this value has at most 100 characters (it has 101).')

    def test_form_label(self):
        """ Test the correct form label is used """
        form = SearchForm()
        self.assertEqual(form.fields['query'].label, 'Search for recipes')