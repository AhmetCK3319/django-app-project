from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models import Blog,Category 
data={
    'blogs':[
        {
            'id':1,
            'title':'Python Kursu',
            'is_active':True,
            'is_home':True,
            'descriptions':'bu djangoyu öğrenmek için uğraşacağım'
        },
        {
            'id':2,
            'title':'Django Kursu',
            'is_active':True,
            'is_home':True,
            'descriptions':'asla pes etmeyeceğim'
        },
        {
            'id':3,
            'title':'Bootstrap Kursu',
            'is_active':False,
            'is_home':False,
            'descriptions':'ne olursa olsun hergün çalış !!!'
        },
        {
            'id':4,
            'title':'Html Kursu',
            'is_active':False,
            'is_home':True,
            'descriptions':'ama hergün !!!'
        },
        {
            'id':5,
            'title':'Css Kursu',
            'is_active':False,
            'is_home':False,
            'descriptions':'bu en büyük hayalim !!!'
        },
    ]
}


def index(request):
    context={
        'blogs':Blog.objects.filter(is_home=True),
        'categories':Category.objects.all()
    }
    return render(request,'blogapp/index.html',context)

def blogs(request):
    context={
        'blogs':Blog.objects.filter(is_active=True),
        'categories':Category.objects.all()
    }
    return render (request,'blogapp/blogs.html',context)

def blogs_detail(request,slug):

    blog=Blog.objects.get(slug=slug)
    return render(request, 'blogapp/blogs-detail.html',{
        'blog': blog,
        
    })

def category_request(request,slug):
    context={
        'blogs':Category.objects.get(slug=slug).blog_set.all(), 
        'categories':Category.objects.all(),
        'category_selected':slug,
    }
    return render (request,'blogapp/blogs.html',context)