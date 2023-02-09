from django.test import TestCase
from .forms import ContestarForm
from random import uniform, choice, randrange
from unittest import mock
from django.db.models import CharField
import uuid

class ContestarFormTest(TestCase):

    def setUp(self):
        agua_choices = ['llave','garrafon','filtro','hervida','otra']

        self.form_data = { 
            'edad': randrange(100),
            'peso': randrange(100),
            'vasos': randrange(10),
            'sexo': choice(["mujer", "hombre"]) ,
            'agua_cocinar': choice(agua_choices),
            'agua_tomar': choice(agua_choices),
            'cuidador': choice([True, False]),
            'lat': uniform(14.5, 32.56),
            'lon': uniform(-117.15, -86.5)
        }

    @mock.patch("captcha.fields.ReCaptchaField.validate")
    def test_form_is_valid_with_valid_data(self, validate_method):
        form = ContestarForm(self.form_data)
        validate_method.return_value = True
        self.assertTrue(form.is_valid())

    @mock.patch("captcha.fields.ReCaptchaField.validate")
    def test_form_is_invalid_with_no_edad(self, validate_method):
        self.form_data["edad"] = None
        form = ContestarForm(self.form_data)
        validate_method.return_value = True
        self.assertTrue(not form.is_valid())
        self.assertEqual(form.errors["edad"], ["This field is required."])

    @mock.patch("captcha.fields.ReCaptchaField.validate")
    def test_form_is_invalid_with_no_peso(self, validate_method):
        self.form_data["peso"] = None
        form = ContestarForm(self.form_data)
        validate_method.return_value = True
        self.assertTrue(not form.is_valid())
        self.assertEqual(form.errors["peso"], ["This field is required."])

    @mock.patch("captcha.fields.ReCaptchaField.validate")
    def test_form_is_invalid_with_no_vasos(self, validate_method):
        self.form_data["vasos"] = None
        form = ContestarForm(self.form_data)
        validate_method.return_value = True
        self.assertTrue(not form.is_valid())
        self.assertEqual(form.errors["vasos"], ["This field is required."])

    @mock.patch("captcha.fields.ReCaptchaField.validate")
    def test_form_is_invalid_with_no_sexo(self, validate_method):
        self.form_data["sexo"] = None
        form = ContestarForm(self.form_data)
        validate_method.return_value = True
        self.assertTrue(not form.is_valid())
        self.assertEqual(form.errors["sexo"], ["This field is required."])

    @mock.patch("captcha.fields.ReCaptchaField.validate")
    def test_form_is_invalid_with_no_agua_cocinar(self, validate_method):
        self.form_data["agua_cocinar"] = None
        form = ContestarForm(self.form_data)
        validate_method.return_value = True
        self.assertTrue(not form.is_valid())
        self.assertEqual(form.errors["agua_cocinar"], ["This field is required."])

    @mock.patch("captcha.fields.ReCaptchaField.validate")
    def test_form_is_invalid_with_no_agua_tomar(self, validate_method):
        self.form_data["agua_tomar"] = None
        form = ContestarForm(self.form_data)
        validate_method.return_value = True
        self.assertTrue(not form.is_valid())
        self.assertEqual(form.errors["agua_tomar"], ["This field is required."])

    @mock.patch("captcha.fields.ReCaptchaField.validate")
    def test_form_is_invalid_with_no_agua_cuidador(self, validate_method):
        self.form_data["cuidador"] = None
        form = ContestarForm(self.form_data)
        validate_method.return_value = True
        self.assertTrue(not form.is_valid())
        self.assertEqual(form.errors["cuidador"], ["This field is required."])

    @mock.patch("captcha.fields.ReCaptchaField.validate")
    def test_form_is_invalid_with_lower_latitude(self, validate_method):
        self.form_data["lat"] = uniform(-14.5, 14.4)
        form = ContestarForm(self.form_data)
        validate_method.return_value = True
        self.assertTrue(not form.is_valid())
        self.assertEqual(form.errors["lat"], ["Latitud inválida. Elige un punto dentro del territorio nacional."])

    @mock.patch("captcha.fields.ReCaptchaField.validate")
    def test_form_is_invalid_with_higher_latitude(self, validate_method):
        self.form_data["lat"] = uniform(32.57,60)
        form = ContestarForm(self.form_data)
        validate_method.return_value = True
        self.assertTrue(not form.is_valid())
        self.assertEqual(form.errors["lat"], ["Latitud inválida. Elige un punto dentro del territorio nacional."])

    @mock.patch("captcha.fields.ReCaptchaField.validate")
    def test_form_is_invalid_with_lower_longitud(self, validate_method):
        self.form_data["lon"] = uniform(-190,-117.14)
        form = ContestarForm(self.form_data)
        validate_method.return_value = True
        self.assertTrue(not form.is_valid())
        self.assertEqual(form.errors["lon"], ["Longitud inválida. Elige un punto dentro del territorio nacional."])

    @mock.patch("captcha.fields.ReCaptchaField.validate")
    def test_form_is_invalid_with_higher_longitud(self, validate_method):
        self.form_data["lon"] = uniform(-86.6,90)
        form = ContestarForm(self.form_data)
        validate_method.return_value = True
        self.assertTrue(not form.is_valid())
        self.assertEqual(form.errors["lon"], ["Longitud inválida. Elige un punto dentro del territorio nacional."])
