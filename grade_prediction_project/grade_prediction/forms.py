from django.contrib.auth.models import User
from django import forms
from .choices import *
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date',)


class StudentDataForm(forms.Form):
    sex = forms.ChoiceField(choices=GENDER, label="Sex")
    age = forms.IntegerField(label="Age")
    addressType = forms.ChoiceField(choices=ADDRESS_TYPE, label="Address Type")
    travelTime = forms.ChoiceField(choices=TRAVEL_TIME, label ="Travel Time to School")
    studyTime = forms.ChoiceField(choices=STUDY_TIME, label="Study Time per Week")
    failures = forms.ChoiceField(choices=FAILURES, label="Past Failed Courses")
    activities = forms.BooleanField(required=False, label="Extra-Curricular Activities")
    internet = forms.BooleanField(required=False, label="Internet Access at Home")
    romance = forms.BooleanField(required=False, label="In a Relationship")
    freeTime = forms.ChoiceField(choices=FREE_TIME, label="Free Time per Week")
    goOut = forms.ChoiceField(choices=GO_OUT, label="Time Going Out per Week")
    educationalSupport = forms.BooleanField(required=False, label="Extra Educational Support")
    weekdayAlcoholConsumption = forms.ChoiceField(choices=WEEKDAY_ALCOHOL, label="Weekday Alcohol Consumption")
    weekendAlcoholConsumption = forms.ChoiceField(choices=WEEKEND_ALCOHOL, label="Weekend Alcohol Consumption")
    health = forms.ChoiceField(choices=HEALTH, label="Health")



