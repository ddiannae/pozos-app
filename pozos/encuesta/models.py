from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Encuesta(models.Model):
    MUJER = 'mujer'
    HOMBRE = 'hombre'
    
    SEXO = [
        (MUJER, _('Mujer')),
        (HOMBRE, _('Hombre'))
    ]

    LLAVE =  'llave'
    GARRAFON = 'garrafon'
    FILTRO = 'filtro'
    HERVIDA = 'hervida'
    OTRA = 'otra'

    AGUAS = [
        (LLAVE, _('De la llave')),
        (GARRAFON, _('De garrafón')),
        (FILTRO, _('De filtro')),
        (HERVIDA, _('Hervida')),
        (OTRA, _('Otra'))
    ]

    SI_NO = (
        (True, _('Sí')),
        (False, _('No'))
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    edad = models.PositiveSmallIntegerField()
    peso = models.PositiveSmallIntegerField()
    sexo = models.CharField(
        max_length = 32,
        choices = SEXO
    )
    agua_cocinar = models.CharField(
        max_length = 32,
        choices = AGUAS 
    )
    agua_tomar = models.CharField(
        max_length = 32,
        choices = AGUAS 
    )
    cuidador = models.BooleanField(choices = SI_NO) 
    vasos = models.PositiveSmallIntegerField(default=0)
    lat = models.FloatField()
    lon = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total_vasos(self):
        return (self.vasos * 250)/1000


