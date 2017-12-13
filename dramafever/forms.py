from django import forms
from django.db import models

class TopicsForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='description', max_length=1000)

class CommentsForm(forms.Form):
    comment = forms.CharField(label='comment',max_length=500)