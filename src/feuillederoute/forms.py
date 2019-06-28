from django import forms
from .models import FeuilleDeRoute

class FeuilleDeRouteModelForm(forms.ModelForm):
    class Meta:
        model =  FeuilleDeRoute
        fields = [
            'titre',
            'direction',
            'chef',
            'priorite',
            'etat',
            'status',
            'commentaire',
            'budget',
            'duree',
            'type',
        ]

        #def clean_title(self):
