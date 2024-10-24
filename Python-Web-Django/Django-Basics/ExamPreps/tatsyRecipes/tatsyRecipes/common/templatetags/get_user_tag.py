from django import template

from tatsyRecipes.utils.get_user import get_user

register = template.Library()

@register.simple_tag
def get_user_tag():
    return get_user()