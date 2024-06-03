from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def auth(request):

    peoples = [
        {'name':'Shivam', 'age':22},
        {'name':'Abhishek', 'age':20},
        {'name':'Rohan', 'age':17},
        {'name':'Shoham', 'age':19},
        {'name':'Shyam', 'age':18},
        {'name':'Ram', 'age':16},
    ]
    # return HttpResponse("Hello You are at Auth page")
    return render(request, 'auth.html', {'peoples':peoples})

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if not user.exists():
            messages.error(request, "User not found!")
            return redirect('/auth/signin')

        user = authenticate(username=username, password=password)
        # print(user)

        if user is None:
            messages.error(request, "Incorrect Password!")
            return redirect('/auth/signin')
        else:
            login(request, user)
            return redirect(f'/receipe/user/{request.user}')

    return render(request, "signin/index.html")

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "Username already exists")
            return redirect('/auth/signup')

        if password == confirm_password:
            user = User.objects.create_user(
                first_name=first_name, 
                last_name=last_name,
                username=username, 
                email=email, 
            )
            user.set_password(password)  # for encryption of password
            user.save()
            
            messages.success(request, "User created successfully")
            return redirect("/auth/signin")

    return render(request, "signup/index.html")

def signout(request):
    logout(request)
    return redirect('/auth/signin')

def changepassword(request):
    return HttpResponse("Hello You are at Change Password page")

def profile(request):
    # return HttpResponse("Hello You are at Profile page")
    return render(request, "profile/index.html")
