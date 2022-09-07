from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError

from .models import BoardModel

# Create your views here.

def signupfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username, "", password)
            return redirect("login")
        except IntegrityError:
            return render(request, 'signup.html', {"error": "すでに作成されているユーザーです"})
    return render(request, 'signup.html', {"some": '100'})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'login.html', {"context": "ログインしました"})
        else:
            return render(request, 'login.html', {"context": "ログインできませんでした"})
    return render(request, 'login.html', {})

def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {"object_list": object_list})