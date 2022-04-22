from django.db import models

# マイグレーションファイルの作成
# Postテーブルの作成
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug= models.SlugField()
    intro = models.TextField()
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post =models.ForeignKey(Post ,related_name = "comments",on_delete=models.CASCADE) #1対多　on_deleteは関連データを一緒に消す
    name =models.CharField(max_length=255)
    email=models.EmailField()
    description =models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)