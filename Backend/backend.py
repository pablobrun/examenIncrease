'''
EXAMEN TECNICO INCREASE
Pablo Brun 2021

Requiere el archivo requests.py

Assert:
Sobre la cervecería resultante, verificar lo siguiente:
"id" = 761
"name" = "Lagunitas Brewing Co"
"street" = "1280 N McDowell Blvd"
"phone" = "7077694495"
'''

import unittest
from requests_cervecerias import requests_cervecerias

# Paso 4
# Con los resultados del paso 3 hago las comprobaciones pedidas
class TestCervecerias(unittest.TestCase):

    def test_cervecerias_id(self):
        self.assertEqual(requests_cervecerias.res_paso3[0]['id'], 761)

    def test_cervecerias_name(self):
        self.assertEqual(requests_cervecerias.res_paso3[0]['name'], 'Lagunitas Brewing Co')

    def test_cervecerias_street(self):
        self.assertEqual(requests_cervecerias.res_paso3[0]['street'], '1280 N McDowell Blvd')

    def test_cervecerias_phone(self):
        self.assertEqual(requests_cervecerias.res_paso3[0]['phone'], '7077694495')


if __name__ == '__main__':
    unittest.main()
