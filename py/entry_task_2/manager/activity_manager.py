#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.utils import get_timestamp
from django.forms import model_to_dict

from constant.ret_codes import Resp
from model.models.activity import ActivityTab, ActivityCommentTab, ActivityUserRelationTab
from model.models.activity_channel import ActivityChannelTab


def list_activity(order_by='-id', values=None, **kwargs):
	query = ActivityTab.objects
	if kwargs:
		query = query.filter(**kwargs)
	query = query.order_by(order_by)
	if values:
		query = query.values(*values)
	else:
		query = [model_to_dict(q) for q in query]
	return query


def list_activity_with_pagination(pageno, count, order_by='-id', values=None, **kwargs):
	query = ActivityTab.objects
	if kwargs:
		query = query.filter(**kwargs)
	query = query.filter(delete_time=0)
	total_count = query.count()
	query = query.order_by(order_by)
	if values:
		query = query.values(*values)
	query = query[(pageno - 1) * count: pageno * count]
	query = [model_to_dict(q) for q in query]
	return total_count, query


def get_activity(activity_id):
	query = ActivityTab.objects.filter(id=activity_id, delete_time=0).first()
	return model_to_dict(query) if query else None


def remove(activity_id, name, user):
	now = get_timestamp()
	values = {
		'delete_time': now,
		'modified_time': now,
		'modifier': user.get('name')
	}
	change_count = ActivityTab.objects.filter(id=activity_id, name=name).update(**values)
	return Resp.RESP_OK if change_count else Resp.RESP_ITEM_NOT_EXIST


def add(user, **activity):
	if ActivityTab.objects.filter(name=activity.get('name'), delete_time=0).exists():
		return Resp.RESP_ITEM_EXIST, None

	if not ActivityChannelTab.objects.filter(name=activity.get('channel'), delete_time=0).exists():
		return Resp.RESP_CHANNEL_NOT_EXIST, None

	now = get_timestamp()
	model = ActivityTab(**activity)
	model.created_time = now
	model.creator = user.get('name')
	model.modified_time = now
	model.modifier = user.get('name')
	model.save()
	return Resp.RESP_OK, model_to_dict(model)


def edit(user, **activity):
	query = ActivityChannelTab.objects.filter(name=activity.get('name'), delete_time=0)
	query = query.exclude(id=activity.get('id'))
	if query.exists():
		return Resp.RESP_ITEM_EXIST, None

	if not ActivityChannelTab.objects.filter(name=activity.get('channel'), delete_time=0).exists():
		return Resp.RESP_CHANNEL_NOT_EXIST, None

	now = get_timestamp()
	activity['modified_time'] = now
	activity['modifier'] = user.get('name')
	change_count = ActivityTab.objects.filter(id=activity.get('id'), delete_time=0).update(**activity)
	if change_count:
		model = ActivityTab.objects.filter(id=activity.get('id')).first()
		return Resp.RESP_OK, model_to_dict(model)
	else:
		return Resp.RESP_ITEM_NOT_EXIST, None


def update_channel(old_name, new_name):
	ActivityTab.objects.filter(channel=old_name, delete_time=0).update(channel=new_name)


def list_comment_with_pagination(pageno, count, activity_id):
	query = ActivityCommentTab.objects
	query = query.filter(delete_time=0)
	query = query.filter(activity_id=activity_id)
	total_count = query.count()
	query = query.order_by()
	query = query.values('id', 'content', 'created_time', 'creator')
	query = query[(pageno - 1) * count: pageno * count]
	query = [q for q in query]
	return total_count, query


def comment_add(user, **comment):
	if not ActivityTab.objects.filter(id=comment.get('activity_id'), delete_time=0).exists():
		return Resp.RESP_ITEM_NOT_EXIST, None

	now = get_timestamp()
	model = ActivityCommentTab(
		creator=user.get('name'),
		user_id=user.get('id'),
		activity_id=comment.get('activity_id'),
		content=comment.get('content'),
		created_time=now
	)
	model.save()
	return Resp.RESP_OK, model_to_dict(model)


def list_enter_with_pagination(pageno, count, activity_id):
	query = ActivityUserRelationTab.objects
	query = query.filter(delete_time=0)
	query = query.filter(activity_id=activity_id)
	total_count = query.count()

	query = query.order_by()
	query = query.values('id', 'user_id', 'created_time', 'creator')
	query = query[(pageno - 1) * count: pageno * count]
	query = [q for q in query]
	return total_count, query


def list_enter_with_offset(activity_id, limit=1000, id_offset=0):
	query = ActivityUserRelationTab.objects
	query = query.filter(delete_time=0, activity_id=activity_id, id__gt=id_offset)
	query = query.order_by('id')
	query = query.values('id', 'user_id', 'created_time', 'creator')
	query = query[0:limit]
	query = [q for q in query]
	return query


def enter_add(activity_id, user):
	if not ActivityTab.objects.filter(id=activity_id, delete_time=0).exists():
		return Resp.RESP_ITEM_NOT_EXIST
	try:
		model = ActivityUserRelationTab.objects.get(activity_id=activity_id, user_id=user.get('id'))
		model.delete_time = 0
		model.save()
	except ActivityUserRelationTab.DoesNotExist:
		model = ActivityUserRelationTab(
			user_id=user.get('id'),
			creator=user.get('name'),
			activity_id=activity_id,
			created_time=get_timestamp()
		)
		model.save()
	return Resp.RESP_OK


def enter_cancel(activity_id, user):
	now = get_timestamp()
	ActivityUserRelationTab.objects.filter(activity_id=activity_id, user_id=user.get('id')).update(delete_time=now)
	return Resp.RESP_OK
