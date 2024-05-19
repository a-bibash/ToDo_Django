from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

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
    return render(request, "register.html")


def login(request):
    return render(request, "login.html")
