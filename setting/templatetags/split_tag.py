
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

@register.filter(name='get_velayats')
def get_velayats(value):
    value = value.replace('1', "balkan").replace('2', "ahal").replace('3', "mary").replace('4', "lebap").replace('5', "dashoguz").replace('6', "ashgabat")
    value = value.split('+')
    print(value)
    return value