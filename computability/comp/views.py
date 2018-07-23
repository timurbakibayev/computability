from django.shortcuts import render
from comp.models import Post

latexify = lambda x: x.replace("$","\$")

def index(request):
    user = request.user
    latex_posts = Post.objects.all()
    for post in latex_posts:
        post.title = latexify(post.title)
        post.text = latexify(post.text)
        post.abstract = latexify(post.abstract)

    return render(request,"index.html",{"user": user, "problems": latex_posts})


def almaty2018(request):
    user = request.user
    return render(request,"almaty2018.html",{"user": user})
