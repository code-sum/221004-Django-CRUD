from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# 요청 정보를 받아서..
def index(request):

    # 원하는 페이지를 render..
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # DB에 저장하는 로직
    title = request.GET.get('title')
    content = request.GET.get('content')
    Article.objects.create(title=title, content=content)
    return redirect('articles:index')