from django.shortcuts import render
from . import models


def index(request):
    tasks = models.Task.objects.all()
    return render(request, 'polls/main.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'polls/about.html')


def create(request):
    return render(request, 'polls/create.html')
