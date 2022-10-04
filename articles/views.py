from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# 요청 정보를 받아서..
def index(request):
    # 게시글을 가져와서..
    # (보통 게시판은 최신글이 맨위니까 .order_by('-pk') 활용)
    articles = Article.objects.order_by('-pk')
    # template 에 뿌려준다
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # DB에 저장하는 로직
    title = request.GET.get('title')
    content = request.GET.get('content')
    Article.objects.create(title=title, content=content)
    return redirect('articles:index')