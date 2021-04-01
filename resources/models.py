from django.db import models
from user.models import *
from home.models import *

# Create your models here.

class Resource(models.Model):
	resource_by			= models.ForeignKey(User, limit_choices_to={'is_student': True}, on_delete=models.CASCADE, null=True)
	Subject 			= models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
	title				= models.CharField(max_length=50)
	description			= models.CharField(max_length=500)
	file				= models.FileField(default='', upload_to='file/', blank=True, null=True)

class Reminder(models.Model):
	reminder_by 		= models.ForeignKey(User, limit_choices_to={'is_student':True}, on_delete=models.CASCADE, null=True)
	Subject 			= models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
	title				= models.CharField(max_length=50)
	description			= models.CharField(max_length=500)
	due_at 				= models.DateTimeField(null=False, blank=False)
