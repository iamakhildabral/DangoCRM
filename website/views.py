from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        username_entered = request.POST['username']
        password_entered = request.POST['password']

        ## authenticating user
        user = authenticate(request, username= username_entered, password= password_entered)

        if user is not None:
            login(request,user)
            messages.success(request,"Welcome, You have been logged in!")
            return redirect('home')
        else:
            messages.success(request,"There has been an error loggin in , Please try again ")
            return redirect('home')
    return render(request, 'home.html',{})


def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out...")
    return redirect('home')

def register_user(request):
    return render(request,'register.html',{})