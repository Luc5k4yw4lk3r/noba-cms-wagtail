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