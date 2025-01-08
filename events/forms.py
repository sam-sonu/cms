from colorful.forms import RGBColorField
from colorful.widgets import ColorFieldWidget
from django import forms
from .models import UpcomingEventsModel
from djangocms_text_ckeditor.fields import HTMLField  # Correct import statement

class CustomColorFieldWidget(ColorFieldWidget):
    class Media:
        css = {
            'all': ("colorful/colorPicker.css", 'css/admin/color-widget.css',)
        }
        js = ("colorful/jQuery.colorPicker.js",)

class CardConfigForm(forms.ModelForm):
    """
    Form for configuring event cards.
    """
    event_day = forms.CharField()
    event_date = forms.CharField(max_length=1000)
    event_title = forms.CharField(max_length=1000)
    event_time = forms.CharField(max_length=1000)
    event_description = HTMLField(max_length=1000)
    event_font_color = RGBColorField(widget=CustomColorFieldWidget())
    event_card_shadow_color = RGBColorField(widget=CustomColorFieldWidget())
    event_card_color = RGBColorField(widget=CustomColorFieldWidget())
    event_image = forms.ImageField(required=False)

    class Meta:
        """
        Meta class for the CardConfigForm.
        """
        model = UpcomingEventsModel
        exclude = ("file_version",)
        fields = ['event_day', 'event_date', 'event_title', 'event_time', 'event_description', 'event_font_color', 'event_card_shadow_color', 'event_card_color', 'event_image']

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with any additional arguments or keyword arguments.
        """
        super(CardConfigForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(CardConfigForm, self).save(commit=False)
        if 'event_image' in self.changed_data:
            instance.event_image = self.cleaned_data['event_image']
        if commit:
            instance.save()
        return instance
    
    
    