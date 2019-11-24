from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.db.models.query import QuerySet


class TestApp(TestCase):
    def test_banco(self) -> None:
        """
        Simples test para garantir que a conexão com o Postgres está sendo
        realizada corretamente.

        :return:
        """
        docs = User.objects.all()
        self.assertIsInstance(docs, QuerySet)

        User.objects.create_user('Djorge', 'nadaSegura')

        docs: QuerySet = User.objects.all()
        self.assertEqual(len(docs), 1)

    def test_endpoints(self) -> None:
        client = Client()
        res = client.get(path='/admin/')
        self.assertNotEqual(res.status_code, 500)
