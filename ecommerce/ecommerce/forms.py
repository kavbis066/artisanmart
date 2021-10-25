from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    firstname = forms.CharField(
                widget = forms.TextInput(
                    attrs = {
                        "class": 'form-control',
                        "placeholder": 'First Name...'
                    }
                )
    )

    lastname = forms.CharField(
                widget = forms.TextInput(
                    attrs = {
                        "class": 'form-control',
                        "placeholder": 'Last Name...' 
                    }
                )
    )

    email = forms.EmailField(
            widget = forms.EmailInput(
                attrs = {
                    "class": 'form-control',
                    "placeholder": 'Email: xyz@gmail.com'
                }
            )
    )

    password = forms.CharField(
                widget = forms.PasswordInput(
                    attrs = {
                        "class": 'form-control',
                        "placeholder": 'Password...'
                    }
                )
    )

    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname', 'password', 'email')
        help_texts = {
            'username': None,
        }
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not ("gmail.com") in email:
            raise forms.ValidationError("Email has to be gmail")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)