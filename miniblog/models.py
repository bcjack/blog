#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Style(models.Model):
	style = models.CharField(u'类型',max_length=40)
	def __unicode__(self):
		return self.style

class Reply(models.Model):
	reply = models.TextField(u'回复')
	author = models.ForeignKey(User,verbose_name=u'回复人')
	def __unicode__(self):
		return self.author

class Blog(models.Model):
	title = models.CharField(u'标题',max_length=100)
	ptime= models.DateField(u'发布时间',auto_now=True)
	style = models.ForeignKey(Style,verbose_name=u'类型')
	author = models.ForeignKey(User,verbose_name=u'发帖人')
	content = models.TextField(u'内容')
	reply = models.ManyToManyField(Reply)
	def __unicode__(self):
		return self.title

class BlogAdmin(admin.ModelAdmin):
	list_display = ['title','ptime','author']
	list_filter = ['style']
	 

