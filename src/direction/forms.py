from django import forms

from .models import Direction


class DirectionForm(forms.ModelForm):
    nom = forms.CharField(max_length=56)
    chef = forms.CharField(max_length=56)
    class Meta:
        model = Direction
        fields = ['nom','chef']

    def clean_nom(self,*arg,**kwargs):
        nom = self.cleaned_data.get("nom")
        if not "DISI" in nom:
            raise forms.ValidationError("This is not a valid title")
        else:
            return nom