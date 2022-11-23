from django import forms
from .models import Encuesta
from django.utils.translation import gettext_lazy as _

class AddForm(forms.ModelForm):

    class Meta:
        model = Encuesta
        fields = ('lat', 'lon', 'edad', 'peso', 'sexo', 'agua_cocinar', 'agua_tomar',
                  'cuidador', 'vasos')
        widgets = {
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'vasos': forms.NumberInput(attrs={'class': 'form-control'}),
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
        self.fields["lat"].widget.attrs['readonly'] = True
        self.fields["lon"].widget.attrs['readonly'] = True
