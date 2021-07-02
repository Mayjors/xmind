#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from django.views.decorators.csrf import csrf_exempt

from constant.ret_codes import Resp
from lib import defs
from lib.validator_utils import check_params
from manager import activity_manager
from model.jsonschema.activity import *


@csrf_exempt
@check_params(schema=ENTER_SAVE)
def enter_add(request, data):
	resp = activity_manager.enter_add(user=request.user, **data)
	return defs.response_data(resp)


@check_params(schema=COMMENT_OR_ENTER_LIST, method='GET')
def enter_list(request, data):
	pageno = data.get('pageno', 1)
	params = {
		'pageno': pageno,
		'count': data.get('count', 100),
		'activity_id': data.get('activity_id'),
	}
	total, data_list = activity_manager.list_enter_with_pagination(**params)
	return defs.response_list(Resp.RESP_OK, lists=data_list, extra=data, total=total, pageno=pageno)


@csrf_exempt
@check_params(schema=ENTER_SAVE)
def enter_cancel(request, data):
	resp = activity_manager.enter_cancel(user=request.user, **data)
	return defs.response_data(resp)


@csrf_exempt
@check_params(schema=COMMENT_ADD, method='POST')
def comment_add(request, data):
	resp, model = activity_manager.comment_add(user=request.user, **data)
	return defs.response_data(resp, model)


@check_params(schema=COMMENT_OR_ENTER_LIST, method='GET')
def comment_list(request, data):
	pageno = data.get('pageno', 1)
	params = {
		'pageno': pageno,
		'count': data.get('count', 100),
		'activity_id': data.get('activity_id'),
	}

	total, data_list = activity_manager.list_comment_with_pagination(**params)
	return defs.response_list(Resp.RESP_OK, lists=data_list, extra=data, total=total, pageno=pageno)


@check_params(schema=DETAIL, method='GET')
def get_detail(request, data):
	activity_id = data.get('activity_id')
	activity = activity_manager.get_activity(activity_id)
	return defs.response_data(Resp.RESP_OK, activity)


@check_params(schema=LIST, method='GET')
def get_list(request, data):
	pageno = data.get('pageno', 1)
	count = data.get('count', 100)
	min_datetime = data.get('min_datetime', int(time.time()))
	params = {
		'pageno': pageno,
		'count': count,
		'end_time__gte': min_datetime,
	}

	channel = data.get('channel')
	if channel:
		params['channel'] = channel
	max_datetime = data.get('max_datetime')
	if max_datetime:
		params['begin_time__lte'] = max_datetime

	total, data_list = activity_manager.list_activity_with_pagination(**params)
	return defs.response_list(Resp.RESP_OK, lists=data_list, extra=data, total=total, pageno=pageno)
