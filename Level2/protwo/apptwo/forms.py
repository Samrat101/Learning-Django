from django import forms
from apptwo.models import user

class NewUserForm(forms.ModelForm):
    class Meta():
        model=user
        fields= '__all__'
