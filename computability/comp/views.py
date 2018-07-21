from django.shortcuts import render
from comp.models import Post

def index(request):
    user = request.user
    return render(request,"index.html",{"user": user, "problems": Post.objects.all()})