from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

class Personnes(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    age = models.IntegerField()
    commentaire = models.TextField()
    photo = models.ImageField()

    def __str__(self):
        return f'{self.photo} {self.nom} {self.prenom} {self.ville} {self.age}'

class Objets(models.Model):
    nom = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return f'{self.image} {self.nom} {self.ville}'
