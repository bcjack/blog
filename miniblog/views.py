# Create your views here.
#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from miniblog.models import *
from miniblog.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def main_page(request):
    user = request.user
    styles = Style.objects.all()
    blogs = Blog.objects.all()
    return render_to_response('main_page.html',locals())

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            username = request.POST['username']
            password = request.POST['password']
            loginuser = authenticate(username=username, password=password)
            login(request, loginuser)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render_to_response('register_page.html', locals())

def content(request,blog_id):
    user = request.user
    blog = Blog.objects.get(id=blog_id)
    return render_to_response('content_page.html',locals())

@login_required(login_url='/login/')
def public(request):
    styles = Style.objects.all()
    user = request.user
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = BlogForm()
    return render_to_response('public_page.html', locals())

def style(request,style_id):
    user = request.user
    style = Style.objects.get(id=style_id)
    blogs = Blog.objects.filter(style=style)
    return render_to_response('style_page.html',locals())

@login_required(login_url='/login/')
def reply(request,blog_id):
    user = request.user
    blog = Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            form.author_id = u'1'
            rpl = form.save()
            blog.reply.add(rpl)
            blog.save()
            return HttpResponseRedirect('/content/'+blog_id)
    else:
        form = ReplyForm()
    return render_to_response('reply_page.html', locals())

@login_required(login_url='/login/')
def add_style(request):
    if request.method == 'POST':
        form = StyleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = StyleForm()
    return render_to_response('add_style.html', locals())

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

