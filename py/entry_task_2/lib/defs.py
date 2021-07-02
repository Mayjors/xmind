#!/usr/bin/env python
# -*- coding:utf-8 -*-

import simplejson as json
from django.http import HttpResponse

from constant.ret_codes import Resp
from lib.resp_status import RespStatus


def response_data(resp_status, data=None, msg=None):
	if not isinstance(resp_status, RespStatus):
		return response_data(Resp.RESP_INVALID_INTERNAL_PARAMS, msg=str(resp_status))
	from lib.str_utils import safe_convert_to_string
	resp_d = {
		"retcode": resp_status.code,
		"message": resp_status.msg if not msg else safe_convert_to_string(msg),
		"data": data or {}
	}
	return HttpResponse(json.dumps(resp_d), content_type='application/json; charset=utf-8')


def response_parms_error(request, message=None):
	return response_data(Resp.RESP_INVALID_PARAMS, msg=message)


def response_list(resp_status, lists, extra=None, message=None, total=0, pageno=0, count=10):
	res = {
		"pageno": pageno,
		"count": count,
		"total": total,
		"list": lists if lists else []
	}
	if extra:
		res["extra"] = extra
	return response_data(resp_status, data=res, msg=message)


class ExceptionResp(Exception):
	def __init__(self, *args, **kwargs):
		if len(args) == 1 and isinstance(args[0], RespStatus):
			self.resp = args[0]
