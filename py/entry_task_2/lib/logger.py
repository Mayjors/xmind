#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os

from common.logger import log
from common.loggingmp import MPTimedRotatingFileHandler
from django.conf import settings
from log_request_id.filters import RequestIDFilter

log_dir = settings.LOGGER_CONFIG['log_dir']

extra_logger_config = {
	'access': {
		'handler': {
			'filename': os.path.join(log_dir, 'access.log').replace('\\', '/'),
			'when': 'MIDNIGHT',
			'backupCount': 30,
		},
		'formatter': {
			'fmt': '%(asctime)s.%(msecs)03d|%(levelname)s|%(process)d:%(thread)d|%(filename)s:%(lineno)d|%(module)s.%(funcName)s|%(message)s',
			'datefmt': '%Y-%m-%d %H:%M:%S',
		},
		'level': logging.INFO,
	},
}


class RegionFomatter(logging.Formatter):

	def __init__(self, fmt=None, datefmt=None, region=None):
		self.region = region
		super(RegionFomatter, self).__init__(fmt, datefmt)

	def formatTime(self, record, datefmt=None):
		if self.region is None:
			return super(RegionFomatter, self).formatTime(record, datefmt)
		else:
			from common import convert
			if datefmt:
				s = convert.timestamp_to_datetime(record.created, self.region).strftime(datefmt)
			else:
				t = convert.timestamp_to_datetime(record.created, self.region).strftime('%Y-%m-%d %H:%M:%S')
				s = '%s.%03d' % (t, record.msecs)
			return s


def add_extra_logger(extra_logger, logger_config):
	handler = MPTimedRotatingFileHandler(**logger_config['handler'])
	handler.setFormatter(logging.Formatter(**logger_config['formatter']))
	setattr(log, extra_logger, logging.getLogger(extra_logger))
	getattr(log, extra_logger).setLevel(logger_config['level'])
	getattr(log, extra_logger).addHandler(handler)


for extra_logger, logger_config in extra_logger_config.items():
	add_extra_logger(extra_logger, logger_config)

# add request_id into access.log / data.log
if getattr(settings, 'LOG_REQUEST_ID', False):
	for logger_name in ['main', 'data', 'access']:
		logger = logging.getLogger(logger_name)
		for hand in logger.handlers:
			hand.addFilter(RequestIDFilter())
			pattern = hand.formatter._fmt
			if pattern.find('%(filename)s') < 0:
				pattern = pattern.replace('%(message)s', '%(filename)s:%(lineno)d|%(module)s.%(funcName)s|%(message)s')

			fmt = logging.Formatter(
				fmt=pattern.replace('%(message)s', '%(request_id)s|%(message)s'),
				datefmt='%Y-%m-%d %H:%M:%S'
			)
			hand.setFormatter(fmt)

# Workaround to make log always use UTC+8 timezone, which consistent with mall.
if getattr(settings, 'LOG_REGION', None) is not None:
	from logging import Logger

	for logger_name in Logger.manager.loggerDict.keys():
		logger = logging.getLogger(logger_name)
		for hand in logger.handlers:
			old_formatter = hand.formatter
			if old_formatter is not None:
				formatter = RegionFomatter(
					old_formatter._fmt,
					old_formatter.datefmt,
					settings.LOG_REGION)
				hand.setFormatter(formatter)
