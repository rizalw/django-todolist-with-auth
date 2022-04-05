from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

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