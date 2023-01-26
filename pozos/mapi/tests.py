from django.test import TestCase
from mapi.models import Pozo
from random import uniform

class PozoModelTests(TestCase):
    
    def test_alc_calidad_descripcion_and_color_are_ok_when_alc_total_is_None(self):
        pozo = Pozo(alc_total = None)
        self.assertIs(pozo.alc_calidad, None)
        self.assertEqual(pozo.alc_descripcion, "No encontrado")
        self.assertEqual(pozo.alc_color, "#D3D3D3")

    def test_alc_calidad_descripcion_and_colore_are_ok_when_alc_total_is_20(self):
        pozo = Pozo(alc_total = 20)
        self.assertEqual(pozo.alc_calidad, "Baja")
        self.assertEqual(pozo.alc_descripcion, "Agua apta como fuente de abastecimiento de agua potable")
        self.assertEqual(pozo.alc_color, "#40E0D0") 

    def test_alc_calidad_descripcion_and_color_are_ok_when_alc_total_is_between_20_75(self):
        pozo = Pozo(alc_total = uniform(20, 74.9))
        self.assertEqual(pozo.alc_calidad, "Baja")
        self.assertEqual(pozo.alc_descripcion, "Agua apta como fuente de abastecimiento de agua potable")
        self.assertEqual(pozo.alc_color, "#40E0D0") 
    
    def test_alc_calidad_descripcion_and_color_are_ok_when_alc_total_is_75(self):
        pozo = Pozo(alc_total = 75)
        self.assertEqual(pozo.alc_calidad, "Media")
        self.assertEqual(pozo.alc_descripcion, "Agua potable. Agua no" +
                        " contaminada o condición normal")
        self.assertEqual(pozo.alc_color, "#0000CD") 

    def test_alc_calidad_descripcion_and_color_are_ok_when_alc_total_is_150(self):
        pozo = Pozo(alc_total = 150)
        self.assertEqual(pozo.alc_calidad, "Media")
        self.assertEqual(pozo.alc_descripcion, "Agua potable. Agua no" +
                        " contaminada o condición normal")
        self.assertEqual(pozo.alc_color, "#0000CD") 

    def test_alc_calidad_descripcion_and_color_are_ok_when_alc_total_is_between_75_150(self):
        pozo = Pozo(alc_total = uniform(75, 150))
        self.assertEqual(pozo.alc_calidad, "Media")
        self.assertEqual(pozo.alc_descripcion, "Agua potable. Agua no" +
                        " contaminada o condición normal")
        self.assertEqual(pozo.alc_color, "#0000CD") 

    def test_alc_calidad_descripcion_and_color_are_ok_when_alc_total_is_400(self):
        pozo = Pozo(alc_total = 400)
        self.assertEqual(pozo.alc_calidad, "Alta")
        self.assertEqual(pozo.alc_descripcion, "Agua apta como fuente de abastecimiento de agua potable")
        self.assertEqual(pozo.alc_color, "#40E0D0") 

    def test_alc_calidad_descripcion_and_color_are_ok_when_alc_total_is_between_150_400(self):
        pozo = Pozo(alc_total = uniform(150.1, 400))
        self.assertEqual(pozo.alc_calidad, "Alta")
        self.assertEqual(pozo.alc_descripcion, "Agua apta como fuente de abastecimiento de agua potable")
        self.assertEqual(pozo.alc_color, "#40E0D0") 

    def test_alc_calidad_descripcion_and_color_are_ok_when_alc_total_is_less_20(self):
        pozo = Pozo(alc_total = uniform(0, 19.9))
        self.assertEqual(pozo.alc_calidad, "Indeseable")
        self.assertEqual(pozo.alc_descripcion, "Agua no apta como fuente de" +
                         " abastecimiento de agua potable")
        self.assertEqual(pozo.alc_color, "#C70039") 


    def test_alc_calidad_descripcion_and_color_are_ok_when_alc_total_greater_400(self):
        pozo = Pozo(alc_total = uniform(400.1, 1000))
        self.assertEqual(pozo.alc_calidad, "Indeseable como FAAP")
        self.assertEqual(pozo.alc_descripcion, "Agua no apta como fuente de" +
                         " abastecimiento de agua potable")
        self.assertEqual(pozo.alc_color, "#C70039") 

    def test_conduct_calidad_descripcion_and_color_are_ok_when_conduct_total_is_None(self):
        pozo = Pozo(conduct_total = None)
        self.assertIs(pozo.conduct_calidad, None)
        self.assertEqual(pozo.conduct_descripcion, "No encontrado")
        self.assertEqual(pozo.conduct_color, "#D3D3D3")

    def test_conduct_calidad_descripcion_and_color_are_ok_when_conduct_total_is_250(self):
        pozo = Pozo(conduct_total = 250)
        self.assertEqual(pozo.conduct_calidad, "Excelente para riego")
        self.assertEqual(pozo.conduct_descripcion, "Excelente para riego de" +
                        " todo tipo de cultivos")
        self.assertEqual(pozo.conduct_color, "#0000CD")

    def test_conduct_calidad_descripcion_and_color_are_ok_when_conduct_total_is_less_than_250(self):
        pozo = Pozo(conduct_total = uniform(0, 250))
        self.assertEqual(pozo.conduct_calidad, "Excelente para riego")
        self.assertEqual(pozo.conduct_descripcion, "Excelente para riego de" +
                        " todo tipo de cultivos")
        self.assertEqual(pozo.conduct_color, "#0000CD")

    def test_conduct_calidad_descripcion_and_color_are_ok_when_conduct_total_is_750(self):
        pozo = Pozo(conduct_total = 750)
        self.assertEqual(pozo.conduct_calidad, "Buena para riego")
        self.assertEqual(pozo.conduct_descripcion, "Apta para riego de" +
                        " cultivos sensibles")
        self.assertEqual(pozo.conduct_color, "#40E0D0")

    def test_conduct_calidad_descripcion_and_color_are_ok_when_conduct_total_is_between_250_and_750(self):
        pozo = Pozo(conduct_total = uniform(250.1, 750))
        self.assertEqual(pozo.conduct_calidad, "Buena para riego")
        self.assertEqual(pozo.conduct_descripcion, "Apta para riego de" +
                        " cultivos sensibles")
        self.assertEqual(pozo.conduct_color, "#40E0D0")

    def test_conduct_calidad_descripcion_and_color_are_ok_when_conduct_total_is_2000(self):
        pozo = Pozo(conduct_total = 2000)
        self.assertEqual(pozo.conduct_calidad, "Permisible para riego")
        self.assertEqual(pozo.conduct_descripcion, "Apta para riego de cultivos" +
                         " con manejo especial")
        self.assertEqual(pozo.conduct_color, "#FFC300")

    def test_conduct_calidad_descripcion_and_color_are_ok_when_conduct_total_is_between_750_and_2000(self):
        pozo = Pozo(conduct_total = uniform(750.1, 2000))
        self.assertEqual(pozo.conduct_calidad, "Permisible para riego")
        self.assertEqual(pozo.conduct_descripcion, "Apta para riego de cultivos" +
                         " con manejo especial")
        self.assertEqual(pozo.conduct_color, "#FFC300")

    def test_conduct_calidad_descripcion_and_color_are_ok_when_conduct_total_is_3000(self):
        pozo = Pozo(conduct_total = 3000)
        self.assertEqual(pozo.conduct_calidad, "Dudosa para riego")
        self.assertEqual(pozo.conduct_descripcion, "Apta para riego de cultivos tolerantes")
        self.assertEqual(pozo.conduct_color, "#FF5733")

    def test_conduct_calidad_descripcion_and_color_are_ok_when_conduct_total_is_between_2000_and_3000(self):
        pozo = Pozo(conduct_total = uniform(2000.1,3000))
        self.assertEqual(pozo.conduct_calidad, "Dudosa para riego")
        self.assertEqual(pozo.conduct_descripcion, "Apta para riego de cultivos tolerantes")
        self.assertEqual(pozo.conduct_color, "#FF5733")

    def test_conduct_calidad_descripcion_and_color_are_ok_when_conduct_total_is_greater_than_3000(self):
        pozo = Pozo(conduct_total = uniform(3000.1,10000))
        self.assertEqual(pozo.conduct_calidad, "Indeseable para riego")
        self.assertEqual(pozo.conduct_descripcion, "Indeseable para riego")
        self.assertEqual(pozo.conduct_color, "#C70039")

    def test_sdtm_sal_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_None(self):
        pozo = Pozo(sdtm_total = None)
        self.assertIs(pozo.sdtm_sal_calidad, None)
        self.assertEqual(pozo.sdtm_sal_descripcion, "No encontrado")
        self.assertEqual(pozo.sdtm_sal_color, "#D3D3D3")

    def test_sdtm_sal_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_1000(self):
        pozo = Pozo(sdtm_total = 1000)
        self.assertEqual(pozo.sdtm_sal_calidad, "Potable - Dulce") 
        self.assertEqual(pozo.sdtm_sal_descripcion, "Agua Potable. Agua Dulce")
        self.assertEqual(pozo.sdtm_sal_color, "#0000CD")

    def test_sdtm_sal_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_less_than_1000(self):
        pozo = Pozo(sdtm_total = uniform(0, 999.1))
        self.assertEqual(pozo.sdtm_sal_calidad, "Potable - Dulce") 
        self.assertEqual(pozo.sdtm_sal_descripcion, "Agua Potable. Agua Dulce")
        self.assertEqual(pozo.sdtm_sal_color, "#0000CD")

    def test_sdtm_sal_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_2000(self):
        pozo = Pozo(sdtm_total = 2000)
        self.assertEqual(pozo.sdtm_sal_calidad, "Ligeramente salobres") 
        self.assertEqual(pozo.sdtm_sal_descripcion, "Aguas subterráneas con bajo contenido de sales")
        self.assertEqual(pozo.sdtm_sal_color, "#40E0D0")

    def test_sdtm_sal_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_between_1000_and_2000(self):
        pozo = Pozo(sdtm_total = uniform(1000.1,2000))
        self.assertEqual(pozo.sdtm_sal_calidad, "Ligeramente salobres") 
        self.assertEqual(pozo.sdtm_sal_descripcion, "Aguas subterráneas con bajo contenido de sales")
        self.assertEqual(pozo.sdtm_sal_color, "#40E0D0")

    def test_sdtm_sal_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_10000(self):
        pozo = Pozo(sdtm_total = 10000)
        self.assertEqual(pozo.sdtm_sal_calidad, "Salobres") 
        self.assertEqual(pozo.sdtm_sal_descripcion, "Aguas subterráneas con alto contenido de sales")
        self.assertEqual(pozo.sdtm_sal_color, "#FFC300")

    def test_sdtm_sal_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_between_2000_and_10000(self):
        pozo = Pozo(sdtm_total = uniform(2000.1,10000))
        self.assertEqual(pozo.sdtm_sal_calidad, "Salobres") 
        self.assertEqual(pozo.sdtm_sal_descripcion, "Aguas subterráneas con alto contenido de sales")
        self.assertEqual(pozo.sdtm_sal_color, "#FFC300")

    def test_sdtm_sal_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_greater_than_10000(self):
        pozo = Pozo(sdtm_total = uniform(10000.1,100000))
        self.assertEqual(pozo.sdtm_sal_calidad, "Salinas") 
        self.assertEqual(pozo.sdtm_sal_descripcion, "Aguas subterráneas con muy alto contenido de sales")
        self.assertEqual(pozo.sdtm_sal_color, "#C70039")

    def test_sdtm_ra_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_None(self):
        pozo = Pozo(sdtm_total = None)
        self.assertIs(pozo.sdtm_ra_calidad, None)
        self.assertEqual(pozo.sdtm_ra_descripcion, "No encontrado")
        self.assertEqual(pozo.sdtm_ra_color, "#D3D3D3")

    def test_sdtm_ra_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_500(self):
        pozo = Pozo(sdtm_total = 500) 
        self.assertEqual(pozo.sdtm_ra_calidad, "Excelente para riego")
        self.assertEqual(pozo.sdtm_ra_descripcion, "Excelente para riego de todo tipo de cultivos")
        self.assertEqual(pozo.sdtm_ra_color, "#0000CD")

    def test_sdtm_ra_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_less_than_500(self):
        pozo = Pozo(sdtm_total = uniform(0, 500)) 
        self.assertEqual(pozo.sdtm_ra_calidad, "Excelente para riego")
        self.assertEqual(pozo.sdtm_ra_descripcion, "Excelente para riego de todo tipo de cultivos")
        self.assertEqual(pozo.sdtm_ra_color, "#0000CD")

    def test_sdtm_ra_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_1000(self):
        pozo = Pozo(sdtm_total = 1000) 
        self.assertEqual(pozo.sdtm_ra_calidad, "Cultivos sensibles")
        self.assertEqual(pozo.sdtm_ra_descripcion, "Apta para riego de cultivos sensibles")
        self.assertEqual(pozo.sdtm_ra_color, "#40E0D0")

    def test_sdtm_ra_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_between_500_and_1000(self):
        pozo = Pozo(sdtm_total = uniform(500.1, 1000)) 
        self.assertEqual(pozo.sdtm_ra_calidad, "Cultivos sensibles")
        self.assertEqual(pozo.sdtm_ra_descripcion, "Apta para riego de cultivos sensibles")
        self.assertEqual(pozo.sdtm_ra_color, "#40E0D0")

    def test_sdtm_ra_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_between_2000(self):
        pozo = Pozo(sdtm_total = 2000) 
        self.assertEqual(pozo.sdtm_ra_calidad, "Cultivos con manejo especial")
        self.assertEqual(pozo.sdtm_ra_descripcion, "Apta para riego de cultivos con manejo especial")
        self.assertEqual(pozo.sdtm_ra_color, "#FFC300")

    def test_sdtm_ra_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_between_1000_and_2000(self):
        pozo = Pozo(sdtm_total = uniform(1000.1,2000))
        self.assertEqual(pozo.sdtm_ra_calidad, "Cultivos con manejo especial")
        self.assertEqual(pozo.sdtm_ra_descripcion, "Apta para riego de cultivos con manejo especial")
        self.assertEqual(pozo.sdtm_ra_color, "#FFC300")

    def test_sdtm_ra_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_5000(self):
        pozo = Pozo(sdtm_total = 5000)
        self.assertEqual(pozo.sdtm_ra_calidad, "Cultivos tolerantes")
        self.assertEqual(pozo.sdtm_ra_descripcion, "Apta para riego de cultivos tolerantes")
        self.assertEqual(pozo.sdtm_ra_color, "#FF5733")

    def test_sdtm_ra_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_between_2000_and_5000(self):
        pozo = Pozo(sdtm_total = uniform(2000.1,5000))
        self.assertEqual(pozo.sdtm_ra_calidad, "Cultivos tolerantes")
        self.assertEqual(pozo.sdtm_ra_descripcion, "Apta para riego de cultivos tolerantes")
        self.assertEqual(pozo.sdtm_ra_color, "#FF5733")

    def test_sdtm_ra_calidad_descripcion_and_color_are_ok_when_sdtm_total_is_greater_than_5000(self):
        pozo = Pozo(sdtm_total = uniform(5000.1, 10000))
        self.assertEqual(pozo.sdtm_ra_calidad, "Indeseable para riego")
        self.assertEqual(pozo.sdtm_ra_descripcion, "Indeseable para riego")
        self.assertEqual(pozo.sdtm_ra_color, "#C70039")
    
    def test_fluor_calidad_descripcion_and_color_are_ok_when_fluor_total_is_None(self):
        pozo = Pozo(fluor_total = None)
        self.assertIs(pozo.fluor_calidad, None)
        self.assertEqual(pozo.fluor_descripcion, "No encontrado")
        self.assertEqual(pozo.fluor_color, "#D3D3D3")

    def test_fluor_calidad_descripcion_and_color_are_ok_when_fluor_total_is_7e1(self):
        pozo = Pozo(fluor_total = 0.7)
        self.assertEqual(pozo.fluor_calidad, "Potable - Optima")
        self.assertEqual(pozo.fluor_descripcion, "Agua potable. Agua no contaminada o condición normal")
        self.assertEqual(pozo.fluor_color, "#0000CD")

    def test_fluor_calidad_descripcion_and_color_are_ok_when_fluor_total_is_between_7e1_and_1p5(self):
        pozo = Pozo(fluor_total = uniform(0.7, 1.49))
        self.assertEqual(pozo.fluor_calidad, "Potable - Optima")
        self.assertEqual(pozo.fluor_descripcion, "Agua potable. Agua no contaminada o condición normal")
        self.assertEqual(pozo.fluor_color, "#0000CD")

    def test_fluor_calidad_descripcion_and_color_are_ok_when_fluor_total_is_4e1(self):
        pozo = Pozo(fluor_total = 0.4)
        self.assertEqual(pozo.fluor_calidad, "Media")
        self.assertEqual(pozo.fluor_descripcion, "Agua con nivel medio de fluoruros")
        self.assertEqual(pozo.fluor_color, "#40E0D0")

    def test_fluor_calidad_descripcion_and_color_are_ok_when_fluor_total_is_between_4e1_and_7e1(self):
        pozo = Pozo(fluor_total = uniform(0.4, 0.69))
        self.assertEqual(pozo.fluor_calidad, "Media")
        self.assertEqual(pozo.fluor_descripcion, "Agua con nivel medio de fluoruros")
        self.assertEqual(pozo.fluor_color, "#40E0D0")

    def test_fluor_calidad_descripcion_and_color_are_ok_when_fluor_total_is_between_0_and_4e1(self):
        pozo = Pozo(fluor_total = uniform(0, 0.39))
        self.assertEqual(pozo.fluor_calidad, "Baja")
        self.assertEqual(pozo.fluor_descripcion, "Agua con bajo contenido de fluoruros")
        self.assertEqual(pozo.fluor_color, "#40E0D0")

    def test_fluor_calidad_descripcion_and_color_are_ok_when_fluor_total_is_1p5(self):
        pozo = Pozo(fluor_total = 1.5)
        self.assertEqual(pozo.fluor_calidad, "Alta")
        self.assertEqual(pozo.fluor_descripcion, "Agua no apta como fuente de abastecimiento de agua potable")
        self.assertEqual(pozo.fluor_color, "#C70039")

    def test_fluor_calidad_descripcion_and_color_are_ok_when_fluor_total_is_greater_than_1p5(self):
        pozo = Pozo(fluor_total = uniform(1.5, 10))
        self.assertEqual(pozo.fluor_calidad, "Alta")
        self.assertEqual(pozo.fluor_descripcion, "Agua no apta como fuente de abastecimiento de agua potable")
        self.assertEqual(pozo.fluor_color, "#C70039")

    def test_dur_calidad_descripcion_and_color_are_ok_when_dur_total_is_None(self):
        pozo = Pozo(dur_total = None)
        self.assertIs(pozo.dur_calidad, None)
        self.assertEqual(pozo.dur_descripcion, "No encontrado")
        self.assertEqual(pozo.dur_color, "#D3D3D3")

    def test_dur_calidad_descripcion_and_color_are_ok_when_dur_total_is_60(self):
        pozo = Pozo(dur_total = 60)
        self.assertEqual(pozo.dur_calidad, "Potable - Suave")
        self.assertEqual(pozo.dur_descripcion, "Agua potable. Bajo contenido de minerales")
        self.assertEqual(pozo.dur_color, "#0000CD")

    def test_dur_calidad_descripcion_and_color_are_ok_when_dur_total_is_less_60(self):
        pozo = Pozo(dur_total = uniform(0,60))
        self.assertEqual(pozo.dur_calidad, "Potable - Suave")
        self.assertEqual(pozo.dur_descripcion, "Agua potable. Bajo contenido de minerales")
        self.assertEqual(pozo.dur_color, "#0000CD")

    def test_dur_calidad_descripcion_and_color_are_ok_when_dur_total_is_120(self):
        pozo = Pozo(dur_total = 120)
        self.assertEqual(pozo.dur_calidad, "Potable - Moderadamente suave")
        self.assertEqual(pozo.dur_descripcion, "Agua potable. Moderado contenido de minerales")
        self.assertEqual(pozo.dur_color, "#40E0D0")

    def test_dur_calidad_descripcion_and_color_are_ok_when_dur_total_is_between_60_and_120(self):
        pozo = Pozo(dur_total = uniform(60.1, 120))
        self.assertEqual(pozo.dur_calidad, "Potable - Moderadamente suave")
        self.assertEqual(pozo.dur_descripcion, "Agua potable. Moderado contenido de minerales")
        self.assertEqual(pozo.dur_color, "#40E0D0")

    def test_dur_calidad_descripcion_and_color_are_ok_when_dur_total_is_500(self):
        pozo = Pozo(dur_total = 500)
        self.assertEqual(pozo.dur_calidad, "Potable - Dura")
        self.assertEqual(pozo.dur_descripcion, "Agua potable. Alto contenido de minerales, principalmente sales de calcio y magnesio")
        self.assertEqual(pozo.dur_color, "#FFC300")

    def test_dur_calidad_descripcion_and_color_are_ok_when_dur_total_is_between_120_and_500(self):
        pozo = Pozo(dur_total = uniform(120.1, 500))
        self.assertEqual(pozo.dur_calidad, "Potable - Dura")
        self.assertEqual(pozo.dur_descripcion, "Agua potable. Alto contenido de minerales, principalmente sales de calcio y magnesio")
        self.assertEqual(pozo.dur_color, "#FFC300")

    def test_dur_calidad_descripcion_and_color_are_ok_when_dur_total_is_greater_than_500(self):
        pozo = Pozo(dur_total = uniform(500.1, 1000))
        self.assertEqual(pozo.dur_calidad, "Muy dura e indeseable usos industrial y domestico")
        self.assertEqual(pozo.dur_descripcion, "Agua no apta como fuente de abastecimiento de agua potable." +
                         " Muy dura e indeseable usos industrial y doméstico")
        self.assertEqual(pozo.dur_color, "#C70039")

    def test_coli_calidad_descripcion_and_color_are_ok_when_coli_total_is_None(self):
        pozo = Pozo(coli_total = None)
        self.assertIs(pozo.coli_calidad, None)
        self.assertEqual(pozo.coli_descripcion, "No encontrado")
        self.assertEqual(pozo.coli_color, "#D3D3D3")

    def test_coli_calidad_descripcion_and_color_are_ok_when_coli_total_is_less_than_1p1(self):
        pozo = Pozo(coli_total = uniform(0, 1.0))
        self.assertEqual(pozo.coli_calidad, "Excelente")
        self.assertEqual(pozo.coli_descripcion, "Agua potable. Agua no contaminada o condición normal." +
                         " No hay evidencia de alteración en los valores de la calidad bacteriológica" +
                         " para el cuerpo de agua subterráneo")
        self.assertEqual(pozo.coli_color, "#0000CD")

    def test_coli_calidad_descripcion_and_color_are_ok_when_coli_total_is_1p1(self):
        pozo = Pozo(coli_total = 1.1)
        self.assertEqual(pozo.coli_calidad, "Buena calidad")
        self.assertEqual(pozo.coli_descripcion, "Aguas para uso recreativo con contacto primario," +
                         " así como para otros usos. Indicios de alteración de la calidad bacteriológica")
        self.assertEqual(pozo.coli_color, "#40E0D0")

    def test_coli_calidad_descripcion_and_color_are_ok_when_coli_total_is_200(self):
        pozo = Pozo(coli_total = 200)
        self.assertEqual(pozo.coli_calidad, "Buena calidad")
        self.assertEqual(pozo.coli_descripcion, "Aguas para uso recreativo con contacto primario," +
                         " así como para otros usos. Indicios de alteración de la calidad bacteriológica")
        self.assertEqual(pozo.coli_color, "#40E0D0")

    def test_coli_calidad_descripcion_and_color_are_ok_when_coli_total_is_between_1p1_and_200(self):
        pozo = Pozo(coli_total = uniform(1.1,200))
        self.assertEqual(pozo.coli_calidad, "Buena calidad")
        self.assertEqual(pozo.coli_descripcion, "Aguas para uso recreativo con contacto primario," +
                         " así como para otros usos. Indicios de alteración de la calidad bacteriológica")
        self.assertEqual(pozo.coli_color, "#40E0D0")

    def test_coli_calidad_descripcion_and_color_are_ok_when_coli_total_is_between_200_and_1000(self):
        pozo = Pozo(coli_total = uniform(200.1, 1000))
        self.assertEqual(pozo.coli_calidad, "Aceptable")
        self.assertEqual(pozo.coli_descripcion, "Aguas con calidad admisible como fuente de abastecimiento" +
                         " de agua potable y para riego agrícola. Muestra bajos niveles de alteración como" +
                         " resultado de la actividad humana")
        self.assertEqual(pozo.coli_color, "#FFC300")

    def test_coli_calidad_descripcion_and_color_are_ok_when_coli_total_is_1000(self):
        pozo = Pozo(coli_total = 1000)
        self.assertEqual(pozo.coli_calidad, "Aceptable")
        self.assertEqual(pozo.coli_descripcion, "Aguas con calidad admisible como fuente de abastecimiento" +
                         " de agua potable y para riego agrícola. Muestra bajos niveles de alteración como" +
                         " resultado de la actividad humana")
        self.assertEqual(pozo.coli_color, "#FFC300")

    def test_coli_calidad_descripcion_and_color_are_ok_when_coli_total_is_10000(self):
        pozo = Pozo(coli_total = 10000)
        self.assertEqual(pozo.coli_calidad, "Contaminada")
        self.assertEqual(pozo.coli_descripcion, "Aguas  con contaminación bacteriológica. Indica alteración" +
                         " substancial con respecto a la condición normal") 
        self.assertEqual(pozo.coli_color, "#FF5733")

    def test_coli_calidad_descripcion_and_color_are_ok_when_coli_total_is_between_1000_and_10000(self):
        pozo = Pozo(coli_total = uniform(1000.1, 10000))
        self.assertEqual(pozo.coli_calidad, "Contaminada")
        self.assertEqual(pozo.coli_descripcion, "Aguas  con contaminación bacteriológica. Indica alteración" +
                         " substancial con respecto a la condición normal") 
        self.assertEqual(pozo.coli_color, "#FF5733")

    def test_coli_calidad_descripcion_and_color_are_ok_when_coli_total_is_greater_than_10000(self):
        pozo = Pozo(coli_total = uniform(10000.1, 15000))
        self.assertEqual(pozo.coli_calidad, "Fuertemente contaminada")
        self.assertEqual(pozo.coli_descripcion, "Aguas con fuerte contaminación bacteriológica. Alteración severa") 
        self.assertEqual(pozo.coli_color, "#C70039")

    def test_nno3_calidad_descripcion_and_color_are_ok_when_nno3_total_is_None(self):
        pozo = Pozo(nno3_total = None)
        self.assertIs(pozo.nno3_calidad, None)
        self.assertEqual(pozo.nno3_descripcion, "No encontrado")
        self.assertEqual(pozo.nno3_color, "#D3D3D3")

    def test_nno3_calidad_descripcion_and_color_are_ok_when_nno3_total_is_5(self):
        pozo = Pozo(nno3_total = 5)
        self.assertEqual(pozo.nno3_calidad,"Potable - Excelente" )
        self.assertEqual(pozo.nno3_descripcion, "Agua potable. Agua no contaminada o condición normal")
        self.assertEqual(pozo.nno3_color, "#0000CD")

    def test_nno3_calidad_descripcion_and_color_are_ok_when_nno3_total_is_less_than_5(self):
        pozo = Pozo(nno3_total = uniform(0,5))
        self.assertEqual(pozo.nno3_calidad,"Potable - Excelente" )
        self.assertEqual(pozo.nno3_descripcion, "Agua potable. Agua no contaminada o condición normal")
        self.assertEqual(pozo.nno3_color, "#0000CD")

    def test_nno3_calidad_descripcion_and_color_are_ok_when_nno3_total_is_between_5_and_11(self):
        pozo = Pozo(nno3_total = uniform(5.1, 11))
        self.assertEqual(pozo.nno3_calidad,"Potable - Buena calidad" )
        self.assertEqual(pozo.nno3_descripcion, "Aguas con indicios de aguas residuales o fertilizantes." +
                         " Condición eutrófica-altos niveles de nutrientes. Efectos moderados en cultivos regados")
        self.assertEqual(pozo.nno3_color, "#40E0D0")

    def test_nno3_calidad_descripcion_and_color_are_ok_when_nno3_total_is_11(self):
        pozo = Pozo(nno3_total = 11)
        self.assertEqual(pozo.nno3_calidad,"Potable - Buena calidad" )
        self.assertEqual(pozo.nno3_descripcion, "Aguas con indicios de aguas residuales o fertilizantes." +
                         " Condición eutrófica-altos niveles de nutrientes. Efectos moderados en cultivos regados")
        self.assertEqual(pozo.nno3_color, "#40E0D0")

    def test_nno3_calidad_descripcion_and_color_are_ok_when_nno3_total_is_greater_than_11(self):
        pozo = Pozo(nno3_total = uniform(11.1, 30))
        self.assertEqual(pozo.nno3_calidad,"No apta como FAAP" )
        self.assertEqual(pozo.nno3_descripcion, "Aguas superficiales con fuerte impacto de aguas residuales" +
                         " crudas con alta carga de nutrientes. Condición hipertrófica, florecimientos algales"+
                         " que incluyen especies tóxicas a seres vivos")
        self.assertEqual(pozo.nno3_color, "#C70039")

    def test_as_calidad_descripcion_and_color_are_ok_when_as_total_is_None(self):
        pozo = Pozo(as_total = None)
        self.assertIs(pozo.as_calidad, None)
        self.assertEqual(pozo.as_descripcion, "No encontrado")
        self.assertEqual(pozo.as_color, "#D3D3D3")

    def test_as_calidad_descripcion_and_color_are_ok_when_as_total_is_0p01(self):
        pozo = Pozo(as_total = 0.01)
        self.assertEqual(pozo.as_calidad, "Potable - Excelente")
        self.assertEqual(pozo.as_descripcion, "Agua potable. Agua no contaminada o condición normal")
        self.assertEqual(pozo.as_color, "#0000CD")

    def test_as_calidad_descripcion_and_color_are_ok_when_as_total_is_less_than_0p01(self):
        pozo = Pozo(as_total = uniform(0, 0.01))
        self.assertEqual(pozo.as_calidad, "Potable - Excelente")
        self.assertEqual(pozo.as_descripcion, "Agua potable. Agua no contaminada o condición normal")
        self.assertEqual(pozo.as_color, "#0000CD")

    def test_as_calidad_descripcion_and_color_are_ok_when_as_total_is_between_0p01_and_0p025(self):
        pozo = Pozo(as_total = uniform(0.01, 0.025))
        self.assertEqual(pozo.as_calidad, "Apta como FAAP")
        self.assertEqual(pozo.as_descripcion, "Agua apta como fuente de abastecimiento de agua potable")
        self.assertEqual(pozo.as_color, "#40E0D0")

    def test_as_calidad_descripcion_and_color_are_ok_when_as_total_is_0p025(self):
        pozo = Pozo(as_total = 0.025)
        self.assertEqual(pozo.as_calidad, "Apta como FAAP")
        self.assertEqual(pozo.as_descripcion, "Agua apta como fuente de abastecimiento de agua potable")
        self.assertEqual(pozo.as_color, "#40E0D0")

    def test_as_calidad_descripcion_and_color_are_ok_when_as_total_is_greater_than_0p025(self):
        pozo = Pozo(as_total = uniform(0.026, 1))
        self.assertEqual(pozo.as_calidad, "No apta como FAAP")
        self.assertEqual(pozo.as_descripcion, "Agua no apta como fuente de abastecimiento de agua potable" +
                         " o requiere de tratamiento para su remoción")
        self.assertEqual(pozo.as_color, "#C70039")
#as_total
#cd_total
#cr_total
#hg_total
#pb_total
#mn_total
#fe_total
