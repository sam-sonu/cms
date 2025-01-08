from django.utils.translation import gettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import UpcomingEventsModel
from .forms import CardConfigForm
from django.shortcuts import render

@plugin_pool.register_plugin
class UpcomingEventsPlugin(CMSPluginBase):
    
    module = _("UpcomingEvents")
    name = _("UpcomingEvents Plugin") 
    model = UpcomingEventsModel
    render_template = "plugins/upcoming_events.html"
    cache = False
    form = CardConfigForm

    def render(self, context, instance, placeholder):
        # Fetch all events from the database
        events = UpcomingEventsModel.objects.all()
        # Update the context with the events
        context['instance'] = instance
        context['events'] = events
        
        return context