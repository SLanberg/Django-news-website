from django import forms
from .models import Commentary




class CommentaryForm(forms.ModelForm):
	""" Class form Commentary"""
	class Meta:
		model 	= Commentary
		fields 	= ("text", )