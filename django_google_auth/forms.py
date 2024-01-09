from django import forms
from django_recaptcha.fields import ReCaptchaField

class Auth(forms.Form):
    username = forms.CharField(max_length=50, required=False)
    password = forms.CharField(max_length=50, required=False)
    captcha = ReCaptchaField()

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not username:
            self.add_error('username', 'Please enter username.')
        if not password:
            self.add_error('password', 'Please enter password.')