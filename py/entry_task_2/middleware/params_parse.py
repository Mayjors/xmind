#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common import jsonutils

from lib import defs

NOT_CHECK_DIR = [
	'/admin',
	'/static',
]

class ParamsParse(object):
	@staticmethod
	def pop_empty_data_key(form_data):
		data = {}
		for field, value in form_data.items():
			if value == u'':
				continue
			data[field] = value
		return data

	@staticmethod
	def format_json_data(json_data):
		for field, value in json_data.items():
			try:
				if isinstance(value, list):
					json_data[field] = [item.strip() for item in value]
				else:
					json_data[field] = value.strip()
			except Exception as ex:
				pass

	def process_request(self, request):
		for start_with in NOT_CHECK_DIR:
			if request.path.startswith(start_with):
				return None

		method = request.method
		if method == 'GET':
			try:
				form_data = request.GET
				form_data = ParamsParse.pop_empty_data_key(form_data)
			except Exception as ex:
				return defs.response_parms_error(request, ex.message)
		else:
			try:
				form_data = jsonutils.from_json(request.body)
				form_data = ParamsParse.pop_empty_data_key(form_data)
			except Exception as ex:
				return defs.response_parms_error(request, 'request body is not json : ' + ex.message)

		ParamsParse.format_json_data(form_data)
		request.json = form_data
		return None
