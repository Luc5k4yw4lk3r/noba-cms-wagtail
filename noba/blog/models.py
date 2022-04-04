from random import randint
from django import forms
from django.db.models.aggregates import Count
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from streams.blocks import (CardApproachBlock, CardBlock,
                            CardEntrepreneurBlock, CardIndexBlock,
                            CardIndexHighlightBlock, CardTeamMemberBlock,
                            CardValueBlock, RichTextBlock, TitleAndTextBlock)
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel,
                                         MultiFieldPanel, PageChooserPanel,
                                         StreamFieldPanel)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet


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


class BlogColor(models.Model):
    name = models.CharField(max_length=100, help_text='Name')
    style = models.CharField(max_length=100, help_text='Css style to apply in code')

    panels = [
        FieldPanel('name'),
        FieldPanel('style')
    ]

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Blog Color'
        verbose_name_plural = 'Blog Colors'


register_snippet(BlogColor)


class Footer(models.Model):
    title = models.CharField(max_length=100, default='')
    slug = models.SlugField(max_length=100, default='')
    form_description = models.CharField(max_length=350, help_text='Formt descripcion')
    term_and_conditions = RichTextField(max_length=350, help_text='Term and conditions')
    location = RichTextField(max_length=350, help_text='Location info')
    low_description = RichTextField(max_length=350, help_text='Location info')

    panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
        FieldPanel('form_description'),
        FieldPanel('term_and_conditions'),
        FieldPanel('location'),
        FieldPanel('low_description')
    ]

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footers'


register_snippet(Footer)


class BlogPage(Page):

    title_screen = models.CharField(max_length=250, default='')
    body = RichTextField(blank=True, help_text='Body information')
    title_card = models.CharField(max_length=250, default='', help_text='Title for the card')
    description_card = models.CharField(max_length=250, default='', help_text='Title for the card')
    reading_time = models.CharField(max_length=50, default='', help_text='Time reading.')
    publication_date = models.DateTimeField(
        verbose_name=('publication date'),
        null=True,
        blank=True,
        help_text='The date is displayed on the screen. If it is empty, '
        'the last date of publication will be displayed.'
    )
    post_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Image for title'
    )

    post_image_thumb = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Image for post item.'
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

    color = ParentalManyToManyField('blog.BlogColor', blank=True)

    blog_cards_automatics = models.BooleanField(
        default=True,
        help_text='If this is true, a set of items will be randomly selected.')

    blog_items_quantity = models.IntegerField(default=3, help_text='Post items quantity')

    blog_cards = StreamField(
        [
            ('card_block', CardBlock()),
        ],
        null=True,
        blank=True,
    )

    blog_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Choose a page to link to your blog page',
    )

    def publication_date_value(self):
        if self.publication_date:
            return self.publication_date
        return self.last_published_at

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # all_academy_posts = BlogPage.objects.live().public().filter(category__name="Academy").order_by('-first_published_at')[:self.blog_highlight_items_quantity]
        all_regular_posts = BlogPage.objects.live().public().filter(
            category__name="Blog regular")
        paginator = Paginator(all_regular_posts, self.blog_items_quantity)
        random_index = randint(1, paginator.num_pages)
        # page = request.GET.get('page')
        page = random_index
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        # context['posts_academy'] = all_academy_posts
        context['posts_regular'] = posts
        return context

    content_panels = Page.content_panels + [
        FieldPanel('title_screen', classname="full"),
        FieldPanel('title_card'),
        FieldPanel('description_card'),
        FieldPanel('body', classname="full"),
        FieldPanel('reading_time'),
        FieldPanel('publication_date'),
        PageChooserPanel('blog_link'),
        ImageChooserPanel('post_image'),
        ImageChooserPanel('post_image_thumb'),
        StreamFieldPanel('content'),
        MultiFieldPanel([
            FieldPanel('blog_cards_automatics'),
            FieldPanel('blog_items_quantity'),
            StreamFieldPanel('blog_cards')
        ], heading='Blog card(s)'
        ),
        MultiFieldPanel([
            InlinePanel('blog_authors', label='Author', min_num=0, max_num=4)
        ], heading='Author(s)'
        ),
        MultiFieldPanel([
            FieldPanel('category', widget=forms.CheckboxSelectMultiple)
        ], heading='Categories'
        ),
        MultiFieldPanel([
            FieldPanel('color', widget=forms.CheckboxSelectMultiple)
        ], heading='Colors'
        ),
    ]

    # Specifies parent to BlogPage as being BlogIndexPages
    # parent_page_types = ['BlogIndexPage']

    # Specifies what content types can exist as children of BlogPage.
    # Empty list means that no child content types are allowed.
    subpage_types = []


class BlogIndexPage(Page):
    title_screen = models.CharField(max_length=250, default='')
    title_highlight = models.CharField(max_length=250, blank=True, help_text='Page title')
    title_card = models.CharField(max_length=250, default='', help_text='Title for the card')
    blog_items_quantity = models.IntegerField(default=1, help_text='Post items quantity')
    blog_highlight_items_quantity = models.IntegerField(default=1, help_text='Post highlight items quantity')

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
        FieldPanel('title_screen'),
        FieldPanel('title_highlight'),
        FieldPanel('title_card'),
        FieldPanel('blog_highlight_items_quantity'),
        FieldPanel('blog_items_quantity'),
        # StreamFieldPanel('blog_highlight_cards'),
        # StreamFieldPanel('blog_cards'),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        all_academy_posts = BlogPage.objects.live().public().filter(category__name="Academy").order_by('-first_published_at')[:self.blog_highlight_items_quantity]
        all_regular_posts = BlogPage.objects.live().public().filter(category__name="Blog regular").order_by('-first_published_at')
        paginator = Paginator(all_regular_posts, self.blog_items_quantity)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context['posts_academy'] = all_academy_posts
        context['posts_regular'] = posts
        return context


class EntrepreneurPage(Page):
    title_screen = models.CharField(max_length=250, default='')

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
        FieldPanel('title_screen', classname="full"),
        FieldPanel('body', classname="full"),
        FieldPanel('orange', classname="full"),
        StreamFieldPanel('card_entrepreneur_block'),
    ]


class SimplePage(Page):
    title_screen = models.CharField(max_length=250, default='')
    body = RichTextField(blank=True, help_text='Body information')
    link_in_breadcrumbs = models.BooleanField(default=True, help_text='This option allow to set this page linkeable or not in breadcrumbs')

    content_panels = Page.content_panels + [
        FieldPanel('title_screen', classname="full"),
        FieldPanel('body', classname="full"),
        FieldPanel('link_in_breadcrumbs'),
    ]


class ValuePage(Page):
    title_screen = models.CharField(max_length=250, default='')

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
        FieldPanel('title_screen', classname="full"),
        FieldPanel('body', classname="full"),
        FieldPanel('footer_title', classname="full"),
        FieldPanel('footer_body', classname="full"),
        StreamFieldPanel('card_value_block'),
        StreamFieldPanel('card_team_member_block'),
    ]


class ApproachPage(Page):
    title_screen = models.CharField(max_length=250, default='')

    body = RichTextField(blank=True, help_text='Body information')

    card_approach_block = StreamField(
        [
            ('card_approach_block', CardApproachBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('title_screen', classname="full"),
        FieldPanel('body', classname="full"),
        StreamFieldPanel('card_approach_block'),
    ]
