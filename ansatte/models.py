from django.db import models
from django.contrib.auth.models import User

class Rolle(models.Model):
    navn = models.CharField(max_length=100, unique=True)
    beskrivelse = models.TextField(blank=True, null=True)
    aktiv = models.BooleanField(default=True)
    opprettet_dato = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.navn


class Ansatt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roller = models.ManyToManyField(Rolle, blank=True)  # 👈 Knytter til Rolle
    aktiv = models.BooleanField(default=True)

    # Tilleggsfelter
    adresse = models.CharField(max_length=255, blank=True)
    telefon = models.CharField(max_length=20, blank=True)
    personnummer = models.CharField(max_length=20, blank=True)
    ansatt_dato = models.DateField(null=True, blank=True)
    kjonn = models.CharField(
        max_length=10,
        choices=[
            ("M", "Mann"),
            ("K", "Kvinne"),
            ("A", "Annet")
        ],
        blank=True
    )

    def __str__(self):
        return self.user.username
