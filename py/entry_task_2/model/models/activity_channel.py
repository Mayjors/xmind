#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.db import models


class ActivityChannelTab(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=60)
	created_time = models.IntegerField()
	creator = models.CharField(max_length=60)
	modified_time = models.IntegerField()
	modifier = models.CharField(max_length=60)
	delete_time = models.IntegerField(default=0)

	class Meta:
		db_table = 'activity_channel_tab'
		app_label = 'model'
