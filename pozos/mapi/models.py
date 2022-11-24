from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.geos import Point

class Pozo(models.Model):

    EXCELENTE = 'POTABLE - EXCELENTE'
    SIN_EFECTOS = 'SIN EFECTOS EN LA SALUD - PUEDE DAR COLOR AL AGUA'

    CALIDAD = [
        (EXCELENTE, _('Potable - Excelente')),
        (SIN_EFECTOS, _('Sin efectos en la salud - Puede dar color al agua')),
    ]

    VERDE = 'VERDE'
    AMARILLO = 'AMARILLO'
    ROJO = 'ROJO'

    SEMAFORO = [
        (VERDE, _('Verde')),
        (AMARILLO, _('Amarillo')),
        (ROJO, _('Rojo'))
    ]

    clave = models.CharField(max_length = 64)
    sitio = models.CharField(max_length = 128)
    organismo = models.CharField(max_length = 128)
    estado = models.CharField(max_length = 128)
    municipio = models.CharField(max_length = 128)
    acuifero = models.CharField(max_length = 128)
    subtipo = models.CharField(max_length = 32)
    lat = models.FloatField()
    lon = models.FloatField()
    fe_total = models.FloatField()
    fe_calidad = models.CharField(
        max_length = 256,
        choices = CALIDAD
    )
    semaforo = models.CharField(
        max_length = 32,
        choices = SEMAFORO
    )

    @property
    def ubicacion(self):
        return Point(self.lon, self.lat, srid=3857)
