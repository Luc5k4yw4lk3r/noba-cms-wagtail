from django import template
from blog.models import Footer

register = template.Library()


@register.simple_tag()
def get_footer(slug):
    return Footer.objects.get(slug=slug)