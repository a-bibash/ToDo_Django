from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def app(request):
    if request.method == "POST":
        data = request.POST
        Task = data.get("Task")
        TODO.objects.create(
            Task=Task,
        )

    queryset = TODO.objects.all()
    context = {"Task": queryset}
    return render(request, "app.html", context)


def delete_Task(request, id):
    queryset = TODO.objects.get(id=id)
    queryset.delete()
    return redirect('/app')


def update_Task(request, id):
    queryset = TODO.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        Task = data.get("Task")
        queryset.Task = Task
        queryset.save()
        return redirect('/app')

    context = {"Task": queryset}

    return render(request, "update.html", context)
    context = {"Task": queryset}
    return render(request, "update.html", context)


def register(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already exists!")
            return redirect("/register")

        else:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
            )
        user.save()
        messages.success(request, "Account registerd successfully!")
        return redirect("login")

    return render(request, "register.html")


def login(request):
    return render(request, "login.html")
