from django import template
from django.utils.safestring import mark_safe
from marky.markup import convert_markdown

register = template.Library()

@register.filter
def markdown(text):
    return mark_safe(convert_markdown(text))
