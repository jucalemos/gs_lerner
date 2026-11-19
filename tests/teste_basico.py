import unittest
from base_conhecimento import BaseConhecimento, normalizar
from orientacao import Orientacao
from energia import AnaliseEnergia


class TesteLerner(unittest.TestCase):
    def setUp(self):
        self.base = BaseConhecimento("data/base_conhecimento.json")
        self.base.carregar()

    def test_normalizar_remove_acentos_e_maiusculas(self):
        self.assertEqual(normalizar("ÁRVORE!"), " arvore ")

    def test_base_tem_mais_de_dez_orientacoes(self):
        self.assertGreaterEqual(len(self.base.orientacoes), 10)

    def test_base_tem_tres_categorias(self):
        self.assertGreaterEqual(len(self.base.categorias()), 3)

    def test_busca_retorna_tuplas(self):
        resultados = self.base.buscar("Como descartar entulho em um ecoponto?")
        self.assertIsInstance(resultados, list)
        self.assertIsInstance(resultados[0], tuple)
        self.assertIsInstance(resultados[0][1], Orientacao)

    def test_ecoponto_recebe_pontuacao(self):
        resultados = self.base.buscar("Como descartar entulho em um ecoponto?")
        self.assertGreaterEqual(resultados[0][0], 3)

    def test_consumo_anual_led_120w(self):
        energia = AnaliseEnergia()
        self.assertTrue(energia.carregar())
        consumo, custo = energia.calcular(120)
        self.assertAlmostEqual(consumo, 525.6, places=2)
        self.assertAlmostEqual(custo, 228.19, places=2)

    def test_consumo_anual_sodio_310w(self):
        energia = AnaliseEnergia()
        self.assertTrue(energia.carregar())
        consumo, custo = energia.calcular(310)
        self.assertAlmostEqual(consumo, 1357.8, places=2)
        self.assertAlmostEqual(custo, 589.50, places=2)


if __name__ == "__main__":
    unittest.main()
