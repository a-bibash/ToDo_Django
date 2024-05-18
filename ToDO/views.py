from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.


def home(request):
    if request.method == "POST":
        data = request.POST
        Task = data.get("Task")
        TODO.objects.create(
            Task=Task,
        )

    queryset = TODO.objects.all()
    context = {"Task": queryset}
    return redirect('/')
    return render(request, "home.html", context)


def delete_Task(request, id):
    queryset = TODO.objects.get(id=id)
    queryset.delete()
    return redirect('/')


def update_Task(request, id):
    queryset = TODO.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        Task = data.get("Task")
        queryset.Task = Task
        queryset.save()
        from django.shortcuts import render, redirect


# Create your views here.


def home(request):
    if request.method == "POST":
        data = request.POST
        Task = data.get("Task")
        TODO.objects.create(
            Task=Task,
        )
        return redirect('/')
    queryset = TODO.objects.all()
    context = {"Task": queryset}
    
    return render(request, "home.html", context)


def delete_Task(request, id):
    queryset = TODO.objects.get(id=id)
    queryset.delete()
    return redirect('/')


def update_Task(request, id):
    queryset = TODO.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        Task = data.get("Task")
        queryset.Task = Task
        queryset.save()
        return redirect('/')

    context = {"Task": queryset}

    return render(request, "update.html", context)

    context = {"Task": queryset}

    return render(request, "update.html", context)
