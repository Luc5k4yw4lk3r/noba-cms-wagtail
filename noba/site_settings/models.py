from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(blank=True, null=True, max_length=200, help_text='Facebook URL')
    twitter = models.URLField(blank=True, null=True, max_length=200, help_text='Twitter URL')
    youtube = models.URLField(blank=True, null=True, max_length=200, help_text='Youtube URL')
    instagram = models.URLField(blank=True, null=True, max_length=200, help_text='Instagram URL')
    linkedin = models.URLField(blank=True, null=True, max_length=200, help_text='linkedin URL')
    whatsapp = models.URLField(blank=True, null=True, max_length=200, help_text='Whatsapp URL')
    mail = models.URLField(blank=True, null=True, max_length=200, help_text='Email URL')

    panel = [
        MultiFieldPanel([
            FieldPanel('facebook'),
            FieldPanel('twitter'),
            FieldPanel('youtube'),
            FieldPanel('instagram'),
            FieldPanel('linkedin'),
        ], heading='Social Media Settings')
    ]
