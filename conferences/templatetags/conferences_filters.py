from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.filter
def is_current_page(request, param):
    params = param.split(',')
    name = params[0]
    kwargs = {k:v for k,v in (x.split('=') for x in params[1:]) }
    if kwargs:
        return request.path == reverse(name, kwargs=kwargs)
    else:
        return request.path == reverse(name)
