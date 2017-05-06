# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Hospital(models.Model):
	HospitalId = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=250)
	UserName = models.CharField(max_length=250)
	Password = models.CharField(max_length=250)
	Contact = models.IntegerField(null=True)
	Specialization = models.CharField(max_length=250, null=True)
	Address = models.TextField(null=True)
	Distance = models.IntegerField(null=True)

	# Return the object type of the data
	def __str__(self):
		return str(self.HospitalId)

class Patient(models.Model):
	UID = models.BigIntegerField(max_length=12, unique=True)
	Name = models.CharField(max_length=250)
	Age = models.IntegerField(null=True)
	AgeGroup = models.CharField(max_length=20,null=True,blank=True)
	Gender = models.CharField(max_length=250, null=True)
	HospitalId = models.TextField(null=True,blank=True)
	UserName = models.CharField(max_length=250, unique=True)
	Password = models.CharField(max_length=250)

	def __str__(self):
		return str(self.UID)
