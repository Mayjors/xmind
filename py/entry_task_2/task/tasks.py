#!/usr/bin/env python
# -*- coding: utf-8 -*-

from celery import shared_task

from lib.logger import log
from manager import activity_manager, user_manager


@shared_task(bind=True)
def send_email_to_user(self, *args, **kwargs):
	activity_id = kwargs.get('activity_id')
	activity = activity_manager.get_activity(activity_id)
	if activity is None:
		log.error('不存在id为{}的活动'.format(activity_id))
		return

	start_id = 0
	while start_id >= 0:
		start_id = _handler(start_id, activity_id)


def _handler(start_id, activity_id):
	entry_list = activity_manager.list_enter_with_offset(activity_id=activity_id, limit=100, id_offset=start_id)
	if not entry_list:
		return -1

	user_id_array = [a['user_id'] for a in entry_list]
	user_list = user_manager.get_user_by_ids(user_id_array)
	for user in user_list:
		_do_send(user)

	return entry_list.pop().get('id')


def _do_send(user):
	# TODO send email
	log.info('{}发送成功'.format(user.get('email')))
