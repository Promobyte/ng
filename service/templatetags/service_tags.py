from django import template
from service.models import Service

register = template.Library()


@register.simple_tag()
def get_services():
    return Service.objects.all()

register.tag('services', get_services)
