from django.db import models
from ._validators import validate_ip


class ServidorModel(models.Model):
    ip = models.CharField(
        max_length=16,
        blank=False,
        validators=[validate_ip],
    )
    dominio = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return self.ip
