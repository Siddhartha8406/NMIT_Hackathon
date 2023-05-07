from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as loginUser
from main.views import index as idx

def index(request):
    return render(request, 'index.html')

    
def login(request):
    if request.method == 'POST':
        x=request.POST['username']
        y=request.POST['password']
        user = authenticate(request, username=x, password=y)
        if user is not None:
            loginUser(request, user)
            return redirect('home')
    else:
        return redirect('index')

def signup(request):
    if request.method == 'POST':
        x=request.POST['username']
        y=request.POST['password']
        z=request.POST['group']
        print(x, y, z)
        grp = Group.objects.get(name=z)

        user = User.objects.create_user(username=x, password=y)
        user.save()

        user = authenticate(request, username=x, password=y)
        print(user)

        grp.user_set.add(user)
        return redirect('index')
    else:
        return render(request, 'signup.html')

def sign_up(request):
    print("request.POST")
    return HttpResponseRedirect(reverse('index'))