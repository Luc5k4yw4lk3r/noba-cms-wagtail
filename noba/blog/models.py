from django.db import models
from django import forms

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.admin.edit_handlers import (
    FieldPanel, 
    InlinePanel ,
    PageChooserPanel, 
    StreamFieldPanel, 
    MultiFieldPanel
)
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from streams.blocks import (
    TitleAndTextBlock, 
    RichTextBlock, 
    CardBlock, 
    CardIndexBlock, 
    CardIndexHighlightBlock,
    CardEntrepreneurBlock,
    CardValueBlock,
    CardTeamMemberBlock,
    CardApproachBlock
)


class BlogAuthorsOrderable(Orderable):
    
    page = ParentalKey('blog.BlogPage', related_name='blog_authors')
    author = models.ForeignKey(
        'blog.BlogAuthor',
        on_delete=models.CASCADE,
    )

    panels = [
        SnippetChooserPanel('author')
    ]

class BlogAuthor(models.Model):
    """ Blog authors"""
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='+'
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('name'),
                ImageChooserPanel('image'),
            ],  heading="Name and Image",
        ),
        MultiFieldPanel(
            [
                FieldPanel('website'),
            ],  heading="Links",
        )
    ]

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Blog Author'
        verbose_name_plural = 'Blog Authors'

register_snippet(BlogAuthor)


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    panels = [
        FieldPanel('name')
    ]

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'

register_snippet(BlogCategory)


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

    category = ParentalManyToManyField('blog.BlogCategory', blank=True)

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
        MultiFieldPanel([
            InlinePanel('blog_authors', label='Author', min_num=0, max_num=4)
        ], heading='Author(s)'
        ),
        MultiFieldPanel([
            FieldPanel('category', widget=forms.CheckboxSelectMultiple)
        ], heading='Categories'
        ),
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


class EntrepreneurPage(Page):

    body = RichTextField(blank=True, help_text='Body information')

    card_entrepreneur_block = StreamField(
        [
            ('card_entrepreneur_block', CardEntrepreneurBlock()),
        ],
        null=True,
        blank=True,
    )

    orange = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('orange', classname="full"),
        StreamFieldPanel('card_entrepreneur_block'),
    ]

class SimplePage(Page):

    body = RichTextField(blank=True, help_text='Body information')

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class ValuePage(Page):

    body = RichTextField(blank=True, help_text='Body information')

    footer_title = models.CharField(null=True, blank=True, max_length=250, help_text='Footer Title')

    footer_body = RichTextField(blank=True, help_text='Footer Body information')

    card_value_block = StreamField(
        [
            ('card_value_block', CardValueBlock()),
        ],
        null=True,
        blank=True,
    )

    card_team_member_block = StreamField(
        [
            ('card_team_member_block', CardTeamMemberBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('footer_title', classname="full"),
        FieldPanel('footer_body', classname="full"),
        StreamFieldPanel('card_value_block'),
        StreamFieldPanel('card_team_member_block'),
    ]


class ApproachPage(Page):

    body = RichTextField(blank=True, help_text='Body information')

    card_approach_block = StreamField(
        [
            ('card_approach_block', CardApproachBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('card_approach_block', classname="full"),
    ]

