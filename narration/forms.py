#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:23:00 2018

@author: satyam
"""
from django import forms
from .models import Content
class ContentForm(forms.ModelForm):

    class Meta:
    	model = Content
    	fields = ('title', 'text',)


#class ContentForm(forms.Form):
#	title = forms.CharField(max_length = 200)
#	text = forms.CharField(max_length = 2000, widget = forms.Textarea())

	
#	def clean(self):
#		cleaned_data = super(ContentForm , self).clean()
#		text = cleaned_data.get('input_text')
#		if not text:
#			raise forms.ValidationError("Write Something Please!")
