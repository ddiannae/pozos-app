from django.test import TestCase
from mapi.models import Pozo
from mapi.serializers import PozoSerializer
from random import uniform, choice, randrange
from string import ascii_letters

COLORES = ["#C70039", "#FF5733", "#FFC300", "#40E0D0", "#0000CD",  "#D3D3D3"]
NA_TEXT = "No encontrado"

def rand_char():
    return ''.join(choice(ascii_letters) for _ in range(randrange(1, 60)))

class PozoSerializerTests(TestCase):

    def setUp(self):

        self.pozo_attributes = {
            'clave': rand_char(),
            'sitio': rand_char(),
            'organismo': rand_char(),
            'estado': rand_char(),
            'municipio': rand_char(),
            'acuifero': rand_char(),
            'subtipo': choice(['POZO','NORIA','POZO NORIA','CENOTE',
                             'MANANTIAL','BOMBEO CENOTE','DESCARGA']),
            'lon': uniform(-117.15, -86.5),
            'lat': uniform(15.4, 32.56),
            #Cuando se implementen diferentes periodos, se tiene que cambiar
            'periodo': "2020",
            'alc_total': uniform(0, 1000),
            'conduct_total': uniform(0, 10000),
            'sdtm_total': uniform(0, 15000),
            'fluor_total': uniform(0, 10),
            'dur_total': uniform(0, 1000),
            'coli_total': uniform(0, 15000),
            'nno3_total': uniform(0, 30),
            'as_total': uniform(0, 1),
            'cd_total': uniform(0, 0.1),
            'cr_total': uniform(0, 0.5),
            'hg_total': uniform(0, 0.1),
            'pb_total': uniform(0, 0.1),
            'mn_total': uniform(0, 1),
            'fe_total': uniform(0, 1),
            'semaforo': choice(['Verde', 'Amarillo', 'Rojo'])
        }
        
        self.pozo_none_attributes = {
            'clave': rand_char(),
            'sitio': rand_char(),
            'organismo': rand_char(),
            'estado': rand_char(),
            'municipio': rand_char(),
            'acuifero': rand_char(),
            'subtipo': choice(['POZO','NORIA','POZO NORIA','CENOTE',
                             'MANANTIAL','BOMBEO CENOTE','DESCARGA']),
            'lon': uniform(-117.15, -86.5),
            'lat': uniform(15.4, 32.56),
            #Cuando se implementen diferentes periodos, se tiene que cambiar
            'periodo': "2020",
            'alc_total': None,
            'sdtm_total': None,
            'fluor_total': None,
            'nno3_total': None,
            'as_total': None,
            'cd_total': None,
            'cr_total': None,
            'hg_total': None,
            'pb_total': None,
            'mn_total': None,
            'fe_total': None,
            'semaforo': choice(['Verde', 'Amarillo', 'Rojo'])
        }
        self.pozo = Pozo.objects.create(**self.pozo_attributes)
        self.serializer = PozoSerializer(instance=self.pozo)

        self.pozo_none = Pozo.objects.create(**self.pozo_none_attributes)
        self.serializer_none = PozoSerializer(instance=self.pozo_none)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        contam = ["alc", "conduct",  "fluor", "dur", "coli", "nno3", "as", "cd", 
                 "cr", "hg", "pb", "mn", "fe"]
        fs = [c +"_"+ o for c in contam for o in ["total", "color", "descripcion"]] 
        fs += [c +"_"+ o for c in ["sdtm_ra", "sdtm_sal"] for o in ["color", "descripcion"]] 
        fs += ["sdtm_total", "semaforo", "estado", "municipio", "lon", "lat", "acuifero", 
               "sitio", "subtipo", "organismo"]
        self.assertEqual(set(data.keys()), set(fs)) 

    def test_estado_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['estado'], self.pozo_attributes['estado'])

    def test_municipio_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['municipio'], self.pozo_attributes['municipio'])

    def test_acuifero_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['acuifero'], self.pozo_attributes['acuifero'])

    def test_sitio_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['sitio'], self.pozo_attributes['sitio'])

    def test_subtipo_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['subtipo'], self.pozo_attributes['subtipo'])

    def test_organismo_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['organismo'], self.pozo_attributes['organismo'])

    def test_lon_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['lon'], self.pozo_attributes['lon'])

    def test_lat_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['lat'], self.pozo_attributes['lat'])

    def test_sdtm_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['sdtm_total'], float(self.pozo_attributes['sdtm_total']))
        self.assertIn(data['sdtm_sal_color'], COLORES) 
        self.assertIn(data['sdtm_ra_color'], COLORES) 
        self.assertIsInstance(data['sdtm_ra_descripcion'], str)
        self.assertIsInstance(data['sdtm_sal_descripcion'], str)

    def test_fluor_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['fluor_total'], float(self.pozo_attributes['fluor_total']))
        self.assertIn(data['fluor_color'], COLORES)
        self.assertIsInstance(data['fluor_descripcion'], str)

    def test_dur_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['dur_total'], float(self.pozo_attributes['dur_total']))
        self.assertIn(data['dur_color'], COLORES)
        self.assertIsInstance(data['dur_descripcion'], str)

    def test_alc_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['alc_total'], float(self.pozo_attributes['alc_total']))
        self.assertIn(data['alc_color'], COLORES)
        self.assertIsInstance(data['alc_descripcion'], str)

    def test_conduct_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['conduct_total'], float(self.pozo_attributes['conduct_total']))
        self.assertIn(data['conduct_color'], COLORES)
        self.assertIsInstance(data['conduct_descripcion'], str)

    def test_coli_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['coli_total'], float(self.pozo_attributes['coli_total']))
        self.assertIn(data['coli_color'], COLORES)
        self.assertIsInstance(data['coli_descripcion'], str)

    def test_nno3_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['nno3_total'], float(self.pozo_attributes['nno3_total']))
        self.assertIn(data['nno3_color'], COLORES)
        self.assertIsInstance(data['nno3_descripcion'], str)

    def test_as_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['as_total'], float(self.pozo_attributes['as_total']))
        self.assertIn(data['as_color'], COLORES)
        self.assertIsInstance(data['as_descripcion'], str)

    def test_cd_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['cd_total'], float(self.pozo_attributes['cd_total']))
        self.assertIn(data['cd_color'], COLORES)
        self.assertIsInstance(data['cd_descripcion'], str)

    def test_cr_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['cr_total'], float(self.pozo_attributes['cr_total']))
        self.assertIn(data['cr_color'], COLORES)
        self.assertIsInstance(data['cr_descripcion'], str)

    def test_hg_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['hg_total'], float(self.pozo_attributes['hg_total']))
        self.assertIn(data['hg_color'], COLORES)
        self.assertIsInstance(data['hg_descripcion'], str)

    def test_pb_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['pb_total'], float(self.pozo_attributes['pb_total']))
        self.assertIn(data['pb_color'], COLORES)
        self.assertIsInstance(data['pb_descripcion'], str)

    def test_mn_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['mn_total'], float(self.pozo_attributes['mn_total']))
        self.assertIn(data['mn_color'], COLORES)
        self.assertIsInstance(data['mn_descripcion'], str)

    def test_fe_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['fe_total'], float(self.pozo_attributes['fe_total']))
        self.assertIn(data['fe_color'], COLORES)
        self.assertIsInstance(data['fe_descripcion'], str)
        
    def test_sdtm_fields_content_when_null(self):
        data = self.serializer_none.data
        self.assertIs(data['sdtm_total'], None)
        self.assertEqual(data['sdtm_sal_color'], COLORES[-1]) 
        self.assertIn(data['sdtm_ra_color'], COLORES[-1]) 
        self.assertEqual(data['sdtm_ra_descripcion'], NA_TEXT)
        self.assertEqual(data['sdtm_sal_descripcion'], NA_TEXT)

    def test_fluor_fields_content_when_null(self):
        data = self.serializer_none.data
        self.assertIs(data['fluor_total'], None)
        self.assertEqual(data['fluor_color'], COLORES[-1])
        self.assertEqual(data['fluor_descripcion'], NA_TEXT)

    def test_dur_fields_content_when_null(self):
        data = self.serializer_none.data
        self.assertIs(data['dur_total'], None)
        self.assertEqual(data['dur_color'], COLORES[-1])
        self.assertEqual(data['dur_descripcion'], NA_TEXT)

    def test_alc_fields_content_when_null(self):
        data = self.serializer_none.data
        self.assertIs(data['alc_total'], None)
        self.assertEqual(data['alc_color'], COLORES[-1])
        self.assertEqual(data['alc_descripcion'], NA_TEXT)

    def test_conduct_fields_content_when_null(self):
        data = self.serializer_none.data
        self.assertIs(data['conduct_total'], None)
        self.assertEqual(data['conduct_color'], COLORES[-1])
        self.assertEqual(data['conduct_descripcion'], NA_TEXT)

    def test_coli_fields_content_when_null(self):
        data = self.serializer_none.data
        self.assertIs(data['coli_total'], None)
        self.assertEqual(data['coli_color'], COLORES[-1])
        self.assertEqual(data['coli_descripcion'], NA_TEXT)

    def test_nno3_fields_content_when_null(self):
        data = self.serializer_none.data
        self.assertIs(data['nno3_total'], None)
        self.assertEqual(data['nno3_color'], COLORES[-1])
        self.assertEqual(data['nno3_descripcion'], NA_TEXT)

    def test_as_fields_content_when_null(self):
        data = self.serializer_none.data
        self.assertIs(data['as_total'], None)
        self.assertEqual(data['as_color'], COLORES[-1])
        self.assertEqual(data['as_descripcion'], NA_TEXT)

    def test_cd_fields_content_when_null(self):
        data = self.serializer_none.data
        self.assertIs(data['cd_total'], None)
        self.assertEqual(data['cd_color'], COLORES[-1])
        self.assertEqual(data['cd_descripcion'], NA_TEXT)

    def test_cr_fields_content_when_null(self):
        data = self.serializer_none.data
        self.assertIs(data['cr_total'], None)
        self.assertEqual(data['cr_color'], COLORES[-1])
        self.assertEqual(data['cr_descripcion'], NA_TEXT)

    def test_hg_fields_content_when_null(self):
        data = self.serializer_none.data
        self.assertIs(data['hg_total'], None)
        self.assertEqual(data['hg_color'], COLORES[-1])
        self.assertEqual(data['hg_descripcion'], NA_TEXT)

    def test_pb_fields_content_when_null(self):
        data = self.serializer_none.data
        self.assertIs(data['pb_total'], None)
        self.assertEqual(data['pb_color'], COLORES[-1])
        self.assertEqual(data['pb_descripcion'], NA_TEXT)

    def test_mn_fields_content_when_null(self):
        data = self.serializer_none.data
        self.assertIs(data['mn_total'], None)
        self.assertEqual(data['mn_color'], COLORES[-1])
        self.assertEqual(data['mn_descripcion'], NA_TEXT)

    def test_fe_fields_content_when_null(self):
        data = self.serializer_none.data
        self.assertIs(data['fe_total'], None)
        self.assertEqual(data['fe_color'], COLORES[-1])
        self.assertEqual(data['fe_descripcion'], NA_TEXT)
