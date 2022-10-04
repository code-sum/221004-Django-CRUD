# ✅Django ModelForm I

> Form Class / ModelForm에 대한 이해
>
> ModelForm 구현
>
> CRUD 로직을 ModelForm으로 변경
>
> 1. 가상환경 및 Django 설치
> 2. articles app
> 3. Model 정의 (DB 설계)
> 4. CRUD 기능 구현



## 1. 가상환경 및 Django 설치

> 가상환경 설치하는 이유: 패키지를 별도로 가져가기 위해서

### 1-1. 가상환경 생성 및 실행

* 가상환경 폴더를 `.gitignore`로 설정을 해둔다.

```bash
$ python -m venv venv
$ source venv/Scripts/activate
(venv) $
```

### 1-2. Django 설치 및 기록

```
$ pip install django==3.2.13
$ pip freeze > requirements.txt
```

### 1-3. Django 프로젝트 생성

```bash
$ django-admin startproject pjt .
```



## 2. articles app 

### 2-1. app 생성

### 2-2. app 등록

### 2-3. urls.py 설정 



## 3. Model 정의 (DB 설계)

### 3-1. 클래스 정의

### 3-2. 마이그레이션 파일 생성

### 3-3. DB 반영(`migrate`)



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
