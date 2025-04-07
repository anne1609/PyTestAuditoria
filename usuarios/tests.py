# usuarios/tests.py

from django.test import TestCase

class MiPaginaTest(TestCase):
    def test_pagina_inicio(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
