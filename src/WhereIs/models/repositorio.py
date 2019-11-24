from django.db import models
from .servidor import ServidorModel


class RepositorioModel(models.Model):
    objects = models.Manager()
    nome = models.CharField(max_length=50, blank=False)
    descricao = models.TextField(blank=True)
    link = models.URLField(blank=False)
    servidor = models.ForeignKey(
        ServidorModel,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self) -> None:
        return self.nome
