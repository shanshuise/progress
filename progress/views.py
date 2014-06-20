#coding:utf-8

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.encoding import smart_str
from progress.models import Progress, User

def common_response(request):
    username = request.COOKIES.get('username', '')
    if username == '':
        login = False
    else:
        login = True
    commons = {
        "login": login,
    }
    return commons

def index(request):
    data = {}
    username = request.COOKIES.get('username', '')
    if username != '':
        user = User.objects.get(username=username)
        data['user'] = user
    data.update(common_response(request))
    return render(request, 'index.html', data)

def result(request):
    if request.method == "POST":
        username = request.COOKIES.get('username', '')
        user = User.objects.get(username=username)

        pname = request.POST.get('pname')
        pprogress = request.POST.get('pprogress')
        remark = request.POST.get('remark')

        Progress.objects.create(puser=user, pname=pname, pprogress=pprogress, remark=remark)
        return HttpResponseRedirect(reverse('result'))

    data = {}
    username = request.COOKIES.get('username', '')
    if username != '':
        user = User.objects.get(username=username)
        if user:
            progress = user.progress_set.all()
        else:
            progress = ''
        data['progress'] = progress
        data['user'] = user
        data.update(common_response(request))
        return render(request, 'result.html', data)
    else:
        error = u'你好像还没有登录'
        data['error'] = error
        data.update(common_response(request))
    return render(request, 'index.html', data)

def login(request):
    data = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            data['errors'] = u"用户名不存在"
            return render(request, 'login.html', data)
        user = User.objects.filter(username=username,password=password)
        if user is None:
            data['errors'] = u"登陆失败，用户名与密码不匹配"
            return render(request, 'login.html', data)
        else:
            response = HttpResponseRedirect(reverse('index'))
            response.set_cookie('username', smart_str(username), 3600)
            return response
        return ResponseRedirect(reverse('index'))
    else:
        return render(request, 'login.html', data)

def logout(request):
    response = HttpResponseRedirect(reverse('index'))
    response.delete_cookie("username")
    return response

def register(request):
    data = {}
    if request.method == 'GET':
        return render(request, 'register.html', data)
    elif request.method == 'POST':
        username = request.POST['username']
        department = request.POST['department']
        password = request.POST['password']
        password2 = request.POST['password2']

    if User.objects.filter(username=username).exists():
        data['errors'] = u"用户名不存在"
        return render(request, 'register.html', data)
    if password != password2 or password == '':
        data['errors'] = u"两次输入的密码不一致或为空"
        return render(request, 'register.html', data)

    user = User.objects.create(username=username,password=password,department=department)
    return HttpResponseRedirect(reverse('login'))
