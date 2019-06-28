from django.db import models
from django.urls import reverse

# Create your models here.


class FeuilleDeRoute(models.Model):
    # id = models.IntegerField(primary_key=True)
    titre = models.CharField(max_length=128,default=1)
    #direction = models.CharField(max_length=32,blank=True, null=False)
    direction = models.ForeignKey('direction.direction', on_delete=models.CASCADE)
    # chef = models.CharField(max_length=30, default=1)
    chef = models.ForeignKey('membre.membre', on_delete=models.CASCADE)
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

    priorite= models.CharField(max_length=2, choices=PRIORITE_LIST, default=Priority1)
    etat = models.BooleanField(default=False)
    status = models.CharField(max_length=32, default=1)
    commentaire =  models.CharField(max_length=256, default=1)
    budget = models.DecimalField(max_digits=20, decimal_places=5)
    duree = models.CharField(max_length=32, default=2)

    FeuilleDeRoute = 'FeuilleDeRoute'
    HorsFeuilleDeRoute = 'HorsFeuilleDeRoute'

    TYPE_LIST = [
        (FeuilleDeRoute, 'FeuilleDeRoute'),
        (HorsFeuilleDeRoute, 'HorsFeuilleDeRoute'),
    ]

    type = models.CharField(max_length=32, choices=TYPE_LIST)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("feuillederoute:feuillederoute-detail", kwargs={"id": self.id})

    # class Meta:
    #     permissions = (
    #         ("view_fdr", "can see available fdr projects"),
    #         ("change_fdr","can edit fdr"),
    #         ("close_fdr", "can remove this project"),
    #                    )
