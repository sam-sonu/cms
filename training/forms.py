from django import forms
from .models import TrainingPluginModel

class TrainingPluginForm(forms.ModelForm):
    class Meta:
        model = TrainingPluginModel
        fields = '__all__'
        widgets = {
            # 'description': forms.HiddenInput(),
            # 'event_dt': forms.HiddenInput(),
            # 'location': forms.HiddenInput(),
        }