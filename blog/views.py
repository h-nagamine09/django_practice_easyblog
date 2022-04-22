from ssl import HAS_TLSv1_1
from django.shortcuts import render
from .models import Post
def frontpage(request):
    posts = Post.objects.all()
    return render(request,"blog/frontpage.html",{"posts":posts})#"posts"にposts変数の値を渡す
