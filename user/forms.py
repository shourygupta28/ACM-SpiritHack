from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from django.db import transaction
from .models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class StudentRegistrationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model 		= User
		fields 		= ['name','email','contact_no', 'yr_branch', 'password1','password2']


class TeacherRegistrationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model 		= User
		fields 		= ['name','email','contact_no', 'password1','password2']