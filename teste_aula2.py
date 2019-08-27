import unittest
from aula2 import validar, tabela


class AutomatoFinitoTeste(unittest.TestCase):
    def test_deve_retornar_uma_string_valida(self):
        input = "e103e12e"
        result = validar(tabela, input)
        expected = [1, 0, 3, 'e', 1, 2, 'e']
        self.assertEqual(result, expected)

    def test_deve_retornar_uma_string_valida_depois_de_um_e_duplicado_no_final(self):
        input = "e103e12eee"
        result = validar(tabela, input)
        expected = [1, 0, 3, 'e', 1, 2, 'e']
        self.assertEqual(result, expected)

    def test_deve_retornar_uma_string_valida_depois_de_um_e_duplicado_no_comeco(self):
        input = "eee103e12e"
        result = validar(tabela, input)
        expected = [1, 0, 3, 'e', 1, 2, 'e']
        self.assertEqual(result, expected)

    def test_deve_retornar_uma_string_valida_com_sinal_positivo(self):
        input = "eee103e12e+23"
        result = validar(tabela, input)
        expected = [1, 0, 3, 'e', 1, 2, 'e', '+', 2, 3]
        self.assertEqual(result, expected)
