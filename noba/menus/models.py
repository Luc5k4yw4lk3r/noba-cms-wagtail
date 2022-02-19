from pydoc import pager
from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, 
    InlinePanel ,
    PageChooserPanel, 
    StreamFieldPanel, 
    MultiFieldPanel
)

# Create your models here.
class MenuItem(Orderable):
    link_title = models.CharField(blank=True, null=True, max_length=100)
    link_url = models.CharField(blank=True, null=True, max_length=100)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.CASCADE
    )
    open_in_new_tab = models.BooleanField(default=False)

    page = ParentalKey("Menu", related_name="menu_items")

    panels = [
        FieldPanel('link_title'),
        FieldPanel('link_url'),
        PageChooserPanel('link_page'),
        FieldPanel('open_in_new_tab'),
    ]


@register_snippet
class Menu(ClusterableModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)


    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('slug'),
        ], heading='Menu'
        ),
        InlinePanel("menu_items", label="Menu Items"),
    ]

    def __str__(self) -> str:
        return self.title