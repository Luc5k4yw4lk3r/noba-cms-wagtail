from email.policy import default
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    title =  blocks.CharBlock(required=True, help_text='Add your title')
    text =  blocks.TextBlock(required=True, help_text='Add your additional text')

    class Meta:
        template = 'streams/title_and_text_block.html'
        icon = 'edit'
        label = 'Title & Text'


class RichTextBlock(blocks.RichTextBlock):
    
    class Meta:
        template = 'streams/rich_text_block.html'
        icon = 'edit'
        label = 'Full RichText'


class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add your title')

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock()),
                ('title', blocks.CharBlock(required=True, max_length=60, help_text='Add your card title')),
                ('text', blocks.TextBlock(required=True, max_length=200)),
                ('link_page', blocks.PageChooserBlock(required=False)),
                ('link_external', blocks.URLBlock(required=False, help_text='If link page is not selected It will be applied'))
            ]
        )
    )

    class Meta:
        template = 'streams/card_block.html'
        icon = 'placeholder'
        label = 'Blog Cards'


class CardIndexBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add your title')

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock()),
                ('title', blocks.CharBlock(required=True, max_length=60, help_text='Add your card title')),
                ('text', blocks.TextBlock(required=True, max_length=200)),
                ('link_page', blocks.PageChooserBlock(required=False)),
                ('link_external', blocks.URLBlock(required=False, help_text='If link page is not selected It will be applied'))
            ]
        )
    )

    class Meta:
        template = 'streams/card_index_block.html'
        icon = 'placeholder'
        label = 'Blog Cards'


class CardIndexHighlightBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add your title')

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('title', blocks.CharBlock(required=True, max_length=60, help_text='Add your card title')),
                ('text', blocks.TextBlock(required=True, max_length=200)),
                ('link_page', blocks.PageChooserBlock(required=False)),
                ('link_external', blocks.URLBlock(required=False, help_text='If link page is not selected It will be applied'))
            ]
        )
    )

    class Meta:
        template = 'streams/card_index_highlight_block.html'
        icon = 'placeholder'
        label = 'Blog Highlight Cards'


class CardEntrepreneurBlock(blocks.StructBlock):

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('title', blocks.CharBlock(required=True, max_length=60, help_text='Add your card title')),
                ('text', blocks.TextBlock(required=True, max_length=200)),
                ('year', blocks.TextBlock(required=True, max_length=200)),
                ('location', blocks.TextBlock(required=True, max_length=200)),
                ('description', blocks.TextBlock(required=False)),
                ('gold', blocks.BooleanBlock(required=False, default=False)),
            ]
        )
    )

    class Meta:
        template = 'streams/card_entrepeneur_block.html'
        icon = 'placeholder'
        label = 'Entrepreneurs Cards'


class CardValueBlock(blocks.StructBlock):

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('title', blocks.CharBlock(required=True, max_length=60, help_text='Add your card title')),
                ('text', blocks.TextBlock(required=True, max_length=200)),
            ]
        )
    )

    class Meta:
        template = 'streams/card_value_block.html'
        icon = 'placeholder'
        label = 'Values Cards'


class CardTeamMemberBlock(blocks.StructBlock):

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('name', blocks.CharBlock(required=True, max_length=60, help_text='Add your card title')),
                ('role', blocks.TextBlock(required=False, max_length=200, default='Founder')),
                ('image', ImageChooserBlock()),
                ('link_page', blocks.PageChooserBlock(required=False)),
                ('link_external', blocks.URLBlock(required=False, help_text='If link page is not selected It will be applied')),
            ]
        )
    )

    class Meta:
        template = 'streams/card_team_member_block.html'
        icon = 'placeholder'
        label = 'Values Cards'


class CardApproachBlock(blocks.StructBlock):

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('title', blocks.CharBlock(required=True, max_length=60, help_text='Add your card title')),
                ('text', blocks.RichTextBlock(required=True, help_text='Add your card text')),
                ('description', blocks.TextBlock(required=True, help_text='Add your card description')),
            ]
        )
    )

    class Meta:
        template = 'streams/card_approach_block.html'
        icon = 'placeholder'
        label = 'Values Cards'


class CardCompaniesBlock(blocks.StructBlock):

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('title', blocks.CharBlock(required=True, max_length=60, help_text='Add your card title')),
                ('text', blocks.TextBlock(required=True, help_text='Add your card text')),
                ('description', blocks.TextBlock(required=True, help_text='Add your card description')),
            ]
        )
    )

    class Meta:
        template = 'streams/card_companies_block.html'
        icon = 'placeholder'
        label = 'Values Cards'


class CardLogoBlocks(blocks.StructBlock):

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock()),
                ('width', blocks.CharBlock(required=True, max_length=60, help_text='Image width value')),
                ('height', blocks.TextBlock(required=True, help_text='Image height value')),
                ('alt', blocks.TextBlock(required=False, help_text='Image description')),
            ]
        )
    )

    class Meta:
        template = 'streams/card_logo_block.html'
        icon = 'placeholder'
        label = 'Logo Cards'


class CardKnowledgeBlocks(blocks.StructBlock):

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('title', blocks.CharBlock(required=True, max_length=60, help_text='Image width value')),
                ('text', blocks.TextBlock(required=True, help_text='Image height value')),
            ]
        )
    )

    class Meta:
        template = 'streams/card_knowledge_block.html'
        icon = 'placeholder'
        label = 'Knowledge Cards'


class QuoteBlocks(blocks.StructBlock):

    text = blocks.TextBlock(required=True, help_text='Text')

    class Meta:
        template = 'streams/quote_block.html'
        icon = 'openquote'
        label = 'Quote'
