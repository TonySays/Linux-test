from django.shortcuts import render, redirect
from django.http import HttpResponse
from requests import request
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login



def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"tutorials":Tutorial.objects.all})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request,user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

             

    form = UserCreationForm
    return render(request,
                  template_name = "main/register.html",
                  context={"form":form})


