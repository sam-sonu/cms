from cms.models.pluginmodel import CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from colorful.fields import RGBColorField


class UpcomingEventsModel(CMSPlugin):
    event_day = models.CharField(max_length=1000)
    event_date = models.CharField(max_length=1000)
    event_title = models.CharField(max_length=1000)
    event_time = models.CharField(max_length=1000)
    event_description = HTMLField(max_length=1000)
    event_font_color = RGBColorField(('Font Color'), blank=True, default='#fff',
                                    help_text=('Choose the desired font color.'))
    event_card_shadow_color = RGBColorField(('Shadow Color'), blank=True, default='#fff',
                                    help_text=('Choose the desired Shadow color.'))
    event_card_color = RGBColorField(('Card Color'), blank=True, default='#fff',
                                    help_text=('Choose the desired Card color.'))
    event_image = models.ImageField(upload_to='media/events_images', null=True, blank=True)

    @property
    def color_background_exist(self):
        return self.event_font_color and not self.event_font_color == '#ffffff'
    
    def delete(self, *args, **kwargs):
        # Perform any necessary cleanup here
        super().delete(*args, **kwargs)

    def __str__(self): 
        return "Upcoming Events "