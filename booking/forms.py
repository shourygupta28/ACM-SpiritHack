from django import forms
from .models import *


class SlotForm(forms.ModelForm):
	date = forms.DateTimeField(    widget=forms.TextInput(     
									attrs={'type': 'date'} 
								))
	time = forms.ModelMultipleChoiceField(	        queryset=Time.objects.all(),
							        widget=forms.CheckboxSelectMultiple
						)
	class Meta(forms.ModelForm):
		model 		= Slot
		fields 		= ['date', 'time']


class bookedForm(forms.ModelForm):

	class Meta(forms.ModelForm):
		model 		= booked
		fields 		= []