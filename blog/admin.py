from django.contrib import admin
from .models import Post,Comment #同じ階層のmodels.pyの中のPost関数を呼び出す

admin.site.register(Post) #管理画面でPost関数を呼び出してデータ登録できるようにする
admin.site.register(Comment)