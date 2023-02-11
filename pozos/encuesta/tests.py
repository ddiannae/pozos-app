from django.test import TestCase
from .models import Encuesta
from random import randrange

class EncuestaModelTests(TestCase):

    def test_total_vasos_is_0_when_vasos_is_0(self): 
        encuesta = Encuesta(vasos = 0)
        self.assertEqual(encuesta.total_vasos, 0)

    def test_total_vasos_is_ok_with_random(self):
        vasos = randrange(15)
        encuesta = Encuesta(vasos = vasos)
        self.assertEqual(encuesta.total_vasos, (vasos*250)/1000)

