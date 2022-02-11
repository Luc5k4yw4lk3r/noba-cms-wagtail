from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from streams.blocks import TitleAndTextBlock, RichTextBlock, CardBlock, CardIndexBlock, CardIndexHighlightBlock

class BlogPage(Page):

    body = RichTextField(blank=True, help_text='Body information')

    post_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content = StreamField(
        [
            # ('title_and_text', TitleAndTextBlock()),
            ('full_richtext', RichTextBlock()),
        ],
        null=True,
        blank=True,
    )

    blog_cards = StreamField(
        [
            ('card_block', CardBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('post_image'),
        StreamFieldPanel('content'),
        StreamFieldPanel('blog_cards'),
    ]

    # Specifies parent to BlogPage as being BlogIndexPages
    # parent_page_types = ['BlogIndexPage']

    # Specifies what content types can exist as children of BlogPage.
    # Empty list means that no child content types are allowed.
    subpage_types = []


   

class BlogIndexPage(Page):
    title_highlight = RichTextField(blank=True, help_text='Page title')

    blog_cards = StreamField(
        [
            ('card_block', CardIndexBlock()),
        ],
        null=True,
        blank=True,
    )

    blog_highlight_cards = StreamField(
        [
            ('blog_highlight_cards', CardIndexHighlightBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('title_highlight', classname="full"),
        StreamFieldPanel('blog_highlight_cards'),
        StreamFieldPanel('blog_cards'),
    ]