from django.db import models
from ._validators import validate_ip
from .repositorio import RepositorioModel


class ServidorModel(models.Model):
    objects = models.Manager()
    ip = models.CharField(
        max_length=16,
        blank=False,
        validators=[validate_ip],
        unique=True,
    )
    dominio = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return self.ip

    def repositorios(self):
        return RepositorioModel.objects.filter(servidor=self.pk).values()
