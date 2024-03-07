from django import forms 

from app.models import *


class userForm(forms.ModelForm):
    class Meta:

        model = userdetails

        fields = '__all__'
        

