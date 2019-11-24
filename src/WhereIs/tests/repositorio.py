from django.test import TestCase
from WhereIs.models import RepositorioModel


class TestRepositorioModel(TestCase):
    def test_model(self) -> None:
        rep = RepositorioModel(
            nome='RepTest',
            descricao='Uma descrição longa',
            link='http://nodomain.com',
        )

        rep.save()
        self.assertEqual(1, rep.pk)
        res = rep.delete()
        self.assertEqual(res[0], 1)
