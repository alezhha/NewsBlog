from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Posts

# Create your views here.
def main(request):
    posts = Posts.objects.all()
    return render(request, "index.html", {"posts":posts})

def makePost(request):
    posts = Posts()
    posts.title = request.POST.get("title")
    posts.text = request.POST.get("text")
    if request.POST.get("author") == "":
        posts.author = "Anonymus"
    else:
        posts.author = request.POST.get("author")
    posts.save()
    return HttpResponseRedirect("/")