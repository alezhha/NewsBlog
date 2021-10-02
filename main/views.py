from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Posts
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def main(request):
    posts = Posts.objects.order_by("-created_at")
    return render(request, "index.html", {"posts":posts})

def newPost(request):
    posts = Posts.objects.all()
    return render(request, "makepost.html", {"posts":posts})

def makePost(request):
    if request.method == "POST":
        posts = Posts()
        posts.title = request.POST.get("title")
        posts.text = request.POST.get("text")
        posts.author = request.user
        posts.save()
    return HttpResponseRedirect("/")

def delete(request, id):
    try:
        post = Posts.objects.get(id = id)
        post.delete()
        return HttpResponseRedirect('/')
    except Posts.DoesNotExist:
        HttpResponseNotFound("<h2>Задача не найдена</h2>")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form":form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {"form":form})

def signout(request):
    logout(request)
    return render(request, 'postsPage.html')