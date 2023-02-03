from django.test import TestCase, Client
import json
from .models import Lot, Corral, Animal


class AnimalIngressViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.lot = Lot.objects.create(lot_number=1)
        self.corral = Corral.objects.create()

    def test_post_ingress(self):
        # Test indicando todos los datos correctos
        url = "/api/animals/income/"
        data = {
            "lote": 1,
            "ingresos": [
                {"corral": 1, "cantidad": 5},
            ],
        }
        response = self.client.post(
            url, data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Animal.objects.count(), 5)

    def test_post_ingress_no_lote(self):
        # Test sin indicar el lote
        url = "/api/animals/income/"
        data = {
            "ingresos": [
                {"corral": 1, "cantidad": 3},
            ]
        }
        response = self.client.post(
            url, data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Animal.objects.count(), 0)

    def test_post_ingress_no_ingresos(self):
        # Test sin el array de ingresos
        url = "/api/animals/income/"
        data = {
            "lote": 1,
        }
        response = self.client.post(
            url, data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Animal.objects.count(), 0)

    def test_post_ingress_corral_no_existe(self):
        # Test cuando el corral no existe
        url = "/api/animals/income/"
        data = {
            "lote": 1,
            "ingresos": [
                {"corral": 2, "cantidad": 3},
            ],
        }
        response = self.client.post(
            url, data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Animal.objects.count(), 0)

    def test_post_ingress_lote_no_existe(self):
        # Test cuando el lote no existe
        url = "/api/animals/income/"
        data = {
            "lote": 5,
            "ingresos": [
                {"corral": 1, "cantidad": 3},
            ],
        }
        response = self.client.post(
            url, data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 404)

    def test_post_ingress_corral_erroneo(self):
        # Test cuando el corral posee un dato no soportado
        url = "/api/animals/income/"
        data = {
            "lote": 5,
            "ingresos": [
                {"corral": "si", "cantidad": 3},
            ],
        }
        response = self.client.post(
            url, data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 404)

    def test_post_ingress_cantidad_erroneo(self):
        # Test cuando el ingreso posee un dato no soportado
        url = "/api/animals/income/"
        data = {
            "lote": 5,
            "ingresos": [
                {"corral": 1, "cantidad": "si"},
            ],
        }
        response = self.client.post(
            url, data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 404)

    def test_post_ingress_corral_ya_tiene_animales(self):
        # Test cuando el corral ya esta ocupado
        url = "/api/animals/income/"
        data = {
            "lote": 1,
            "ingresos": [
                {"corral": 1, "cantidad": 3},
            ],
        }
        self.client.post(url, data=json.dumps(data), content_type="application/json")
        response = self.client.post(
            url, data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 404)
