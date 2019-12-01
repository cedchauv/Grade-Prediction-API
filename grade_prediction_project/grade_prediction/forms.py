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
    sex = forms.ChoiceField(choices=GENDER)
    age = forms.IntegerField()
    addressType = forms.CharField()
    travelTime = forms.IntegerField()
    studyTime = forms.IntegerField()
    failures = forms.IntegerField()
    activities = forms.BooleanField(required=False)
    internet = forms.BooleanField(required=False)
    romance = forms.BooleanField(required=False)
    goOut = forms.IntegerField()
    educationalSupport = forms.BooleanField(required=False)
    weekdayAlcoholConsumption = forms.IntegerField()
    weekendAlcoholConsumption = forms.IntegerField()
    health = forms.IntegerField()



