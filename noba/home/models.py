from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

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
    about_section = models.BooleanField(default=False)
    resources_section = models.BooleanField(default=False)


    card_companies_block = StreamField(
        [
            ('card_companies_block', CardCompaniesBlock()),
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

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('video_section', classname="full"),
        FieldPanel('knowledge_section', classname="full"),
        FieldPanel('approach_section', classname="full"),
        StreamFieldPanel('card_companies_block'),
        StreamFieldPanel('card_entrepreneurs_block'),
    ]