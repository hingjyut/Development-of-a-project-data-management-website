from django.db import models
from django.urls import reverse

# Create your models here.


class Direction(models.Model):
    # id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=128,default=1)
    chef = models.CharField(max_length=30, default=1)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("direction:direction-detail", kwargs={"id": self.id})
