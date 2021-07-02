#!/usr/bin/env python
# -*- coding: utf-8 -*-


class RespStatus(object):
	def __init__(self, code, msg):
		self.code = code
		self.msg = msg

	def __repr__(self):
		return "{code:%d msg:\"%s\"}" % (self.code, self.msg)

	def __str__(self):
		return self.__repr__()

	def __eq__(self, other):
		if not isinstance(other, RespStatus):
			return False
		return self.code == other.code

	def __ne__(self, other):
		if not isinstance(other, RespStatus):
			return True
		return self.code != other.code
