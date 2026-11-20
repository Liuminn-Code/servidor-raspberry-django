from django import forms
from .models import RegistroMetrica

class RegistroMetricaForm(forms.ModelForm):

    class Meta:
        model = RegistroMetrica
        fields = ['cpu', 'ram', 'temperatura']

    def clean_cpu(self):
        cpu = self.cleaned_data['cpu']
        if cpu < 0 or cpu > 100:
            raise forms.ValidationError(
                "El CPU debe estar entre 0 y 100."
            )
        return cpu

    def clean_ram(self):
        ram = self.cleaned_data['ram']
        if ram < 0 or ram > 100:
            raise forms.ValidationError(
                "La RAM debe estar entre 0 y 100."
            )
        return ram
