import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_toimii(self):
        transaktio = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(transaktio, 10)

    def test_syo_edullisesti_kateisella_ei_toimi(self):
        transaktio = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(transaktio, transaktio)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_syo_maukkaasti_kateisella_toimii(self):
        transaktio = self.kassapaate.syo_maukkaasti_kateisella(420)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(transaktio, 20)

    def test_syo_maukkaasti_kateisella_ei_toimi(self):
        transaktio = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(transaktio, transaktio)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_toimii(self):
        maksukortti = Maksukortti(1000)
        transaktio = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(transaktio, True)
        self.assertEqual(maksukortti.saldo, 760)

    def test_syo_edullisesti_kortilla_ei_toimi(self):
        maksukortti = Maksukortti(200)
        transaktio = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(transaktio, False)
        self.assertEqual(maksukortti.saldo, 200)

    def test_syo_maukkaasti_kortilla_toimii(self):
        maksukortti = Maksukortti(1000)
        transaktio = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(transaktio, True)
        self.assertEqual(maksukortti.saldo, 600)

    def test_syo_maukkaasti_kortilla_ei_toimi(self):
        maksukortti = Maksukortti(399)
        transaktio = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(transaktio, False)
        self.assertEqual(maksukortti.saldo, 399)

    def test_rahan_lataus_toimii(self):
        maksukortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 500)
        self.assertEqual(maksukortti.saldo, 1000)
    
    def test_rahan_lataus_ei_toimi(self):
        maksukortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -500)
        self.assertEqual(maksukortti.saldo, 500)