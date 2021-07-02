# -*- coding:utf-8 -*-
from lib.resp_status import RespStatus


class Resp(object):
	RESP_OK = RespStatus(0, "")
	RESP_INVALID_INTERNAL_PARAMS = RespStatus(-1, "invalid internal params")
	RESP_INVALID_PARAMS = RespStatus(-10, "invalid params")
	RESP_NOT_LOGGED_IN = RespStatus(-100, "not logged in")
	RESP_LOGIN_FAILED = RespStatus(-101, "login failed")

	RESP_ITEM_EXIST = RespStatus(-600, 'item exist')
	RESP_ITEM_NOT_EXIST = RespStatus(-601, 'item not exist')

	RESP_CHANNEL_NOT_EXIST = RespStatus(-602, 'channel not exist')


ret_code = {}
for k, v in vars(Resp).iteritems():
	if k.startswith('__'):
		continue
	try:
		ret_code[v.code] = v
	except Exception:
		continue
