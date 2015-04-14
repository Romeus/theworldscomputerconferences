from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.filter
def is_current_page(request, param):
    params = param.split(',')
    name = params[0]
    args = params[1:]
    if args:
        return request.path == reverse(name, args=args)
    else:
        return request.path == reverse(name)
