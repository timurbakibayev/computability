from django.shortcuts import render
from comp.models import Post

latexify = lambda x: x.replace("$","\$")

def index(request):
    user = request.user
    latex_posts = Post.objects.filter(type="open")
    for post in latex_posts:
        post.title = latexify(post.title)
        post.text = latexify(post.text)
        post.abstract = latexify(post.abstract)

    return render(request,"index.html",{"user": user, "problems": latex_posts,
                                        "title": "Open Problems"})


def almaty2018abstracts(request):
    user = request.user
    latex_posts = Post.objects.filter(type="workshop")
    for post in latex_posts:
        post.title = latexify(post.title)
        post.text = latexify(post.text)
        post.abstract = latexify(post.abstract)

    return render(request,"index.html", {"user": user, "problems": latex_posts,
                                        "title": "Abstracts for Workshop on Computability Problems"})


def almaty2018(request):
    user = request.user
    return render(request,"almaty2018.html",{"user": user})


def almaty2018venue(request):
    user = request.user
    return render(request,"almaty2018venue.html",{"user": user})

def almaty2018participants(request):
    user = request.user
    return render(request,"almaty2018participants.html",{"user": user})

def almaty2018program(request):
    user = request.user
    return render(request,"almaty2018program.html",{"user": user})

def almaty2018orgcom(request):
    user = request.user
    return render(request,"almaty2018orgcom.html",{"user": user})

