from django.shortcuts import render
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
    return render(request, "home.html")
