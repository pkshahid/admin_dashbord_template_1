from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
  """Allows to get an item from a dictionary using a variable key in Django templates."""
  if hasattr(dictionary, 'get'):
    return dictionary.get(key)
  return None
