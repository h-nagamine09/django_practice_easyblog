from django.contrib import admin
from django.urls import path
from blog.views import frontpage,post_detail #blogフォルダのViews.pyの中のfrontpage関数をimportしている

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage),#/を叩いたらviews.pyのfrontpage関数を読む
    path('<slug:slug>/',post_detail, name="post_detail")
]
