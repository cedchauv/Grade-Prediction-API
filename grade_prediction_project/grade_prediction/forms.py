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
    addressType = forms.ChoiceField(choices=ADDRESS_TYPE)
    travelTime = forms.ChoiceField(choices=TRAVEL_TIME)
    studyTime = forms.ChoiceField(choices=STUDY_TIME)
    failures = forms.ChoiceField(choices=FAILURES)
    activities = forms.BooleanField(required=False)
    internet = forms.BooleanField(required=False)
    romance = forms.BooleanField(required=False)
    goOut = forms.ChoiceField(choices=GO_OUT)
    educationalSupport = forms.BooleanField(required=False)
    weekdayAlcoholConsumption = forms.ChoiceField(choices=WEEKDAY_ALCOHOL)
    weekendAlcoholConsumption = forms.ChoiceField(choices=WEEKEND_ALCOHOL)
    health = forms.ChoiceField(choices=HEALTH)



