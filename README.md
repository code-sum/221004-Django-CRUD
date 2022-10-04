# ✅Django ModelForm I

> Form Class / ModelForm에 대한 이해
>
> ModelForm 구현
>
> CRUD 로직을 ModelForm으로 변경
>
> 1. 가상환경 및 Django 설치
> 2. articles app 생성 및 등록
> 3. Model 정의 (DB 설계)
> 4. CRUD 기능 구현



## 1. 가상환경 및 Django 설치

> 가상환경 설치하는 이유 : 프로젝트마다 패키지를 별도로 가져가야하기 때문
>
> 가상환경 생성 및 실행하기 전에 .gitignore 파일, README.md 파일을 먼저 추가해놓고, 아래 명령어로 변경내역 추적 시작하기
>
> 이 때 .gitignore 파일에 가상환경 폴더를 써두어야함(`/venv`)
>
> `$ git init` 👉 `$ git add .` 👉 `$ git commit -m 'init'`

### 1-1. 가상환경 생성 및 실행

```bash
$ python -m venv venv
$ source venv/Scripts/activate
(venv)
```

### 1-2. Django 설치 및 기록

```bash
# upgrade pip
$ python -m pip install --upgrade pip

# install Django 
$ pip install django==3.2.13

# 내가 활용하고 있는 패키지들 기록지에 남기기
$ pip freeze > requirements.txt
```

### 1-3. Django 프로젝트 생성

```bash
# 현재 위치(.)에 pjt 라는 이름의 프로젝트를 생성
$ django-admin startproject pjt .

# 서버 실행되는지 확인
$ python manage.py runserver
```

### 1-4. 프로젝트 추가 설정(internationalization)

> 다국어 지원은 django i18n 검색 결과 참조

```python
# pjt/settings.py 하단으로 내려가서

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC' 부분을 아래와 같이 변경

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```



## 2. articles app 생성 및 등록

> 기본적인 CRUD 기능이 동작하는 게시판 앱 만들기
>
> 앱은 MTV 패턴으로 제작
>
> 앱을 생성하기 위해, 위에서 실행하고 있던 서버를 잠깐 종료(`ctrl` + `c`)

### 2-1. app 생성

```bash
$ python manage.py startapp articles
```

### 2-2. app 등록

```python
# pjt/settings.py 에서

# INSTALLED_APPS = [] 괄호 내 최상단에 아래와 같이 생성한 앱 등록

INSTALLED_APPS = [
    'articles',
    ...,
]
```

### 2-3. urls.py 설정 

#### 2-3-1. urls.py 분리 작업

> url 관리를 각 앱에서 관리할 수 있도록, include 활용해 분리하기

```python
# 먼저 pjt/urls.py 에서

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

```python
# articles/urls.py 생성하고,
# urlpatterns = [] 이런 식으로 빈 리스트 선언해야 서버 실행이 됨

urlpatterns = [
    
]
```

```python
# articles/urls.py 에서 아래와 같이 코드 계속 작성

from django.urls import path

app_name = 'articles'

urlpatterns = [

]
```

#### 2-3-2. index.html 생성

> 기본 순서 : URL - VIEW - TEMPLATE
>
> - url 을 등록하고, view 함수 생성, template 만든다
> - URL 을 요청 받아서, 처리하고 응답해주는게 Django 의 근본이니까 위와 같은 순서로 작업

```python
# articles/urls.py 에서 아래와 같이 path 채워넣기

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # 아래 주소에 들어오면 어떤 화면을 보여줄지
    # 생각하면서 path 를 작성 ...
    # http://127.0.0.1:8000/articles/
    path('', views.index, name='index'),
]
```

```python
# articles/views.py 에서 index 함수 생성

from django.shortcuts import render

# Create your views here.

# 요청 정보를 받아서..
def index(request):

    # 원하는 페이지를 render..
    return render(request, 'articles/index.html')
```

```django
<!-- articles/templates/articles 폴더 생성 후 
     폴더 최하단에 index.html 생성 -->

<body>
    <h1>안녕!</h1>
</body>

<!-- 여기까지 작성 후,
     http://127.0.0.1:8000/articles/ 접속했을때
     서버 정상적으로 실행되는지 확인 -->
```



## 3. Model 정의 (DB 설계)

> SW개발에서 UI 기능 / DB 는 서로 밀접한 연관을 맺고 있음
>
> CRUD 를 만든다는 것은 DB의 생성, 수정, 삭제를 고려해야 하는 것이므로, CRUD 로 넘어가기 전에 모델 정의가 선행되어야함

### 3-1. 클래스 정의

```python
# articles/models.py 에 모델 설계

from django.db import models

# Create your models here.

'''
게시판 기능
- 제목(20글자이내)
- 내용(긴 글)
- 글 작성시간 / 글 수정시간(자동으로 기록, 날짜/시간)
'''

# 1. 모델 설계 (=DB 스키마 설계)
# Article 은 models 에 있는 Model 을 상속 받음
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 2. 설계한 모델을 DB에 반영
```

### 3-2. 마이그레이션 파일 생성

```bash
$ python manage.py makemigrations
```

### 3-3. DB 반영 (`migrate`)

```bash
$ python manage.py migrate
```

### 3-4. DB 반영 잘 되었는지 Django 에서 확인

```bash
$ python manage.py showmigrations

# 이때 articles [X] 0001_initial 생성되어있으면 DB 반영된 것임
```





## 4. CRUD 기능 구현

### 4-1. 게시글 생성

> 사용자에게 HTML Form 제공, 입력받은 데이터를 처리 (ModelForm 로직으로 변경)

#### 4-1-1. HTML Form 제공

> http://127.0.0.1:8000/articles/new/

#### 4-1-2. 입력받은 데이터 처리

> http://127.0.0.1:8000/articles/create/

> 게시글 DB에 생성하고 index 페이지로 redirect

### 4-2. 게시글 목록

> DB에서 게시글을 가져와서, template에 전달

### 4-3. 상세보기

> 특정한 글을 본다.

> http://127.0.0.1:8000/articles/<int:pk>/

### 4-4. 삭제하기

> 특정한 글을 삭제한다.

> http://127.0.0.1:8000/articles/<int:pk>/delete/

### 4-5. 수정하기

> 특정한 글을 수정한다. => 사용자에게 수정할 수 양식을 제공하고(GET) 특정한 글을 수정한다.(POST)

> http://127.0.0.1:8000/articles/<int:pk>/update/
