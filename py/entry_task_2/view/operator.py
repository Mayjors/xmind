#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.decorators.csrf import csrf_exempt

from constant.ret_codes import Resp
from lib import defs, str_utils
from lib.exception import BusinessExceptionError
from lib.validator_utils import check_params
from manager import activity_channel_manager, activity_manager, user_manager, token_manager
from model.jsonschema import activity as activity_schema
from model.jsonschema import user as user_schema
from task import tasks as send_email_task


@csrf_exempt
@check_params(schema=user_schema.USER_LOGIN, method='POST')
def login(request, data):
	pwd = str_utils.generate_sha1(data["password"])
	success = user_manager.login(data["name"], pwd)
	if success:
		user = user_manager.load_user(data["name"])
		user["token"] = token_manager.generate_token(user, True)
		return defs.response_data(Resp.RESP_OK, user)

	raise BusinessExceptionError(Resp.RESP_LOGIN_FAILED)


@csrf_exempt
@check_params(schema=user_schema.SEND_EMAIL)
def send_email(request, data):
	send_email_task.send_email_to_user.delay(**data)
	return defs.response_data(Resp.RESP_OK)


@csrf_exempt
@check_params(schema=activity_schema.ADD)
def activity_add(request, data):
	resp, model = activity_manager.add(request.user, **data)
	return defs.response_data(resp, model)


@csrf_exempt
@check_params(schema=activity_schema.EDIT)
def activity_edit(request, data):
	resp, model = activity_manager.edit(request.user, **data)
	return defs.response_data(resp, model)


@csrf_exempt
@check_params(schema=activity_schema.REMOVE)
def activity_remove(request, data):
	resp = activity_manager.remove(user=request.user, **data)
	return defs.response_data(resp)


@csrf_exempt
@check_params(schema=activity_schema.CHANNEL_LIST)
def channel_list(request, data):
	pageno = data.get('pageno', 1)
	count = data.get('count', 100)
	params = {
		'pageno': pageno,
		'count': count
	}
	total, data_list = activity_channel_manager.list_with_pagination(**params)
	return defs.response_list(Resp.RESP_OK, lists=data_list, extra=data, total=total, pageno=pageno)


@csrf_exempt
@check_params(schema=activity_schema.CHANNEL_ADD)
def channel_add(request, data):
	resp, model = activity_channel_manager.add(request.user, **data)
	return defs.response_data(resp, model)


@csrf_exempt
@check_params(schema=activity_schema.CHANNEL_REMOVE)
def channel_remove(request, data):
	resp = activity_channel_manager.remove(request.user, **data)
	return defs.response_data(resp)


@csrf_exempt
@check_params(schema=activity_schema.CHANNEL_EDIT)
def channel_edit(request, data):
	resp, model, old_name = activity_channel_manager.edit(request.user, **data)
	if not old_name:
		activity_manager.update_channel(old_name, model.get('name'))
	return defs.response_data(resp, model)
