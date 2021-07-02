#!/usr/bin/env python
# -*- coding:utf-8 -*-

# created by wenyi.zhou on 26/4/2020
from django.conf.urls import patterns

from view import operator

urlpatterns = patterns(
	'',
	(r'^login/?$', operator.login),
	(r'^send_email/?$', operator.send_email),
	(r'^activity/add/?$', operator.activity_add),
	(r'^activity/edit/?$', operator.activity_edit),
	(r'^activity/remove/?$', operator.activity_remove),
	(r'^channel/list/?$', operator.channel_list),
	(r'^channel/add/?$', operator.channel_add),
	(r'^channel/remove/?$', operator.channel_remove),
	(r'^channel/edit/?$', operator.channel_edit),
)
