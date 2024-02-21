from collections.abc import Mapping

from django import template
from django.template.engine import Engine

register = template.Library()


@register.filter("getattr")
def getattribute(value, arg):
    if hasattr(value, str(arg)):
        return getattr(value, arg)
    elif isinstance(value, Mapping) and arg in value:
        return value[arg]
    elif str(arg).isdigit() and len(value) > int(arg):
        return value[int(arg)]
    else:
        return Engine.get_default().string_if_invalid
