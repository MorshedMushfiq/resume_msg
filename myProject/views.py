from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from App.models import *
from django.contrib import messages


def loginPage(req):
    if req.method == "POST":
        username = req.POST.get('uname')
        password = req.POST.get('pass')
        
        user = authenticate(username=username, password=password)
        if user:
            login(req, user)
            return redirect('home')
    
    
    
    return render(req, 'common/login.html')


def register(req):
    if req.method == "POST":
        username = req.POST.get('uname')
        email = req.POST.get('email')
        user_type = req.POST.get('user_type')
        password = req.POST.get('pass')
        confirm_password = req.POST.get('con_pass')
        
        if password == confirm_password:
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                user_type = user_type,
                password=confirm_password
            )
            messages.success(req, 'Registration Successful, Please Login')

            return redirect('login')
        
        else:
            messages.error(req, "Password and confirm password doesn't match")
            
    
    return render(req, 'common/register.html')




@login_required
def home(req):
    messages.success(req, "Login Success")
    return render(req, 'common/index.html')

def logoutPage(req):
    logout(req)
    return redirect('login')







