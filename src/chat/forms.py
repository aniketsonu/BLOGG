from django import forms
from .models import Chat


class UserForm(forms.ModelForm):
    class Meta:
        model = Chat
        widgets = {
            'password': forms.PasswordInput(),
        }
