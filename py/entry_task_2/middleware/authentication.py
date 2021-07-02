#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse

from constant.ret_codes import Resp
from lib import defs
from manager import token_manager

NOT_CHECK_DIR = [
	'/entry_task/api/user/login',
	'/entry_task/api_admin/operator/login',
	'/admin',
	'/static',
]

ADMIN_DIR = '/entry_task/api_admin/'


class Authentication(object):

	@staticmethod
	def not_need_login(request):
		if request.method == 'GET':
			return True

		for start_with in NOT_CHECK_DIR:
			if request.path.startswith(start_with):
				return True
		return False

	def process_request(self, request):
		if request.method == 'OPTIONS':
			return HttpResponse()

		if Authentication.not_need_login(request):
			return None

		is_admin = request.path.startswith(ADMIN_DIR)

		validate_token, validate_message = token_manager.validate_token(request, is_admin)
		if validate_token:
			return None

		if validate_message is not None:
			return defs.response_data(Resp.RESP_NOT_LOGGED_IN, msg=validate_message)
		else:
			return HttpResponse(status=401)
