#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('dev.views',

    url(r'^test/$', 'test', name='url'),
    url(r'^init/$', 'game_init', name='init'),
    url(r'^action/$', 'action', name='action'),
    url(r'^status/$', 'status', name='status'),
    url(r'css_test/$', 'css_test', name='css-test'),
    url(r'^(?P<role>.*)/$', 'play_page', name='role'),
    )
