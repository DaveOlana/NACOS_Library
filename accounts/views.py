from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import StudentRegistrationForm
from library.models import StudentProfile


def register(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password1"]
            )

            StudentProfile.objects.create(
                user=user,
                school=form.cleaned_data["school"],
                department=form.cleaned_data["department"],
                level=form.cleaned_data["level"]
            )

            login(request, user)
            return redirect("dashboard")
    else:
        form = StudentRegistrationForm()

    return render(request, "accounts/register.html", {"form": form})
