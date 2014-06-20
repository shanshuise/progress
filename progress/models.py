#coding:utf-8
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    department = models.CharField(max_length=10)

    def __unicode__(self):
        return self.username

class Progress(models.Model):
    puser = models.ForeignKey(User)
    pname = models.CharField(max_length=50)
    pprogress = models.CharField(max_length=50)
    remark = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.pname
