from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import TrainingPluginModel
from .forms import TrainingPluginForm


class TRConfigAdmin(ModelAdmin):
    form = TrainingPluginForm


admin.site.register(TrainingPluginModel, TRConfigAdmin)
