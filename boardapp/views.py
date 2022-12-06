from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

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
            return render(request, 'signup.html', {})
    return render(request, 'signup.html', {})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

def listfunc(request):
    current_user = request.user
    username = request.user.get_username()
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {"object_list": object_list, "current_user": current_user, "username": username})

def logoutfunc(request):
    logout(request)
    return redirect('login')

@login_required
def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    username = request.user.get_username()
    current_user = request.user
    return render(request, "detail.html", {"object": object, "current_user": current_user, "username": username})

def goodfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    user = request.user.get_username()
    if user in object.good_user:
        object.good -= 1
        object.good_user = object.good_user.replace(user, "")
        object.save()
        return redirect("list")
    else:
        object.good = object.good + 1
        object.good_user = object.good_user + " " + user
        object.save()
        return redirect("list")

def readfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    username = request.user.get_username()
    if username in object.read_text:
        object.read -= 1
        object.read_text = object.read_text.replace(username, "")
        object.save()
        return redirect("list")
    else:
        object.read += 1
        object.read_text = object.read_text + " " + username
        object.save()
        return redirect("list")

def profilefunc(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, "profile.html", {"users": user})

class BoardCreate(CreateView):
    template_name = "create.html"
    model = BoardModel
    fields = ("title", "author", "content", "sns_image")
    success_url = reverse_lazy("list")

def deletefunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    username = request.user.get_username()
    if username == object.author:
        object.delete()
        return redirect("list")
    else:
        return redirect("list")
    
class BoardEdit(UpdateView):
    template_name = "edit.html"
    model = BoardModel
    fields = ("title", "content", "sns_image")
    
    def get_success_url(self):
        return reverse_lazy("detail", kwargs={"pk": self.kwargs["pk"]})
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author == request.user.get_username():
            return super().get(request, *args, **kwargs)
        else:
            current_user = request.user
            object = BoardModel.objects.all()
            return render(request, "list.html", {"object_list": object ,"error": "この投稿は編集できません", "current_user": current_user, "username": current_user.get_username() })