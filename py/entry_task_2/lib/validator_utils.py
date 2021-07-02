#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from functools import wraps

from common.form_validator import FormValidator
from jsonschema.validators import Draft4Validator

from defs import response_parms_error, response_data, ExceptionResp
from lib.logger import log


def check_json_schema_v2(schema, data, validator=None):
	if not validator:
		validator = Draft4Validator(schema)
	return sorted(validator.iter_errors(data), key=lambda e: e.path)


def json_schema_errors_to_str(errors):
	error_dict = {'/'.join(['%s' % err_path for err_path in error.path]): error.message for error in errors}
	return json.dumps(error_dict)


def check_params(schema, method='POST'):
	def _parse_params(func):
		@wraps(func)
		def _func(request, *args, **kwargs):
			if request.method != method:
				log.error(
					'view_method_error|url=%s,method=%s',
					request.get_full_path().encode('utf-8'),
					request.method)
				return response_parms_error(request, 'request method is not %s' % method)

			from common.form_validator import FormValidateError
			if method == 'GET':
				try:
					form = FormValidator(schema)
					form_data = request.json
					form_data = form.normalize(form_data)
				except FormValidateError as form_error:
					return form_validate_error_message(request, schema, form_error)
				except Exception as ex:
					return response_parms_error(request, ex.message)
			else:
				form_data = request.json
			check_result = check_json_schema_v2(schema, form_data)
			if check_result:
				return json_schema_error_message(request, schema, check_result)
			try:
				return func(request, form_data, *args, **kwargs)
			except ExceptionResp as ex:
				return response_data(ex.resp)

		return _func

	return _parse_params


def json_schema_error_message(request, schema, errers):
	if not errers or not schema:
		return response_parms_error(request, json_schema_errors_to_str(errers))
	try:
		error = errers[0]
		field = error.path[0]
		user_msg = _find_jsonschema_field(schema, field)
		if user_msg:
			return response_parms_error(request, user_msg)
	except Exception as e:
		pass

	return response_parms_error(request, json_schema_errors_to_str(errers))


def _find_jsonschema_field(schema, field):
	if not schema:
		return None
	properties = schema.get('properties', None)
	if not properties:
		return None

	field = properties.get(field, None)
	if not field:
		return None
	return field.get('message', None)


def _get_error_field_conf(err_type):
	err_type_conf = {
		'minlength': {
			'err_type': 'Item error',
			'field_index': 1,
			'field_value': 2,
		},
		'maxlength': {
			'err_type': 'Item error',
			'field_index': 1,
			'field_value': 2,
		},
		'pattern': {
			'err_type': 'format error',
			'field_index': -2,
			'field_value': -1,
		},
		'convert': {
			'err_type': 'type error',
			'field_index': -2,
			'field_value': -1,
		},
		'maximum': {
			'error_type': 'Integer value exceeds upper limit',
			'field_index': -2,
			'field_value': -1,
		}
	}

	for _key, conf in err_type_conf.iteritems():
		try:
			sz = len(_key)
			err_type = err_type.encode("utf-8").lower().strip()
			if _key == err_type[0: sz]:
				return conf
		except Exception as e:
			pass
	return None


def form_validate_error_message(request, schema, fve):
	msg = fve.message
	array = msg.split(',')
	if len(array) < 1:
		return response_parms_error(request, msg)

	err_type = array[0].lower()
	conf = _get_error_field_conf(err_type)
	if not conf:
		return response_parms_error(request, msg)

	field_index = conf.get('field_index', None)
	if field_index is None:
		return response_parms_error(request, msg)
	field = array[field_index]
	user_msg = _find_jsonschema_field(schema, field)
	if not user_msg:
		return response_parms_error(request, msg)
	return response_parms_error(request, user_msg)
