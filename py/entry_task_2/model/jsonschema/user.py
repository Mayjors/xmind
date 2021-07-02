#!/usr/bin/env python
# -*- coding:utf-8 -*-


import model.jsonschema.schema_defs as sd

USER_LOGIN = {
	'type': 'object',
	'properties': {
		'name': sd.STR64,
		'password': sd.STR128
	},
	'required': ['name', 'password']
}

USER_ACTIVITY_LIST = {
	'type': 'object',
	'properties': {
		'pageno': sd.UINT16_SCHEMA,
		'count': sd.UINT32_SCHEMA
	}
}

SEND_EMAIL = {
	'type': 'object',
	'properties': {
		'activity_id': sd.UINT64_SCHEMA
	}
}
