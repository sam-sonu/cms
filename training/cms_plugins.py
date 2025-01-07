from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from .models import TrainingPluginModel
from .forms import TrainingPluginForm

@plugin_pool.register_plugin
class TrainingPlugin(CMSPluginBase):
    model = TrainingPluginModel  # Model where data about each plugin is stored
    module = _("Training")
    name = _("Training Plugin")  # Name of the plugin
    cache = False
    render_template = "training/training_plugin.html"  # template to render the plugin with
    form = TrainingPluginForm  # Use custom form to hide fields

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context