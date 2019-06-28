from django.db import models
from django.urls import reverse

# Create your models here.

class HorsFeuilleDeRoute(models.Model):

    titre = models.CharField(max_length=128,default=1)
    Priority1 = '1'
    Priority2 = '2'
    Priority3 = '3'
    Priority4 = '4'
    Priority5 = '5'

    PRIORITE_LIST = [
        (Priority1, '1'),
        (Priority2, '2'),
        (Priority3, '3'),
        (Priority4, '4'),
        (Priority5, '5'),
    ]

    priorite = models.CharField(max_length=2,choices=PRIORITE_LIST,default=Priority1)
    etat = models.BooleanField(default=False)
    status = models.CharField(max_length=32,default=1)
    commentaire = models.CharField(max_length=256,default=1)
    budget = models.DecimalField(decimal_places = 1, max_digits = 40,default=0)
    duree = models.CharField(max_length=32,default=2)
    type = models.CharField(max_length=32,default=1)

    def __str__(self):
        return self.titre

    # def get_absolute_url(self):
    #     return reverse("horsfeuillederoute:horsfeuillederoute-detail", kwargs={"id": self.id})
