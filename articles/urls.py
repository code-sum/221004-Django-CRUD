# URL 설정을 app 단위로!
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # 아래 주소에 들어오면 어떤 화면을 보여줄지
    # 생각하면서 path 를 작성 ...
    # http://127.0.0.1:8000/articles/
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/articles/new/
    # path('new/', views.new, name='new'),
    # http://127.0.0.1:8000/articles/create/
    path('create/', views.create, name='create'),
    # http://127.0.0.1:8000/articles/1/ : 1번글
    # http://127.0.0.1:8000/articles/3/ : 3번글
    path('<int:pk>/', views.detail, name='detail'),
    # http://127.0.0.1:8000/articles/1/update : 1번글 수정
    # http://127.0.0.1:8000/articles/3/update : 3번글 수정
    path('<int:pk>/update', views.update, name='update'),
]