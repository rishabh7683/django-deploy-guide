from django import template

register = template.Library()
@register.filter(name='cut')
# basically the above line is decorator , instead of this u can use the last line of this py file which is commented
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg,'')

# register.filter('cut',cut)
