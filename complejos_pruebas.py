import complejos3001 as lcp
import unittest


class TestcplxOperations(unittest.TestCase):

    def test_sumac(self):
        suma = lcp.sumac(c1=(5, 1.8), c2=(3, -5.6))
        self.assertAlmostEqual(suma[0], 8)
        self.assertAlmostEqual(suma[1], -3.8)

        suma = lcp.sumac(c1=(3, 9), c2=(-2, 6))
        self.assertAlmostEqual(suma[0], 1)
        self.assertAlmostEqual(suma[1], 15)

    def test_multic(self):
        multip = lcp.multic(c1=(5, 1.8), c2=(3, -5.6))
        self.assertAlmostEqual(multip[0], 25.08)
        self.assertAlmostEqual(multip[1], -22.6)

        multip = lcp.multic(c1=(3, 9), c2=(-2, 6))
        self.assertAlmostEqual(multip[0], -60)
        self.assertAlmostEqual(multip[1], 0)

    def test_restc(self):
        resta = lcp.restc(c1=(5, 1.8), c2=(3, -5.6))
        self.assertAlmostEqual(resta[0], 2)
        self.assertAlmostEqual(resta[1], 7.4)

        resta = lcp.restc(c1=(9, 8), c2=(-5, 2))
        self.assertAlmostEqual(resta[0], 5)
        self.assertAlmostEqual(resta[1], 3)

    def test_divic(self):
        divis = lcp.divic(c1=(1.8, 2), c2=(6, -4.6))
        self.assertAlmostEqual(divis[0], 0.12, places=1)
        self.assertAlmostEqual(divis[1], 0.82, places=1)

        divis = lcp.divic(c1=(-3, 9), c2=(2, 6))
        self.assertAlmostEqual(divis[0], 1.2)
        self.assertAlmostEqual(divis[1], -0.9)

    def test_moduc(self):
        modulo = lcp.moduc((4,9))
        self.assertAlmostEqual(modulo, 6.40, places=1)

        modulo = lcp.moduc(3,5)
        self.assertAlmostEqual(modulo, 8.24, places=1)

    def test_conjuc(self):
        conjugado = lcp.conjuc((-4,-5))
        self.assertAlmostEqual(conjugado[0], 4)
        self.assertAlmostEqual(conjugado[1], -5)

        conjugado = lcp.conjuc(1,6)
        self.assertAlmostEqual(conjugado[0], 2)
        self.assertAlmostEqual(conjugado[1], 8)

    def test_fasec(self):
        fase = lcp.fasec(3,2)
        self.assertAlmostEqual(fase, 0.89, places=1)

        fase = lcp.fasec(20,7)
        self.assertAlmostEqual(fase, 1.32, places=1)

    def test_geomc(self):
        geomet = lcp.geomc(5, 4)
        self.assertAlmostEqual(geomet[0], 4.0, places=1)
        self.assertAlmostEqual(geomet[1], 4.99, places=1)

        geomet = lcp.geomc(9, 2)
        self.assertAlmostEqual(geomet[0], 1.99, places=1)
        self.assertAlmostEqual(geomet[1], 8.0, places=1)


if __name__ == '__main__':
    unittest.main()