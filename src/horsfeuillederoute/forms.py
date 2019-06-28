from django import forms
from .models import HorsFeuilleDeRoute


class HorsFeuilleDeRouteModelForm(forms.ModelForm):
    class Meta:
        model =  HorsFeuilleDeRoute
        fields = [
            'titre',
            'priorite',
            'etat',
            'status',
            'commentaire',
            'budget',
            'duree',
            'type',
        ]

        #def clean_title(self):