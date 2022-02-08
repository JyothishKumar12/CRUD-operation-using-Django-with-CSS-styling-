from django import forms
from.models import StudntRegistration

class StudentRegForm(forms.ModelForm):
    class Meta:
        model = StudntRegistration
        fields = ['name','email','department','mobno']
