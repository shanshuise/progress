#coding:utf-8
from django.db import models

class Progress(models.Model):
    PROGRESS_CHOICES = (
        (u'1', u'正在编制')
        (u'2', u'初稿已完成')
        (u'3', u'正在审后修改')
        (u'2', u'终稿已完成')
    )
    puser = models.ForeignKey(User)
    pname = models.CharField(max_length=50)
    pprogress = models.CharField(max_length=50, choices=PROGRESS_CHOICES)
    remark = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.puser

class User(models.Model):
    DEPARTMENT_CHOICES = (
        (u'1', u'一所')
        (u'2', u'二所')
        (u'3', u'三所')
    )
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    deparment = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES)

    def __unicode__(self):
        return self.username
