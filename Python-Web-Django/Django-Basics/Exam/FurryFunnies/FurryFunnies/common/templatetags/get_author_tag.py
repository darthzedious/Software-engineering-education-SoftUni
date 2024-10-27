from django import template
from FurryFunnies.utils.get_profile import get_author_obj

register = template.Library()

@register.simple_tag
def get_author_tag():
    return get_author_obj()