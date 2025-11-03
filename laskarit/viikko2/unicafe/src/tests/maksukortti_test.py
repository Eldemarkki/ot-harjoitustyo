import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_on_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(self.maksukortti.saldo, 1500)
    
    def test_rahaa_ottaessa_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        result = self.maksukortti.ota_rahaa(300)
        self.assertEqual(self.maksukortti.saldo, 700)
        self.assertTrue(result)

    def test_rahaa_ottaessa_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        result = self.maksukortti.ota_rahaa(1400)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertFalse(result)
    
    def test_palauttaa_saldon_euroina_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_palauttaa_merkkijonon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")