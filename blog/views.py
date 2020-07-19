from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Blog
# Create your views here.

def home(request):
    blogs=Blog.objects  #쿼리셋:데이터베이스로부터 받은정보 표시-->메소드
    return render(request,'home.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id) #pk=primary key||객체들의 이름표,구분자,데이터의 대표값,
                #이용자가 원한 몇번 블로그 객체
    return render(request,'detail.html',{'blog':blog_detail})

def new(request):
    return render(request,'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

    #쿼리셋과 메소드의 형식
    #모델 이름.쿼리셋(dbjects).메소드