import unittest
import main


class PruebasAplicacion(unittest.TestCase):
    def setUp(self):
        main.registros.clear()
        self.client = main.app.test_client()

    def test_menu_principal(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn(b"Ejercicio 1", respuesta.data)
        self.assertIn(b"Ejercicio 2", respuesta.data)

    def test_ejercicio1_aprobado(self):
        respuesta = self.client.post("/ejercicio1", data={
            "nota1": "60", "nota2": "50", "nota3": "70", "asistencia": "80"
        }, follow_redirects=True)
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn(b"APROBADO", respuesta.data)
        self.assertIn(b"60.00", respuesta.data)

    def test_ejercicio1_reprobado_por_asistencia(self):
        respuesta = self.client.post("/ejercicio1", data={
            "nota1": "60", "nota2": "60", "nota3": "60", "asistencia": "74.9"
        }, follow_redirects=True)
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn(b"REPROBADO", respuesta.data)

    def test_ejercicio1_rechaza_nota_fuera_de_rango(self):
        respuesta = self.client.post("/ejercicio1", data={
            "nota1": "9", "nota2": "60", "nota3": "60", "asistencia": "80"
        })
        self.assertEqual(respuesta.status_code, 400)
        self.assertIn("Nota 1 debe estar entre".encode(), respuesta.data)

    def test_ejercicio2_nombre_mas_largo(self):
        respuesta = self.client.post("/ejercicio2", data={
            "nombre1": "Ana", "nombre2": "Cristobal", "nombre3": "Basti"
        }, follow_redirects=True)
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn(b"Cristobal", respuesta.data)
        self.assertIn(b"9 caracteres", respuesta.data)

    def test_ejercicio2_rechaza_nombres_repetidos(self):
        respuesta = self.client.post("/ejercicio2", data={
            "nombre1": "Ana", "nombre2": "ana", "nombre3": "Luis"
        })
        self.assertEqual(respuesta.status_code, 400)
        self.assertIn("tres nombres diferentes".encode(), respuesta.data)

    def test_resultado_inexistente(self):
        respuesta = self.client.get("/resultado/999")
        self.assertEqual(respuesta.status_code, 404)


if __name__ == "__main__":
    unittest.main()
