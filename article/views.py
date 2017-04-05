from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from article.models import ArticleModel

# Create your views here.
def home(request):
    return HttpResponse('Hello world, Django!')

def detail(request, param):
    return HttpResponse('detail parameter: %s' % param)

def article(request, id):
    a1 = ArticleModel.objects.get(id=int(id))
    return HttpResponse('title: %s<br>content: %s<br>' % (a1.title, a1.content))

def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})

def index(request):
    posts = ArticleModel.objects.all()
    return render(request, 'index.html', {'posts': posts})