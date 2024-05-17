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
        return redirect('/')
    queryset = TODO.objects.all()
    context = {"Task": queryset}
    return render(request, "home.html", context)


def delete_Task(request, id):
    queryset = TODO.objects.get(id=id)
    queryset.delete()
    return redirect('/')
