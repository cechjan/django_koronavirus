from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib import messages
import json
import requests as rq
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.sites import requests
from django.http import HttpResponse, HttpResponseRedirect


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            captcha_token = request.POST.get("g-recaptcha-response")
            cap_url = "https://www.google.com/recaptcha/api/siteverify"
            cap_secret = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'
            cap_data = {"secret": cap_secret, "response": captcha_token}
            cap_server_response = rq.post(url=cap_url, data=cap_data)
            cap_json = json.loads(cap_server_response.text)

            if cap_json['success'] == False:
                messages.error(request, "Invalid Captcha Try Again")
                print("Invalid Captcha")
            elif cap_json['success'] == True:
                print("Valid Captcha")
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return HttpResponseRedirect("../../koronavirus/")

    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
