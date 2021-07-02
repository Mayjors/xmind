#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.forms import model_to_dict

from model.models.activity import ActivityTab, ActivityUserRelationTab
from model.models.user import UserTab, UserSecurityTab


def get_user_by_email(email):
	user = UserTab.objects.filter(email=email).first()
	return user


def create_user(info):
	user = UserTab(**info)
	user.save()
	return user


def login(name, password):
	user = UserSecurityTab.objects.filter(user_name=name, password=password).first()
	return user is not None


def load_user(name):
	user = UserTab.objects.filter(name=name).first()
	user = model_to_dict(user)
	return user


def list_activity_with_pagination(user, pageno, count):
	query = ActivityUserRelationTab.objects
	query = query.filter(delete_time=0, user_id=user.get('id'))
	total_count = query.count()
	query = query.values('id', 'activity_id')
	query = query[(pageno - 1) * count: pageno * count]
	activity_id_array = [q.get('activity_id') for q in query]

	query = ActivityTab.objects.filter(id__in=activity_id_array)
	return total_count, [model_to_dict(q) for q in query]


def get_user_by_ids(id_array):
	query = UserTab.objects.filter(id__in=id_array, delete_time=0)
	query = [model_to_dict(q) for q in query]
	return query
