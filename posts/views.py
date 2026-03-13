
from django.shortcuts import render,redirect,get_object_or_404
from .models import Post

def home(request):
    posts=Post.objects.all().order_by("-created")
    if request.method=="POST":
        content=request.POST.get("content")
        if request.user.is_authenticated:
            Post.objects.create(author=request.user,content=content)
            return redirect("/")
    return render(request,"posts/home.html",{"posts":posts})

def like_post(request,id):
    post=get_object_or_404(Post,id=id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect("/")
