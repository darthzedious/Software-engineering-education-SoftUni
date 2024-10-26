from django import forms

from tatsyRecipes.mixins import PlaceholderMixin
from tatsyRecipes.recipe_app.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author',]

        widgets = {
            'ingredients': forms.Textarea(attrs={'placeholder': "ingredient1, ingredient2, ..."}),
            'instructions': forms.Textarea(attrs={'placeholder': "Enter detailed instructions here..."}),
            'image_url': forms.TextInput(attrs={'placeholder': "Optional image URL here..."}),
        }

        labels = {
            'cuisine_type': 'Cuisine Type:',
            'cooking_time': 'Cooking Time:',
            'image_url': 'Image URL:',
        }

class EditRecipeForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author', ]