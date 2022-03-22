from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from streams.blocks import (CardApproachBlock, CardBlock, CardCompaniesBlock,
                            CardEntrepreneurBlock, CardIndexBlock,
                            CardIndexHighlightBlock, CardTeamMemberBlock,
                            CardValueBlock, RichTextBlock, TitleAndTextBlock)
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel,
                                         MultiFieldPanel, PageChooserPanel,
                                         StreamFieldPanel)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from blog.models import BlogPage

class HomePage(Page):
    body = RichTextField(blank=True)
   
    intial_section = models.BooleanField(default=False)
    video_section = models.BooleanField(default=False)
    knowledge_section = models.BooleanField(default=False)
    approach_section = models.BooleanField(default=False)
    entrepreneur_section = models.BooleanField(default=False)

    company_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Choose a page to link your company page',
    )
    entrepreneurs_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Choose a page to link your entrepreneurs page',
    )
    about_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Choose a page to link your about page',
    )
    blog_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Choose a page to link your about page',
    )

    about_section = models.BooleanField(default=False)
    resources_section = models.BooleanField(default=False)

    approach_title = models.CharField(null=True, blank=True, max_length=250, help_text='Approach Title')
    approach_body = RichTextField(blank=True)

    about_title = models.CharField(null=True, blank=True, max_length=250, help_text='About Title')
    about_body = RichTextField(blank=True)

    resources_title = models.CharField(null=True, blank=True, max_length=250, help_text='About Title')
    resources_body = RichTextField(blank=True)
    title_highlight = models.CharField(max_length=250, blank=True, help_text='Page title')
    title_card = models.CharField(max_length=250, default='', help_text='Title for the card')
    blog_items_quantity = models.IntegerField(default=1, help_text='Post items quantity')
    blog_highlight_items_quantity = models.IntegerField(default=1, help_text='Post highlight items quantity')

    modal_privacy_policy_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Choose a page to link your privacy policy',
    )

    card_companies_block = StreamField(
        [
            ('card_companies_block', CardCompaniesBlock()),
        ],
        null=True,
        blank=True,
    )

    card_approach_block = StreamField(
        [
            ('card_approach_block', CardApproachBlock()),
        ],
        null=True,
        blank=True,
    )

    card_entrepreneurs_block = StreamField(
        [
            ('card_entrepreneurs_block', CardCompaniesBlock()),
        ],
        null=True,
        blank=True,
    )

    blog_cards = StreamField(
        [
            ('blog_block', CardIndexBlock()),
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

    card_team_member_block = StreamField(
        [
            ('card_team_member_block', CardTeamMemberBlock()),
        ],
        null=True,
        blank=True,
    )

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        all_academy_posts = BlogPage.objects.live().public().filter(category__name="Academy").order_by('-first_published_at')[:self.blog_highlight_items_quantity]
        all_regular_posts = BlogPage.objects.live().public().filter(category__name="Blog regular").order_by('-first_published_at')
        regular_posts_qt = all_regular_posts.count()
        entrepreneurs_qt = len(context['page'].entrepreneurs_link.entrepreneurpage.card_entrepreneur_block.raw_data[0]['value']['cards'])
        companies_qt = len(context['page'].company_link.entrepreneurpage.card_entrepreneur_block.raw_data[0]['value']['cards'])
        team_qt = len(context['page'].about_link.valuepage.card_team_member_block.raw_data[0]['value']['cards'])
        paginator = Paginator(all_regular_posts, self.blog_items_quantity)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context['posts_academy'] = all_academy_posts
        context['regular_posts_qt'] = regular_posts_qt
        context['entrepreneurs_qt'] = entrepreneurs_qt
        context['companies_qt'] = companies_qt
        context['team_qt'] = team_qt
        context['posts_regular'] = posts
        return context

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intial_section'),
            FieldPanel('body'),
            PageChooserPanel('modal_privacy_policy_link'),
        ], heading='Initial Section'
        ),
        MultiFieldPanel([
            FieldPanel('video_section'),
        ], heading='Video Section'
        ),
        MultiFieldPanel([
            FieldPanel('knowledge_section'),
        ], heading='Knowledge Section'
        ),
        MultiFieldPanel([
            FieldPanel('approach_section'),
            FieldPanel('approach_title'),
            FieldPanel('approach_body'),
            StreamFieldPanel('card_approach_block'),
        ], heading='Approach Section'
        ),
        MultiFieldPanel([
            FieldPanel('entrepreneur_section'),
            PageChooserPanel('company_link'),
            PageChooserPanel('entrepreneurs_link'),
            StreamFieldPanel('card_companies_block'),
            StreamFieldPanel('card_entrepreneurs_block'),
        ], heading='Entrepreneur Section'
        ),
        MultiFieldPanel([
            FieldPanel('about_section'),
            FieldPanel('about_title'),
            FieldPanel('about_body'),
            PageChooserPanel('about_link'),
            StreamFieldPanel('card_team_member_block'),
        ], heading='About Section'
        ),
        MultiFieldPanel([
            FieldPanel('resources_section'),
            PageChooserPanel('blog_link'),
            FieldPanel('resources_title'),
            FieldPanel('resources_body'),
            FieldPanel('title_highlight'),
            FieldPanel('blog_highlight_items_quantity'),
            FieldPanel('title_card'),
            FieldPanel('blog_items_quantity'),
        ], heading='Resources Section'
        ),
    ]
