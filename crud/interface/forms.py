from django import forms
from .models import User

class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'