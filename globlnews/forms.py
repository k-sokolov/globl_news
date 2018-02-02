from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Fieldset


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, min_length=4, label=("Email"))
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'email',
            'password1',
            'password2',
            ButtonHolder(Submit('register', 'Register', css_class='btn-primary'))
        )

#    class Meta:
#        fields = ('username', 'email', 'password1', 'password2')




class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            ButtonHolder(Submit('login', 'Login', css_class='btn-primary'))
        )

