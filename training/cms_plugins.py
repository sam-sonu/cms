from django.utils.translation import gettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import TrainingPluginModel  # Import the model

@plugin_pool.register_plugin
class TrainingPlugin(CMSPluginBase):
    module = _("Training")
    name = _("Training Plugin")  # Name of the plugin
    cache = False
    render_template = "training/training_list.html"  # template to render the plugin with
    

    def render(self, context, instance, placeholder):
        # Fetch all data from TrainingPluginModel
        trainings = TrainingPluginModel.objects.all()
        
        # Update the context with fetched data
        context.update({
            'instance': instance,
            'trainings': trainings,
        })
        return context