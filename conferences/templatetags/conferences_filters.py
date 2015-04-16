from django import template
from django.core.urlresolvers import resolve

register = template.Library()

@register.filter
def is_current_page(request, view_name):
    return resolve(request.path).url_name == view_name
