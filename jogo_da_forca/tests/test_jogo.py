"""Testes das regras do Jogo da Forca."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from jogo import JogoDaForca  # noqa: E402


class BancoFalso:
    def __init__(self, entradas):
        self.entradas = iter(entradas)

    def sortear(self):
        return next(self.entradas)


class TestJogoDaForca(unittest.TestCase):
    def criar_jogo(self, palavra="CASA", maximo_erros=6):
        banco = BancoFalso([("TESTE", palavra)])
        return JogoDaForca(banco, maximo_erros)

    def test_acerto_revela_todas_as_ocorrencias(self):
        jogo = self.criar_jogo()

        self.assertEqual(jogo.tentar_letra("a"), "correta")
        self.assertEqual(jogo.palavra_oculta, "_ A _ A")
        self.assertEqual(jogo.erros, 0)

    def test_erro_reduz_uma_tentativa(self):
        jogo = self.criar_jogo()

        self.assertEqual(jogo.tentar_letra("x"), "incorreta")
        self.assertEqual(jogo.erros, 1)
        self.assertEqual(jogo.tentativas_restantes, 5)

    def test_tentativa_repetida_nao_conta_como_erro(self):
        jogo = self.criar_jogo()
        jogo.tentar_letra("x")

        self.assertEqual(jogo.tentar_letra("X"), "repetida")
        self.assertEqual(jogo.erros, 1)

    def test_letra_sem_acento_revela_letra_acentuada(self):
        jogo = self.criar_jogo("AÇAÍ")

        jogo.tentar_letra("c")
        jogo.tentar_letra("i")

        self.assertEqual(jogo.palavra_oculta, "_ Ç _ Í")

    def test_espaco_e_hifen_ficam_visiveis(self):
        jogo = self.criar_jogo("ARCO-ÍRIS")

        self.assertEqual(jogo.palavra_oculta, "_ _ _ _ - _ _ _ _")

    def test_vitoria_bloqueia_novas_jogadas(self):
        jogo = self.criar_jogo("OI")
        jogo.tentar_letra("o")
        jogo.tentar_letra("i")

        self.assertTrue(jogo.venceu)
        self.assertTrue(jogo.terminou)
        self.assertEqual(jogo.tentar_letra("x"), "invalida")

    def test_derrota_acontece_no_limite_de_erros(self):
        jogo = self.criar_jogo("A", maximo_erros=2)
        jogo.tentar_letra("x")
        jogo.tentar_letra("y")

        self.assertTrue(jogo.perdeu)
        self.assertEqual(jogo.tentativas_restantes, 0)

    def test_nova_partida_limpa_o_estado(self):
        banco = BancoFalso([("UMA", "CASA"), ("DUAS", "BOLA")])
        jogo = JogoDaForca(banco)
        jogo.tentar_letra("x")

        jogo.nova_partida()

        self.assertEqual(jogo.palavra, "BOLA")
        self.assertEqual(jogo.categoria, "DUAS")
        self.assertEqual(jogo.erros, 0)
        self.assertEqual(jogo.letras_tentadas, set())


if __name__ == "__main__":
    unittest.main()
