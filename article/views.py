from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from article.models import ArticleModel

def home(request):
    return HttpResponse('Hello world, Django!')

def detail(request, param):
    return HttpResponse('detail parameter: %s' % param)

def article(request, id):
    a1 = ArticleModel.objects.get(id=int(id))
    return HttpResponse('title: %s<br>content: %s<br>' % (a1.title, a1.content))