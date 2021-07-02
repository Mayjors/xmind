#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib


def safe_convert_to_string(source):
	if isinstance(source, str) or isinstance(source, unicode):
		return source
	else:
		try:
			return u'%s' % source
		except:
			return None


def generate_sha1(source):
	m = hashlib.sha1()
	m.update(source.encode('utf-8'))
	return m.hexdigest().lower()
