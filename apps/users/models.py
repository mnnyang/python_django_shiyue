# coding=utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default='')
    avator = models.ImageField(upload_to='upload/avator/%Y%m', default='avator/default.png', max_length=100)

    gender = models.IntegerField(choices=((0, u'男'), (1, u'女')), default=1)
    blogurl = models.CharField(max_length=100, default=u'')

    class Meta:
        verbose_name = '用户体'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
