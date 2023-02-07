from django.test import TestCase
from .models import Encuesta

class EncuestaModelTests(TestCase):

    def test_total_vasos_is_0_when_vasos_is_0(self): 
        encuesta = Encuesta(vasos = 0)
        self.assertEqual(encuesta.total_vasos, 0)

