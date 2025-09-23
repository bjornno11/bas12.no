from django.db import models

# Create your models here.

class Kunde(models.Model):
    navn = models.CharField(max_length=200)
    adresse = models.CharField(max_length=255, blank=True)
    telefon = models.CharField(max_length=20, blank=True)
    epost = models.EmailField(blank=True)
    organisasjonsnummer = models.CharField(max_length=20, blank=True)
    aktiv = models.BooleanField(default=True)

    def __str__(self):
        return self.navn
