from django.db import models

# Create your models here.

class Membre(models.Model):
    nom = models.CharField(max_length=64)
    prenom = models.CharField(max_length=64)
    direction_id = models.ForeignKey('direction.direction', on_delete=models.CASCADE)
    Developpeur = 'Développeur'
    Chef = 'Chef'

    METIER_LIST = [
        (Developpeur,'Développeur'),
        (Chef , 'Chef'),
    ]

    post = models.CharField(max_length=64,choices=METIER_LIST)


    def __str__(self):
        return self.nom + ' '+self.prenom