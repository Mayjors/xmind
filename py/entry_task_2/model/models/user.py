#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.db import models


class UserTab(models.Model):
	id = models.AutoField(primary_key=True)
	email = models.CharField(max_length=64)
	name = models.CharField(max_length=32)
	photo_url = models.CharField(max_length=1024)
	created_time = models.IntegerField()
	delete_time = models.IntegerField(default=0)

	class Meta:
		db_table = 'user_tab'
		app_label = 'model'


class UserSecurityTab(models.Model):
	id = models.AutoField(primary_key=True)
	user_name = models.CharField(max_length=64)
	password = models.CharField(max_length=128)
	created_time = models.IntegerField()
	delete_time = models.IntegerField(default=0)

	class Meta:
		db_table = 'user_security_tab'
		app_label = 'model'
