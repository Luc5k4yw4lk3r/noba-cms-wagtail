from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.admin.edit_handlers import (
    FieldPanel, 
    InlinePanel ,
    PageChooserPanel, 
    StreamFieldPanel, 
    MultiFieldPanel
)

from streams.blocks import (
    TitleAndTextBlock, 
    RichTextBlock, 
    CardBlock, 
    CardIndexBlock, 
    CardIndexHighlightBlock,
    CardEntrepreneurBlock,
    CardValueBlock,
    CardTeamMemberBlock,
    CardApproachBlock,
    CardCompaniesBlock
)

class HomePage(Page):
    body = RichTextField(blank=True)
    
    video_section = models.BooleanField(default=False)
    knowledge_section = models.BooleanField(default=False)
    approach_section = models.BooleanField(default=False)
    entrepreneur_section = models.BooleanField(default=False)
    about_section = models.BooleanField(default=False)
    resources_section = models.BooleanField(default=False)

    approach_title = models.CharField(null=True, blank=True, max_length=250, help_text='Approach Title')
    approach_body = RichTextField(blank=True)

    about_title = models.CharField(null=True, blank=True, max_length=250, help_text='About Title')
    about_body = RichTextField(blank=True)

    resources_title = models.CharField(null=True, blank=True, max_length=250, help_text='About Title')
    resources_body = RichTextField(blank=True)

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

    content_panels = Page.content_panels + [
        # FieldPanel('body', classname="full"),
        # FieldPanel('video_section', classname="full"),
        # FieldPanel('knowledge_section', classname="full"),
        # FieldPanel('entrepreneur_section', classname="full"),
        # FieldPanel('about_section', classname="full"),
        # FieldPanel('resources_section', classname="full"),
        # FieldPanel('approach_section', classname="full"),
        # StreamFieldPanel('card_companies_block'),
        # StreamFieldPanel('card_approach_block'),
        # StreamFieldPanel('card_entrepreneurs_block'),
        MultiFieldPanel([
            FieldPanel('body'),
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
            StreamFieldPanel('card_companies_block'),
            StreamFieldPanel('card_entrepreneurs_block'),
        ], heading='Entrepreneur Section'
        ),
        MultiFieldPanel([
            FieldPanel('about_section'),
            FieldPanel('about_title'),
            FieldPanel('about_body'),
            StreamFieldPanel('card_team_member_block'),
        ], heading='About Section'
        ),
        MultiFieldPanel([
            FieldPanel('resources_section'),
            FieldPanel('resources_title'),
            FieldPanel('resources_body'),
            StreamFieldPanel('blog_highlight_cards'),
            StreamFieldPanel('blog_cards'),
        ], heading='Resources Section'
        ),
    ]