from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from cms.models.pluginmodel import CMSPlugin

@plugin_pool.register_plugin
class Header(CMSPluginBase):
    model = CMSPlugin  # Model where data about each plugin is saved
    module = _("Base Plugin")  # Module name that will appear in the admin interface
    name = _("Header Alias")  # Name of the plugin
    render_template = "header_footer/page_header.html"  # Path to the template that will be rendered

    def render(self, context, instance, placeholder):
        return context
    
    
    
@plugin_pool.register_plugin
class Footer(CMSPluginBase):
    model = CMSPlugin  # Model where data about each plugin is saved
    module = _("Base Plugin")  # Module name that will appear in the admin interface
    name = _("Footer Alias")  # Name of the plugin
    render_template = "header_footer/page_footer.html"  # Path to the template that will be rendered

    def render(self, context, instance, placeholder):
        return context