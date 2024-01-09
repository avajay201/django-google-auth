from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, logout, authenticate
from django.conf  import settings
import requests
import json

def verify_captcha(captcha):
    print(captcha)
    data = {
        'secret': settings.SECRET_KEY,
        'response': captcha
    }
    res = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    res = json.loads(res.content)
    print(res)
    return res['success']

def auth(request):
    if request.method == 'POST':
        auth_form = forms.Auth(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('auth')
    else:
        auth_form = forms.Auth()
    return render(request, 'index.html', {'auth_form': auth_form})

def logout1(request):
    logout(request)
    return redirect('auth')