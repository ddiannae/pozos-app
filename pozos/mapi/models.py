from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.geos import Point

ALC_CHOICES = ["Indeseable","Baja", "Media", "Alta", "Indeseable como FAAP"]
CONDUCT_CHOICES = ["Excelente para riego", "Buena para riego", "Permisible para riego",
                  "Dudosa para riego", "Indeseable para riego"]
SDTM_SAL_CHOICES = ["Potable - Dulce", "Ligeramente salobres", "Salobres",
                    "Salinas"]
SDTM_RA_CHOICES = ["Excelente para riego", "Cultivos sensibles", "Cultivos con manejo especial",
                       "Cultivos tolerantes", "Indeseable para riego"]
FLUOR_CHOICES = ["Potable - Optima", "Media", "Baja", "Alta"]
DUR_CHOICES = ["Potable - Suave", "Potable - Moderadamente suave", "Potable - Dura",
               "Muy dura e indeseable usos industrial y domestico"]
COLI_CHOICES = ["Excelente", "Buena calidad", "Aceptable", "Contaminada",
                "Fuertemente contaminada"]
# rojo, naranja, amarillo, turquesa, azul, lightgrey
COLORES = ["#C70039", "#FF5733", "#FFC300", "#40E0D0", "#0000CD",  "#D3D3D3"]
NA_TEXT = "No encontrado"

class Pozo(models.Model):

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
    lon = models.FloatField()
    lat = models.FloatField()
    periodo = models.PositiveSmallIntegerField()
    #fe_total = models.FloatField()
    alc_total = models.FloatField(null=True)
    conduct_total = models.FloatField(null=True)
    sdtm_total = models.FloatField(null=True)
    fluor_total = models.FloatField(null=True)
    dur_total = models.FloatField(null=True)
    coli_total = models.FloatField(null=True)

    semaforo = models.CharField(
        max_length = 32,
        choices = SEMAFORO
    )

    @property
    def ubicacion(self):
        return (self.lat, self.lon)

    @property
    def alc_calidad(self):
        if self.alc_total is None:
            return None
        elif self.alc_total < 20:
             return ALC_CHOICES[0]
        elif self.alc_total >= 20 and self.alc_total < 75:
             return ALC_CHOICES[1]
        elif self.alc_total >= 75 and self.alc_total <= 150:
             return ALC_CHOICES[2]
        elif self.alc_total > 150 and self.alc_total <= 400:
             return ALC_CHOICES[3]
        else:
             return ALC_CHOICES[4]
    
    @property
    def alc_descripcion(self):
        if self.alc_calidad is None:
            return NA_TEXT
        elif self.alc_calidad == ALC_CHOICES[0] or self.alc_calidad == ALC_CHOICES[4]:
             return "Agua no apta como fuente de abastecimiento de agua potable"
        elif self.alc_calidad == ALC_CHOICES[3] or self.alc_calidad == ALC_CHOICES[1]:
             return "Agua apta como fuente de abastecimiento de agua potable"
        elif self.alc_calidad == ALC_CHOICES[2]:
             return "Agua potable. Agua no contaminada o condición normal"

    @property
    def alc_color(self):
        if self.alc_calidad is None:
            return COLORES[-1] 
        elif self.alc_calidad == ALC_CHOICES[0] or self.alc_calidad == ALC_CHOICES[4]:
             return COLORES[0]
        elif self.alc_calidad == ALC_CHOICES[3] or self.alc_calidad == ALC_CHOICES[1]:
             return COLORES[3]
        elif self.alc_calidad == ALC_CHOICES[2]:
             return COLORES[4]

    @property
    def conduct_calidad(self):
        if self.conduct_total is None:
            return None
        elif self.conduct_total <= 250:
             return CONDUCT_CHOICES[0] 
        elif self.conduct_total > 250 and self.conduct_total <= 750:
             return CONDUCT_CHOICES[1] 
        elif self.conduct_total > 750 and self.conduct_total <= 2000:
             return CONDUCT_CHOICES[2] 
        elif self.conduct_total > 2000 and self.conduct_total <= 3000:
             return CONDUCT_CHOICES[3] 
        else:
             return CONDUCT_CHOICES[4] 
    
    @property
    def conduct_descripcion(self):
        if self.conduct_calidad is None:
            return NA_TEXT 
        elif self.conduct_calidad == CONDUCT_CHOICES[0]: 
            return "Excelente para riego de todo tipo de cultivos" 
        elif self.conduct_calidad == CONDUCT_CHOICES[1]:
            return "Apta para riego de cultivos sensibles"
        elif self.conduct_calidad == CONDUCT_CHOICES[2]:
            return "Apta para riego de cultivos con manejo especial"
        elif self.conduct_calidad == CONDUCT_CHOICES[3]:
            return "Apta para riego de cultivos tolerantes" 
        else:
            return "Indeseable para riego"
   
    @property
    def conduct_color(self):
        if self.conduct_calidad is None:
            return COLORES[-1]
        elif self.conduct_calidad == CONDUCT_CHOICES[0]: 
            return COLORES[4]
        elif self.conduct_calidad == CONDUCT_CHOICES[1]:
            return COLORES[3] 
        elif self.conduct_calidad == CONDUCT_CHOICES[2]:
            return COLORES[2]
        elif self.conduct_calidad == CONDUCT_CHOICES[3]:
            return COLORES[1] 
        else:
            return COLORES[0]

    @property
    def sdtm_sal_calidad(self):
        if self.sdtm_total is None:
            return None
        elif self.sdtm_total <= 1000:
           return SDTM_SAL_CHOICES[0]
        elif self.sdtm_total > 1000 and self.sdtm_total <= 2000:
           return SDTM_SAL_CHOICES[1]
        elif self.sdtm_total > 2000 and self.sdtm_total <= 10000:
           return SDTM_SAL_CHOICES[2]
        else:
           return SDTM_SAL_CHOICES[3]

    @property 
    def sdtm_sal_descripcion(self): 
        if self.sdtm_sal_calidad is None:
            return NA_TEXT
        elif self.sdtm_sal_calidad == SDTM_SAL_CHOICES[0]:
            return "Agua Potable. Agua Dulce"
        elif  self.sdtm_sal_calidad == SDTM_SAL_CHOICES[1]:
            return "Aguas subterráneas con bajo contenido de sales"
        elif  self.sdtm_sal_calidad == SDTM_SAL_CHOICES[2]:
            return "Aguas subterráneas con alto contenido de sales"
        else:
            return "Aguas subterráneas con muy alto contenido de sales"

    @property
    def sdtm_sal_color(self):
        if self.sdtm_sal_calidad is None:
            return COLORES[-1]
        elif self.sdtm_sal_calidad == SDTM_SAL_CHOICES[0]:
            return COLORES[4]
        elif  self.sdtm_sal_calidad == SDTM_SAL_CHOICES[1]:
            return COLORES[3]
        elif  self.sdtm_sal_calidad == SDTM_SAL_CHOICES[2]:
            return COLORES[2]
        else:
            return COLORES[0]

    @property
    def sdtm_ra_calidad(self):
        if self.sdtm_total is None:
            return None
        elif self.sdtm_total <= 500:
            return SDTM_RA_CHOICES[0]
        elif self.sdtm_total > 500 and self.sdtm_total <= 1000:
            return SDTM_RA_CHOICES[1]
        elif self.sdtm_total > 1000 and self.sdtm_total <= 2000:
            return SDTM_RA_CHOICES[2]
        elif self.sdtm_total > 2000 and self.sdtm_total <= 5000:
            return SDTM_RA_CHOICES[3]
        else:
            return SDTM_RA_CHOICES[4]

    @property
    def sdtm_ra_descripcion(self):
        if self.sdtm_ra_calidad is None:
            return NA_TEXT
        elif self.sdtm_ra_calidad == SDTM_RA_CHOICES[0]:
            return "Excelente para riego de todo tipo de cultivos"
        elif self.sdtm_ra_calidad == SDTM_RA_CHOICES[1]:
            return "Apta para riego de cultivos sensibles"
        elif self.sdtm_ra_calidad == SDTM_RA_CHOICES[2]:
            return "Apta para riego de cultivos con manejo especial"
        elif self.sdtm_ra_calidad == SDTM_RA_CHOICES[3]:
            return "Apta para riego de cultivos tolerantes"
        else: 
            return "Indeseable para riego"

    @property
    def sdtm_ra_color(self):
        if self.sdtm_ra_calidad is None:
            return COLORES[-1]
        elif self.sdtm_ra_calidad == SDTM_RA_CHOICES[0]:
            return COLORES[4]
        elif self.sdtm_ra_calidad == SDTM_RA_CHOICES[1]:
            return COLORES[3]
        elif self.sdtm_ra_calidad == SDTM_RA_CHOICES[2]:
            return COLORES[2]
        elif self.sdtm_ra_calidad == SDTM_RA_CHOICES[3]:
            return COLORES[1]
        else: 
            return COLORES[0]

    @property
    def fluor_calidad(self):
        if self.fluor_total is None:
            return None
        elif self.fluor_total >= 0.7 and self.fluor_total < 1.5:
            return FLUOR_CHOICES[0]
        elif self.fluor_total >= 0.4 and self.fluor_total < 0.7:
            return FLUOR_CHOICES[1]
        elif self.fluor_total < 0.4:
            return FLUOR_CHOICES[2]
        else:
            return FLUOR_CHOICES[3]

    @property
    def fluor_descripcion(self):
        if self.fluor_calidad is None:
            return NA_TEXT 
        elif self.fluor_calidad == FLUOR_CHOICES[0]:
            return "Agua potable. Agua no contaminada o condición normal"
        elif self.fluor_calidad == FLUOR_CHOICES[1]:
            return "Agua con nivel medio de fluoruros"
        elif self.fluor_calidad == FLUOR_CHOICES[2]:
            return "Agua con bajo contenido de fluoruros"
        elif self.fluor_calidad == FLUOR_CHOICES[3]:
            return "Agua no apta como fuente de abastecimiento de agua potable"

    @property
    def fluor_color(self):
        if self.fluor_calidad is None:
            return COLORES[-1]
        elif self.fluor_calidad == FLUOR_CHOICES[0]:
            return COLORES[4]
        elif self.fluor_calidad == FLUOR_CHOICES[1]:
            return COLORES[2] 
        elif self.fluor_calidad == FLUOR_CHOICES[2]:
            return COLORES[1] 
        elif self.fluor_calidad == FLUOR_CHOICES[3]:
            return COLORES[0] 


    @property
    def dur_calidad(self):
        if self.dur_total is None:
            return None
        elif self.dur_total <= 60: 
            return DUR_CHOICES[0] 
        elif self.dur_total > 60 and self.dur_total <= 120:
            return DUR_CHOICES[1] 
        elif self.dur_total > 120 and self.dur_total <= 500:
            return DUR_CHOICES[2] 
        else:
            return DUR_CHOICES[3] 

    @property
    def dur_descripcion(self):
        if self.dur_calidad is None:
            return NA_TEXT 
        elif self.dur_calidad == DUR_CHOICES[0]:
            return "Agua potable. Bajo contenido de minerales"
        elif self.dur_calidad == DUR_CHOICES[1]:
            return "Agua potable. Moderado contenido de minerales"
        elif self.dur_calidad == DUR_CHOICES[2]:
            return "Agua potable. Alto contenido de minerales, principalmente sales de calcio y magnesio"
        elif self.dur_calidad == DUR_CHOICES[3]:
            return "Agua no apta como fuente de abastecimiento de agua potable. Muy dura e indeseable usos industrial y doméstico"

    @property
    def dur_color(self):
        if self.dur_calidad is None:
            return COLORES[-1] 
        elif self.dur_calidad == DUR_CHOICES[0]:
            return COLORES[4] 
        elif self.dur_calidad == DUR_CHOICES[1]:
            return COLORES[3] 
        elif self.dur_calidad == DUR_CHOICES[2]:
            return COLORES[2] 
        elif self.dur_calidad == DUR_CHOICES[3]:
            return COLORES[0] 

    @property
    def coli_calidad(self):
        if self.coli_total is None:
            return None
        elif self.coli_total <= 1.1:
            return COLI_CHOICES[0]
        elif self.coli_total >= 1.1 and self.coli_total <= 200:
            return COLI_CHOICES[1]
        elif self.coli_total > 200 and self.coli_total <= 1000:
            return COLI_CHOICES[2]
        elif self.coli_total > 1000 and self.coli_total <= 10000:
            return COLI_CHOICES[3]
        else:
            return COLI_CHOICES[4]

    @property
    def coli_descripcion(self):
        if self.coli_calidad is None:
            return NA_TEXT
        elif self.coli_calidad == COLI_CHOICES[0]:
            return "Agua potable. Agua no contaminada o condición normal. No hay evidencia de alteración en los valores de la calidad bacteriológica para el cuerpo de agua subterráneo"
        elif self.coli_calidad == COLI_CHOICES[1]:
            return "Aguas para uso recreativo con contacto primario, así como para otros usos. Indicios de alteración de la calidad bacteriológica"
        elif self.coli_calidad == COLI_CHOICES[2]:
            return "Aguas con calidad admisible como fuente de abastecimiento de agua potable y para riego agrícola. Muestra bajos niveles de alteración como resultado de la actividad humana"
        elif self.coli_calidad == COLI_CHOICES[3]:
            return "Aguas  con contaminación bacteriológica. Indica alteración substancial con respecto a la condición normal"
        else:
            return "Aguas con fuerte contaminación bacteriológica. Alteración severa"

    @property
    def coli_color(self):
        if self.coli_calidad is None:
            return NA_TEXT
        elif self.coli_calidad == COLI_CHOICES[0]:
            return COLORES[4] 
        elif self.coli_calidad == COLI_CHOICES[1]:
            return COLORES[3] 
        elif self.coli_calidad == COLI_CHOICES[2]:
            return COLORES[2]
        elif self.coli_calidad == COLI_CHOICES[3]:
            return COLORES[1] 
        else:
            return COLORES[0]
