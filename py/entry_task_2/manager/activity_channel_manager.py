#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.utils import get_timestamp
from django.forms import model_to_dict

from constant.ret_codes import Resp
from model.models.activity_channel import ActivityChannelTab


def add(user, **channel):
	if ActivityChannelTab.objects.filter(name=channel.get('name'), delete_time=0).exists():
		return Resp.RESP_ITEM_EXIST, None
	now = get_timestamp()
	model = ActivityChannelTab(**channel)
	model.created_time = now
	model.creator = user.get('name')
	model.save()
	return Resp.RESP_OK, model_to_dict(model)


def list_with_pagination(pageno, count):
	query = ActivityChannelTab.objects
	query = query.filter(delete_time=0)
	total_count = query.count()
	query = query.order_by()
	query = query[(pageno - 1) * count: pageno * count]
	query = [model_to_dict(q) for q in query]
	return total_count, query


def remove(user, channel_id, name):
	now = get_timestamp()
	values = {
		'delete_time': now,
		'modified_time': now,
		'modifier': user.get('name')
	}
	change_count = ActivityChannelTab.objects.filter(id=channel_id, name=name).update(**values)
	return Resp.RESP_OK if change_count else Resp.RESP_ITEM_NOT_EXIST


def edit(user, channel_id, name):
	query = ActivityChannelTab.objects.filter(name=name, delete_time=0)
	query = query.exclude(id=channel_id)
	if query.exists():
		return Resp.RESP_ITEM_EXIST, None, None

	model = ActivityChannelTab.objects.filter(id=channel_id, delete_time=0).first()
	if not model:
		return Resp.RESP_ITEM_NOT_EXIST, None, None

	old_name = model.name
	now = get_timestamp()
	model.name = name
	model.created_time = now
	model.creator = user.get('name')
	model.save()
	return Resp.RESP_OK, model_to_dict(model), old_name
