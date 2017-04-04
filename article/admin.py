from django.contrib import admin

# Register your models here.
from django.contrib import admin
from article.models import ArticleModel

admin.site.register(ArticleModel)