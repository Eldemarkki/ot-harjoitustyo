import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_alkutila_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # Käteinen
    def test_edullinen_kateisosto_maksu_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(vaihtoraha, 760)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullinen_kateisosto_maksu_ei_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(50)
        self.assertEqual(vaihtoraha, 50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukas_kateisosto_maksu_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(vaihtoraha, 600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukas_kateisosto_maksu_ei_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(50)
        self.assertEqual(vaihtoraha, 50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    # Maksukortti
    def test_edullinen_korttiosto_maksu_riittava(self):
        kortti = Maksukortti(1000)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertTrue(onnistui)
        self.assertEqual(kortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_korttiosto_maksu_ei_riittava(self):
        kortti = Maksukortti(50)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertFalse(onnistui)
        self.assertEqual(kortti.saldo, 50)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_korttiosto_maksu_riittava(self):
        kortti = Maksukortti(1000)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertTrue(onnistui)
        self.assertEqual(kortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_korttiosto_maksu_ei_riittava(self):
        kortti = Maksukortti(50)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertFalse(onnistui)
        self.assertEqual(kortti.saldo, 50)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kassapaatteesta(self):
        kortti = Maksukortti(50)
        self.kassapaate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(kortti.saldo, 150)
    
    def test_negatiivinen_lataussumma_ei_muuta_maaraa(self):
        kortti = Maksukortti(50)
        self.kassapaate.lataa_rahaa_kortille(kortti, -20)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 50)
    
    def test_euromaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)