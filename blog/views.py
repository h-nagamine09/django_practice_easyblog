from ssl import HAS_TLSv1_1
from django.shortcuts import render,redirect
from blog.forms import CommentForm
from .models import Post

def frontpage(request):
    posts = Post.objects.all()
    return render(request,"blog/frontpage.html",{"posts":posts})#"posts"にposts変数の値を渡す

def post_detail(request,slug):
    post = Post.objects.get(slug=slug)#引数で渡ってきたslugとmodelのslugの値を照合して一致したらpost変数に値を代入する。
    if request.method == "POST":
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect("post_detail",slug=post.slug)
    else:
        form = CommentForm()
        
    return render(request,"blog/post_detail.html",{"post": post, "form":form})
#"post"にpost変数の値を渡してhtmlにrenderする