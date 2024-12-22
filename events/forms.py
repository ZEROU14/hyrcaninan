from django import forms
from .models import Event_SignUp

class SignUpForm(forms.ModelForm):

    class Meta:
        model = Event_SignUp
        fields = ['name', 'last_name', 'Id_pic', 'insurance_pic','paid_pic', 'phone_number', 'category']
        