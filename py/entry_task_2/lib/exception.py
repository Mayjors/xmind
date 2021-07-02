#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.defs import RespStatus


class BusinessExceptionError(Exception):

	def __init__(self, code_or_status, msg=None, data={}):
		self.msg = ''
		if isinstance(code_or_status, RespStatus):
			self.code = code_or_status.code
			self.msg = code_or_status.msg
		else:
			self.code = code_or_status
		if msg:
			self.msg = msg
		self.data = data

	def __repr__(self):
		return "{code:%d msg:\"%s\"}" % (self.code, self.msg)

	def __str__(self):
		return self.__repr__()
