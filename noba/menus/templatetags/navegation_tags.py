from os import link
from django import template
from wagtail.core.models import Page, Site


register = template.Library()


@register.inclusion_tag('menus/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
        ancestors_not_link = []
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=1)
        ancestors_not_link = ancestors.filter(simplepage__link_in_breadcrumbs = False)
    return {
        'ancestors': ancestors,
        'ancestors_not_link': ancestors_not_link,
        'request': context['request'],
    }