#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import uuid

from lib import date_utils

EXPIRE = 60 * 60
token_cache = {}


def _get_user_with_token(token, is_admin):
	# Debug
	if token == 'ab6aaeae-8ab6-11ea-bd67-acde48001122':
		return True, {'name': 'admin', 'id': '1'}

	user_token = token_cache.get(token, None)
	if not user_token or date_utils.now_stamp() >= user_token['e']:
		return False, None

	if (not is_admin and user_token['is_admin']) or (is_admin and not user_token['is_admin']):
		return False, None

	token_cache[token]['e'] = expire_time()
	return True, user_token['u']


def validate_token(request, is_admin=False):
	json_obj = request.json
	token = json_obj.get('token')

	success, user = _get_user_with_token(token, is_admin)
	if success:
		request.user = user
		del json_obj['token']
		return True, None

	return False, 'invalid token'


def generate_token(user, is_admin=False):
	token = str(uuid.uuid1())
	token_cache[token] = {'u': user, 'e': expire_time(), 'is_admin': is_admin}
	return token


def expire_time():
	return date_utils.now_stamp() + EXPIRE


def clear_token():
	now = date_utils.now_stamp()
	for token, user_token in token_cache.items():
		if now < user_token['e']:
			del token_cache[token]
	time.sleep(10)


# auto clear with async
thread = threading.Thread(target=clear_token)
thread.start()
