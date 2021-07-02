#!/usr/bin/env python
# -*- coding:utf-8 -*-

# created by wenyi.zhou on 26/4/2020
from django.conf.urls import patterns

from view import activity

urlpatterns = patterns(
	'',
	(r'^list/?$', activity.get_list),
	(r'^detail/?$', activity.get_detail),
	(r'^enter/list/?$', activity.enter_list),
	(r'^enter/cancel/?$', activity.enter_cancel),
	(r'^enter/add/?$', activity.enter_add),
	(r'^comment/list/?$', activity.comment_list),
	(r'^comment/add/?$', activity.comment_add)
)
