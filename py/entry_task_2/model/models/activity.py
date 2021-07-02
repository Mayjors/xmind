#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.db import models


class ActivityTab(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64)
	channel = models.CharField(max_length=32)
	icon_url = models.CharField(max_length=128)
	detail = models.CharField(max_length=1000)
	begin_time = models.IntegerField()
	end_time = models.IntegerField()
	place = models.CharField(max_length=200)
	status = models.IntegerField()
	created_time = models.IntegerField()
	creator = models.CharField(max_length=60)
	modified_time = models.IntegerField()
	modifier = models.CharField(max_length=60)
	delete_time = models.IntegerField(default=0)

	class Meta:
		db_table = 'activity_tab'
		app_label = 'model'


class ActivityUserRelationTab(models.Model):
	id = models.AutoField(primary_key=True)
	activity_id = models.IntegerField()
	user_id = models.IntegerField()
	created_time = models.IntegerField()
	creator = models.CharField(max_length=60)
	delete_time = models.IntegerField(default=0)

	class Meta:
		db_table = 'activity_user_relation_tab'
		app_label = 'model'
		ordering = ['-created_time']


class ActivityCommentTab(models.Model):
	id = models.AutoField(primary_key=True)
	activity_id = models.IntegerField()
	user_id = models.IntegerField()
	content = models.CharField(max_length=1024)
	created_time = models.IntegerField()
	creator = models.CharField(max_length=64)
	delete_time = models.IntegerField(default=0)

	class Meta:
		db_table = 'activity_comment_tab'
		app_label = 'model'
		ordering = ['-created_time']
