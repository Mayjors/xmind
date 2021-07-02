#!/usr/bin/env python
# -*- coding:utf-8 -*-


def int_schema(min_val, max_val, message=None):
	return {
		"type": "integer",
		"minimum": min_val,
		"maximum": max_val,
		"message": message
	}


def str_schema(min_len=None, max_len=None, pattern=None, message=None):
	d = {
		'type': 'string',
		'message': message
	}
	if min_len is not None:
		d['minLength'] = min_len
	if max_len is not None:
		d['maxLength'] = max_len
	if pattern is not None:
		d['pattern'] = pattern
	return d


UINT1_SCHEMA = int_schema(0, 1)
UINT7_SCHEMA = int_schema(0, 127)
UINT8_SCHEMA = int_schema(0, 255)
UINT16_SCHEMA = int_schema(0, 65535)
UINT31_SCHEMA = int_schema(0, 2147483647)
UINT32_SCHEMA = int_schema(0, 4294967295)
UINT64_SCHEMA = int_schema(0, 18446744073709551615)

INT8_SCHEMA = int_schema(-128, 127)
INT16_SCHEMA = int_schema(-32768, 32767)
INT32_SCHEMA = int_schema(-2147483648, 2147483647)
INT64_SCHEMA = int_schema(-9223372036854775808, 9223372036854775807)

STR8 = str_schema(0, 8)
STR8_NON_EMPTY = str_schema(1, 8)
STR16 = str_schema(0, 16)
STR16_NON_EMPTY = str_schema(1, 16)
STR32 = str_schema(0, 32)
STR32_NON_EMPTY = str_schema(1, 32)
STR64 = str_schema(0, 64)
STR64_NON_EMPTY = str_schema(1, 64)
STR128 = str_schema(0, 128)
STR128_NON_EMPTY = str_schema(1, 128)
STR256 = str_schema(0, 256)
STR256_NON_EMPTY = str_schema(1, 256)
STR512 = str_schema(0, 512)
STR512_NON_EMPTY = str_schema(1, 512)
STR1024 = str_schema(0, 1024)
STR1024_NON_EMPTY = str_schema(1, 1024)
STR2048 = str_schema(0, 2048)
STR2048_NON_EMPTY = str_schema(1, 2048)
