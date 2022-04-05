from dataclasses import dataclass
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import Task

# Create your views here.

def index(request):
    data = Task.objects.all()
    return render(request, 'main/index.html', {'data' : data})

def login_user(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username = username, password = password)
        print(user)
        if user:
            login(request, user)
            return redirect('main:index')
    else:
        form = UserCreationForm()
        return render(request, 'registration/login.html', {'form' : form})

def add(request):
    if request.POST:
        data = request.POST
        new_task = Task()
        new_task.task_name = data['task_name']
        new_task.description = data['description']
        new_task.owner = request.user
        new_task.save()
        return redirect('main:index')
    else:
        return render(request, 'main/add.html')