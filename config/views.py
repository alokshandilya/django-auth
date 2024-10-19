from django import forms
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    # User model to interact with the form
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# register a user
def registration_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)  # form data
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = RegisterForm()  # empty form

    context = {"form": form}

    return render(request, "registration/register.html", context)


# home page
def index(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    return redirect("login")


@login_required
def profile(request):
    context = {"user": request.user}
    return render(request, "profile.html", context)
