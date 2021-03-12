from django.core import  validators
from django import forms
from .models import  User

class  StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
        }
        
        # file = forms.FieldField(widget=forms.FileInput(attrs={'class': 'rounded_list'}))
        
        
#         widgets = {
#     'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
#     'account_type': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'})
# }