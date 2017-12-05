from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.


def auth(fn):
    def inner(request,*args,**kwargs):
        v = request.COOKIES.get('nid')
        if not v:
            return redirect('/zhihu/login/')
        print('通过了')
        return fn(request,*args,**kwargs)
    return inner


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        if request.POST.get('username'):
            u = request.POST.get('username')
            e = request.POST.get('email')
            p = request.POST.get('password')
            try:
                models.User.objects.create(username=u,email=e,password=p)
                return HttpResponse('OK')
            except:
                return HttpResponse('该邮箱已注册')
        else:
            e = request.POST.get('email_b')
            p = request.POST.get('password_b')
            if models.User.objects.filter(email=e,password=p):
                res = redirect('/zhihu/index/')
                nid = models.User.objects.filter(email=e,password=p).first().id
                print(nid)
                res.set_cookie('nid',nid)
                return res
            else:
                return HttpResponse('密码错误')

def index(request):
    nid = request.COOKIES.get('nid')
    user = models.User.objects.filter(id=nid).first()
    posts = models.Post.objects.all().order_by('-pub_time').values('u__email','title','body','id')
    print(posts)
    return render(request,'index.html',{'posts':posts,'user':user})


@auth
def edit_post(request):
    if request.method == 'GET':
        return render(request,'edit_post.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content= request.POST.get('content')
        nid = request.COOKIES.get('nid')
        models.Post.objects.create(title=title,body=content,u_id=nid)
        return HttpResponse('文章发布成功')

def post(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        uid = request.COOKIES.get('nid')
        user = models.User.objects.filter(id=uid).first()
        post = models.Post.objects.filter(id = nid).values('u__email','title','body','id').first()
        comments = models.comment.objects.filter(p_id=nid).values('u__email','body')
        return render(request,'post.html',{'post':post,'user':user,'comments':comments})
    if request.method =='POST':
        nid = request.POST.get('nid')
        uid = request.POST.get('uid')
        body = request.POST.get('body')
        models.comment.objects.create(body=body,u_id=uid,p_id=nid)
        url = '/zhihu/post/?nid=%s' % nid
        return redirect(url)

def out(request):
    nid = request.COOKIES.get('nid')
    res = redirect('/zhihu/index/')
    res.set_cookie('nid', nid,max_age=0)
    return res