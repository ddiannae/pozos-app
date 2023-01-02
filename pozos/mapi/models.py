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
NNO3_CHOICES = ["Potable - Excelente", "Potable - Buena calidad",
                "No apta como FAAP"]
MN_FE_CHOICES = ["Potable - Excelente", "Sin efectos en la salud - Puede dar color al agua",
                 "Puede afectar la salud"]
SHARED_CHOICES = ["Potable - Excelente", "Apta como FAAP", "No apta como FAAP"]

# rojo, naranja, amarillo, turquesa, azul, lightgrey
COLORES = ["#C70039", "#FF5733", "#FFC300", "#40E0D0", "#0000CD",  "#D3D3D3"]
NA_TEXT = "No encontrado"

class Pozo(models.Model):

    VERDE = 'Verde'
    AMARILLO = 'Amarillo'
    ROJO = 'Rojo'

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
    alc_total = models.FloatField(null=True)
    conduct_total = models.FloatField(null=True)
    sdtm_total = models.FloatField(null=True)
    fluor_total = models.FloatField(null=True)
    dur_total = models.FloatField(null=True)
    coli_total = models.FloatField(null=True)
    nno3_total = models.FloatField(null=True)
    as_total = models.FloatField(null=True)
    cd_total = models.FloatField(null=True)
    cr_total = models.FloatField(null=True)
    hg_total = models.FloatField(null=True)
    pb_total = models.FloatField(null=True)
    mn_total = models.FloatField(null=True)
    fe_total = models.FloatField(null=True)

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
        else:
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
        else:
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
        else:
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
        else:
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

    @property
    def nno3_calidad(self):
        if self.nno3_total is None:
            return None
        elif self.nno3_total <= 5:
            return NNO3_CHOICES[0]
        elif self.nno3_total > 5 and self.nno3_total < 11:
            return NNO3_CHOICES[1]
        else:
            return NNO3_CHOICES[2]

    @property
    def nno3_descripcion(self):
        if self.nno3_calidad is None:
            return NA_TEXT
        elif self.nno3_calidad == NNO3_CHOICES[0]:
            return "Agua potable. Agua no contaminada o condición normal"
        elif self.nno3_calidad == NNO3_CHOICES[1]:
            return """Aguas con indicios de aguas residuales o fertilizantes.
            Condición eutrófica-altos niveles de nutrientes. Efectos moderados en
            cultivos regados"""
        else:
            return "Aguas superficiales con fuerte impacto de aguas residuales crudas con alta carga de nutrientes. Condición hipertrófica, florecimientos algales que incluyen especies tóxicas a seres vivos"

    @property
    def nno3_color(self):
        if self.nno3_calidad is None:
            return COLORES[-1]
        elif self.nno3_calidad == NNO3_CHOICES[0]:
            return COLORES[4]
        elif self.nno3_calidad == NNO3_CHOICES[1]:
            return COLORES[3]
        else:
            return COLORES[0]

    @property
    def as_calidad(self):
        if self.as_total is None:
            return None
        elif self.as_total <= 0.01:
            return SHARED_CHOICES[0]
        elif self.as_total > 0.01 and self.as_total <= 0.025:
            return SHARED_CHOICES[1]
        else:
            return SHARED_CHOICES[2]
 
    @property
    def as_descripcion(self):
        if self.as_calidad is None:
            return NA_TEXT
        elif self.as_calidad == SHARED_CHOICES[0]:
            return "Agua potable. Agua no contaminada o condición normal"
        elif self.as_calidad == SHARED_CHOICES[1]:
            return "Agua apta como fuente de abastecimiento de agua potable"
        else:
            return "Agua no apta como fuente de abastecimiento de agua potable o requiere de tratamiento para su remoción"

    @property
    def as_color(self):
        if self.as_calidad is None:
            return COLORES[-1]
        elif self.as_calidad == SHARED_CHOICES[0]:
            return COLORES[4]
        elif self.as_calidad == SHARED_CHOICES[1]:
            return COLORES[3]
        else:
            return COLORES[0]

    @property
    def cd_calidad(self):
        if self.cd_total is None:
            return None
        elif self.cd_total <= 0.003:
            return SHARED_CHOICES[0]
        elif self.cd_total > 0.003 and self.cd_total <= 0.005:
            return SHARED_CHOICES[1]
        else:
            return SHARED_CHOICES[2]

    @property
    def cd_descripcion(self):
        if self.cd_calidad is None:
            return NA_TEXT
        elif self.cd_calidad == SHARED_CHOICES[0]:
            return "Agua potable. Agua no contaminada o condición normal"
        elif self.cd_calidad == SHARED_CHOICES[1]:
            return "Agua apta como fuente de abastecimiento de agua potable"
        else:
            return "Agua no apta como fuente de abastecimiento de agua potable"

    @property
    def cd_color(self):
        if self.cd_calidad is None:
            return COLORES[-1]
        elif self.cd_calidad == SHARED_CHOICES[0]:
            return COLORES[4]
        elif self.cd_calidad == SHARED_CHOICES[1]:
            return COLORES[3]
        else:
            return COLORES[0]

    @property
    def cr_calidad(self):
        if self.cr_total is None:
            return None
        elif self.cr_total <= 0.05:
            return SHARED_CHOICES[0]
        else:
            return SHARED_CHOICES[2]

    @property
    def cr_descripcion(self):
        if self.cr_calidad is None:
            return NA_TEXT
        elif self.cr_calidad == SHARED_CHOICES[0]:
            return "Agua potable. Agua no contaminada o condición normal"
        else:
            return "Agua no apta como fuente de abastecimiento de agua potable"

    @property
    def cr_color(self):
        if self.cr_calidad is None:
            return COLORES[-1]
        elif self.cd_calidad == SHARED_CHOICES[0]:
            return COLORES[4]
        else:
            return COLORES[0]

    @property
    def hg_calidad(self):
        if self.hg_total is None:
            return None
        elif self.hg_total <= 0.006:
            return SHARED_CHOICES[0]
        else:
            return SHARED_CHOICES[2]

    @property
    def hg_descripcion(self):
        if self.hg_calidad is None:
            return NA_TEXT
        elif self.hg_calidad == SHARED_CHOICES[0]:
            return "Agua potable. Agua no contaminada o condición normal"
        else:
            return "Agua no apta como fuente de abastecimiento de agua potable"

    @property
    def hg_color(self):
        if self.hg_calidad is None:
            return COLORES[-1]
        elif self.hg_calidad == SHARED_CHOICES[0]:
            return COLORES[4]
        else:
            return COLORES[0]

    @property
    def pb_calidad(self):
        if self.pb_total is None:
            return None
        elif self.pb_total <= 0.01:
            return SHARED_CHOICES[0]
        else:
            return SHARED_CHOICES[2]

    @property
    def pb_descripcion(self):
        if self.pb_calidad is None:
            return NA_TEXT
        elif self.pb_calidad == SHARED_CHOICES[0]:
            return "Agua potable. Agua no contaminada o condición normal"
        else:
            return "Agua no apta como fuente de abastecimiento de agua potable"

    @property
    def pb_color(self):
        if self.pb_calidad is None:
            return COLORES[-1]
        elif self.pb_calidad == SHARED_CHOICES[0]:
            return COLORES[4]
        else:
            return COLORES[0]

    @property
    def mn_calidad(self):
        if self.mn_total is None:
            return None
        elif self.mn_total <= 0.15:
            return MN_FE_CHOICES[0]
        elif self.mn_total > 0.15 and self.mn_total <= 0.4:
            return MN_FE_CHOICES[1]
        else:
            return MN_FE_CHOICES[2]

    @property
    def mn_descripcion(self):
        if self.mn_calidad is None:
            return NA_TEXT
        elif self.mn_calidad == MN_FE_CHOICES[0]:
            return "Agua potable. Agua no contaminada o condición normal"
        elif self.mn_calidad == MN_FE_CHOICES[1]:
            return "Sin efectos en la salud - Puede dar color al agua"
        else:
            return "Agua no apta como fuente de abastecimiento de agua potable. Puede afectar la salud"

    @property
    def mn_color(self):
        if self.mn_calidad is None:
            return COLORES[-1]
        elif self.mn_calidad == MN_FE_CHOICES[0]:
            return COLORES[4]
        elif self.mn_calidad == MN_FE_CHOICES[1]:
            return COLORES[3]
        else:
            return COLORES[0]

    @property
    def fe_calidad(self):
        if self.fe_total is None:
            return None
        elif self.fe_total <= 0.3:
            return MN_FE_CHOICES[0]
        else:
            return MN_FE_CHOICES[1]

    @property
    def fe_descripcion(self):
        if self.fe_calidad is None:
            return NA_TEXT
        elif self.fe_calidad == MN_FE_CHOICES[0]:
            return "Agua potable. Agua no contaminada o condición normal"
        else:
            return "Sin efectos en la salud - Puede dar color al agua"

    @property
    def fe_color(self):
        if self.fe_calidad is None:
            return COLORES[-1]
        elif self.fe_calidad == MN_FE_CHOICES[0]:
            return COLORES[4]
        else:
            return COLORES[3]
