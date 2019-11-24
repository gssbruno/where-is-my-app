from django.core.exceptions import ValidationError
from django.test import TestCase
from WhereIs.models import ServidorModel


class TestServidor(TestCase):
    def test_model(self) -> None:
        servidor = ServidorModel(ip='12.226.226.11', dominio='tre.com')
        servidor.save()
        servidor.delete()

    def test_ip_validation(self) -> None:
        with self.assertRaises(ValidationError):
            servidor = ServidorModel(ip='441.12.2.12')
            servidor.full_clean()
            servidor.save()
