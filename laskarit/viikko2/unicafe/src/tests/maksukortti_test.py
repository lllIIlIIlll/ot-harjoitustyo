import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_lataus_vaikuttaa_saldoon_oikein(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")
    
    def test_saldo_vahenee_oikein_jos_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_vahene_jos_ei_tapeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_onnistuiko_rahan_otto(self):
        onnistunut_rahan_otto = self.maksukortti.ota_rahaa(1200)
        self.assertEqual(onnistunut_rahan_otto, False)

    def test_rahan_otto_epaonnistuu(self):
        onnistunut_rahan_otto = self.maksukortti.ota_rahaa(100)
        self.assertEqual(onnistunut_rahan_otto, True)