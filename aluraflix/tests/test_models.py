from django.test import TestCase
from aluraflix.models import Programa

class ProgramaModelTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo = 'Não achamos o Nemo em Russo',
            data_lancamento = '2012-07-04'
        )

    def test_verifica_atributos_do_programa(self):
        """Teste que verificar os atributos de um programa com valores default"""
        self.assertEqual(self.programa.titulo, 'Não achamos o Nemo em Russo')
        self.assertEqual(self.programa.tipo, 'F')
        self.assertEqual(self.programa.data_lancamento, '2012-07-04')
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)
        

