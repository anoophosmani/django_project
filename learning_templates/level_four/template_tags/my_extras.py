from django import template

register = template.Library()

@register.filter(name='cut')  #by using decorators,its good to use it.

def cut(value,arg):
    return value.replace(arg,'')

# register.filter('cut',cut) #not using decorators