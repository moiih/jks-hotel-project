from django import template


register = template.Library()

@register.filter
def check_oddeve(count):
    if count%2 == 0:
        return 0
    else:
        return 1