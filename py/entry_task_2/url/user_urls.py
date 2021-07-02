#!/usr/bin/env python
# -*- coding:utf-8 -*-

# created by wenyi.zhou on 26/4/2020
from django.conf.urls import patterns

from view import user

urlpatterns = patterns(
	'',
	(r'^login/?$', user.login),
	(r'^activity_list/?$', user.activity_list)
)
