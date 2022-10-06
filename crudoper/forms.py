from .models import Bird,BirdFamily
from django import forms

class BirdForm(forms.ModelForm):
    class Meta:
        model = Bird
        fields = "__all__"


class BirdFamilyForm(forms.ModelForm):
    class Meta:
        model = BirdFamily
        fields = "__all__"

        