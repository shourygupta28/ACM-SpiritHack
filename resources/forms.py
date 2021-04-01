from django import forms
from .models import *

class ResourceForm(forms.ModelForm):
	
	class Meta(forms.ModelForm):
		model 		= Resource
		fields 		= ['Subject', 'title','description','file']

class ReminderForm(forms.ModelForm):

	due_at = forms.DateTimeField(    widget=forms.TextInput(     
									attrs={'type': 'date'} 
								))

	class Meta(forms.ModelForm):
		model 		= Reminder
		fields 		= ['Subject', 'title','description','due_at']
