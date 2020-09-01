from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import  AuthenticationForm
# for forgot pass add email later in UserCreationForm, its not there by default
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

# to link html to the homepage 
def homepage(request):
    return render(request=request, template_name="main/home.html", context = {"tutorials": Tutorial.objects.all})

def register(request):
    # to register page
    if request.method == "POST":
        form = NewUserForm(request.POST)
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

    form = NewUserForm
    return render(request, "main/register.html", context = {"form" : form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out succesfully")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) #mentioning username= & password= is necessary
            if user is not None:
                login(request, user) #order of arguements is crucial, pass request first always
                messages.info(request, f"you are now logged in as : {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username/password")
        else:   
            messages.error(request, "Invalid username/password")

    form = AuthenticationForm()
    return render(
        request,
        "main/login.html",
        {"form":form}
    )    