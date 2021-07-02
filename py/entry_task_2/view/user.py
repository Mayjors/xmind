#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt

from constant.ret_codes import Resp
from lib import defs
from lib import str_utils
from lib.validator_utils import check_params
from manager import user_manager, token_manager
from model.jsonschema.user import *


@csrf_exempt
@check_params(schema=USER_LOGIN)
def login(request, data):
	pwd = str_utils.generate_sha1(data["password"])
	success = user_manager.login(data["name"], pwd)
	if success:
		user = user_manager.load_user(data["name"])
		user["token"] = token_manager.generate_token(user)
		return defs.response_data(Resp.RESP_OK, user)
	else:
		return defs.response_data(Resp.RESP_LOGIN_FAILED, msg="登录用户名或者密码错误")


@csrf_exempt
@check_params(schema=USER_ACTIVITY_LIST)
def activity_list(request, data):
	pageno = data.get('pageno', 1)
	count = data.get('count', 100)
	params = {
		'pageno': pageno,
		'count': count
	}

	total, data_list = user_manager.list_activity_with_pagination(user=request.user, **params)
	return defs.response_list(Resp.RESP_OK, lists=data_list, extra=data, total=total, pageno=pageno)
