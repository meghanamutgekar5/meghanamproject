from django.core import validators
from django import forms
from .models import User


class EmployeeRegistration(forms.ModelForm):
  class Meta:
      model = User
      fields = ['name', 'email', 'password']  
      widgets ={
          'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Employee Name:'}),
          'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Employee Email:'}),
          'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control', 'placeholder':'Enter Employee password:'}),
      }