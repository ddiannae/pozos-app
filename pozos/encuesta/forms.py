from django import forms
from .models import Encuesta
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import HiddenInput
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.core.exceptions import ValidationError

class ContestarForm(forms.ModelForm):
    captcha = ReCaptchaField(widget = ReCaptchaV2Checkbox(attrs={'data-callback': 'enableFormSubmit'}),
                             label='')

    class Meta:
        model = Encuesta
        fields = ('lat', 'lon', 'edad', 'peso', 'sexo', 'agua_cocinar', 'agua_tomar',
                  'cuidador', 'vasos')
        widgets = {
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'vasos': forms.NumberInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'agua_cocinar': forms.Select(attrs={'class': 'form-select'}),
            'agua_tomar': forms.Select(attrs={'class': 'form-select'}),
            'cuidador': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'edad': _('¿Cuántos años tienes?'),
            'peso': _('¿Cuántos kilos pesas?'),
            'sexo': _('Sexo'),
            'agua_cocinar': _('¿Qué tipo de agua usas para cocinar?'),
            'agua_tomar': _('¿Qué tipo de agua clara usas para beber?'),
            'vasos': _('¿Cuántos vasos de agua tomas al día?'),
            'cuidador': _('¿Eres el o la principal cuidadora de menores de edad?')
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["lon"].error_messages = {'required': 'Elige un punto en el mapa o haz click en el botón para identificar tu ubicación'}
        self.fields["lat"].error_messages = {'required': ''}

    def clean(self):
        super(ContestarForm, self).clean()
        lat = self.cleaned_data.get("lat")
        lon = self.cleaned_data.get("lon")

        if lat is None or lon is None:
            return self.cleaned_data
        if lat < 14.5 or lat > 32.56:
            self.add_error("lat", "Latitud inválida. Elige un punto dentro del territorio nacional.")
        if lon < -117.15 or lon > -86.5:
            self.add_error("lon", "Longitud inválida. Elige un punto dentro del territorio nacional.")
        return self.cleaned_data

