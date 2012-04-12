#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('dev.views',

    url(r'^test/$', 'test', name='url'),
    url(r'^cards/(?<x>.*)$', 'media', name='media'),
    )
