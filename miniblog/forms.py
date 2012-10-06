#-*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from miniblog.models import *
import re

class StyleForm(forms.ModelForm):
	class Meta:
		model = Style

class ReplyForm(forms.ModelForm):
	class Meta:
		model = Reply
		fields = ['reply']

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		exclude = ['ptime','reply']

class RegisterForm(forms.ModelForm):
	repassword = forms.CharField(label=u'重复密码',widget=forms.PasswordInput())
	class Meta:
		model = User
		widgets = {'password': forms.PasswordInput()}
		fields = ['username','password','repassword','email']

	def clean_repassword(self):
		password = self.cleaned_data['password']
		repassword = self.cleaned_data['repassword']
		if password == repassword:
			return password
		raise forms.ValidationError('两次输入密码不匹配')

	def clean_username(self):
		username = self.cleaned_data['username']
		if not re.search(r'^\w+$', username):
			raise forms.ValidationError('用户名请用数字字母下划线')
		try:
			User.objects.get(username=username)
		except:
			return username
		raise forms.ValidationError('用户名已存在') 

