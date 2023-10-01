from django import template
from datetime import timedelta

register = template.Library()

@register.filter
def format_timedelta_as_days(timedelta_obj):
    if isinstance(timedelta_obj, timedelta):
        return f"{timedelta_obj.days}일"
    return str(timedelta_obj)