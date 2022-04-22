from django.db import models

# マイグレーションファイルの作成
# Postテーブルの作成
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug= models.SlugField()
    intro = models.TextField()
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)