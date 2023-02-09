from django.test import TestCase
from .utils import RiesgoStat
from .models import Encuesta

class RiesgoStatTest(TestCase):
        
    def setUp(self):
        self.encuesta_data = { 
            'edad': 50,
            'peso': 50,
            'vasos': 5,
            'sexo': "",
            'agua_cocinar': "",
            'agua_tomar': "",
            'cuidador': False,
            'lat': 20,
            'lon': -110 
        }

        self.pozo_data = {
            'cd_total' : 0.1, 
            'cr_total' : 0.1, 
            'hg_total' : 0.1, 
            'mn_total' : 0.1, 
            'as_total' : 0.1, 
            'fluor_total' : 0.1, 
        }
        self.encuesta = Encuesta.objects.create(**self.encuesta_data)

    def test_riesgo_cd_is_None_when_cd_total_is_None(self):
        self.pozo_data['cd_total'] = None
        riesgo = RiesgoStat(self.encuesta, self.pozo_data)
        self.assertTrue(riesgo.riesgo_cd is None)

    def test_riesgo_cd_is_correct(self):
        riesgo = RiesgoStat(self.encuesta, self.pozo_data)
        exp = (self.pozo_data['cd_total'] * self.encuesta.total_vasos)/self.encuesta_data['peso']
        self.assertEqual(riesgo.riesgo_cd, round(exp/riesgo.CD_REF, 4))

    def test_riesgo_cr_is_None_when_cr_total_is_None(self):
        self.pozo_data['cr_total'] = None
        riesgo = RiesgoStat(self.encuesta, self.pozo_data)
        self.assertTrue(riesgo.riesgo_cr is None)

    def test_riesgo_cr_is_correct(self):
        riesgo = RiesgoStat(self.encuesta, self.pozo_data)
        exp = (self.pozo_data['cr_total'] * self.encuesta.total_vasos)/self.encuesta_data['peso']
        self.assertEqual(riesgo.riesgo_cr, round(exp/riesgo.CR_REF, 4))

    def test_riesgo_hg_is_None_when_hg_total_is_None(self):
        self.pozo_data['hg_total'] = None
        riesgo = RiesgoStat(self.encuesta, self.pozo_data)
        self.assertTrue(riesgo.riesgo_hg is None)

    def test_riesgo_hg_is_correct(self):
        riesgo = RiesgoStat(self.encuesta, self.pozo_data)
        exp = (self.pozo_data['hg_total'] * self.encuesta.total_vasos)/self.encuesta_data['peso']
        self.assertEqual(riesgo.riesgo_hg, round(exp/riesgo.HG_REF, 4))

    def test_riesgo_mn_is_None_when_mn_total_is_None(self):
        self.pozo_data['mn_total'] = None
        riesgo = RiesgoStat(self.encuesta, self.pozo_data)
        self.assertTrue(riesgo.riesgo_mn is None)

    def test_riesgo_mn_is_correct(self):
        riesgo = RiesgoStat(self.encuesta, self.pozo_data)
        exp = (self.pozo_data['mn_total'] * self.encuesta.total_vasos)/self.encuesta_data['peso']
        self.assertEqual(riesgo.riesgo_mn, round(exp/riesgo.MN_REF, 4))

    def test_riesgo_as_ca_is_None_when_as_ca_total_is_None(self):
        self.pozo_data['as_total'] = None
        riesgo = RiesgoStat(self.encuesta, self.pozo_data)
        self.assertTrue(riesgo.riesgo_as_ca is None)

    def test_riesgo_as_ca_is_correct(self):
        riesgo = RiesgoStat(self.encuesta, self.pozo_data)
        exp = (self.pozo_data['as_total'] * self.encuesta.total_vasos)/self.encuesta_data['peso']
        self.assertEqual(riesgo.riesgo_as_ca, round(exp/riesgo.AS_REF_CA, 4))

    def test_riesgo_as_der_is_None_when_as_total_is_None(self):
        self.pozo_data['as_total'] = None
        riesgo = RiesgoStat(self.encuesta, self.pozo_data)
        self.assertTrue(riesgo.riesgo_as_der is None)

    def test_riesgo_as_der_is_correct(self):
        riesgo = RiesgoStat(self.encuesta, self.pozo_data)
        exp = (self.pozo_data['as_total'] * self.encuesta.total_vasos)/self.encuesta_data['peso']
        self.assertEqual(riesgo.riesgo_as_der, round(exp/riesgo.AS_REF_DER, 4))

    def test_riesgo_fluor_is_None_when_fluor_total_is_None(self):
        self.pozo_data['fluor_total'] = None
        riesgo = RiesgoStat(self.encuesta, self.pozo_data)
        self.assertTrue(riesgo.riesgo_fl is None)

    def test_riesgo_fluor_is_correct(self):
        riesgo = RiesgoStat(self.encuesta, self.pozo_data)
        exp = (self.pozo_data['fluor_total'] * self.encuesta.total_vasos)/self.encuesta_data['peso']
        self.assertEqual(riesgo.riesgo_fl, round(exp/riesgo.FLUOR_REF, 4))
