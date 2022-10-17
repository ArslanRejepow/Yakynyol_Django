
from django import template
register = template.Library()

@register.filter(name='split')
def split(value):
    """
        Returns the value turned into a list.
    """
    return value.split('/')[-1:][0]

@register.filter(name='spliturl')
def spliturl(value):
    """
        Returns the value turned into a list.
    """
    return value.split('/')[1]