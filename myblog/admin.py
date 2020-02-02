from django.contrib import admin
from myblog.views import Post, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)