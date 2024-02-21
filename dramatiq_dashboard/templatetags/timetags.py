import datetime

from django import template

register = template.Library()


@register.filter("timestamp")
def timestamp(timestamp):
    try:
        return datetime.datetime.fromtimestamp(timestamp / 1e3)
    except ValueError:
        return None
