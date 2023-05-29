from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):


    def setUp(self) -> None:
        self.programa = Programa(
            titulo = 'Não achamos o Nemo em Russo',
            data_lancamento = '2012-07-04',
            tipo='F',
            likes=2340,
            dislikes=40
        )

        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verifica_campos_serializados(self):
        """Teste que verifica se os campos estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['titulo', 'data_lancamento', 'tipo', 'likes']))

    def test_verifica_conteudo_dos_campso_serializados(self):
        """Teste que verifica conteudo dos campos serialziados"""
        data = self.serializer.data
        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['likes'], self.programa.likes)
