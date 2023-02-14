from django import forms
from django.db import models

class Categorychoices(models.TextChoices):
    job = "job", "仕事"
    hobby = "hobby", "趣味"
    university = "university", "大学"

class EventForm(forms.Form):

    start_date = forms.IntegerField(required=True)
    end_date = forms.IntegerField(required=True)
    event_name = forms.CharField(required=True, max_length=32)
    category = forms.fields.ChoiceField(choices=Categorychoices, required=False)

class CalendarForm(forms.Form):

    start_date = forms.IntegerField(required=True)
    end_date = forms.IntegerField(required=True)   
