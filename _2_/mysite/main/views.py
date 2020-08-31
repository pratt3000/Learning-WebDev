from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
# for forgot pass add email later in UserCreationForm, its not there by default
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def homepage(request):
    # to link html to the homepage 
    return render(request=request, template_name="main/home.html", context = {"tutorials": Tutorial.objects.all})

def register(request):
    # to register page
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account created : {username}")
            login(request, user)
            messages.info(request, f"you are now logged in as : {username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")

    form = UserCreationForm
    return render(request, "main/register.html", context = {"form" : form})