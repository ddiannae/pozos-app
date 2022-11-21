from django.db import models
from django.utils.translation import gettext_lazy as _

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    vasos = models.PositiveSmallIntegerField(default=0)

