from django import forms

from .models import Membre


class MembreForm(forms.ModelForm):
    nom = forms.CharField(max_length=56)
    prenom = forms.CharField(max_length=56)
    direction = forms.CharField(max_length=56)
    class Meta:
        model = Membre
        fields = ['nom','prenom','direction','post']

    # def clean_nom(self,*arg,**kwargs):
    #     nom = self.cleaned_data.get("nom")
    #     if not "DISI" in nom:
    #         raise forms.ValidationError("This is not a valid title")
    #     else:
    #         return nom