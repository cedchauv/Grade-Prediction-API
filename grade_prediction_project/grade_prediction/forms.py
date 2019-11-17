from django.contrib.auth.models import User
from grade_prediction.models import Profile
from django import forms
from grade_prediction.choices import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date',)


class StudentDataForm(forms.Form):
    gender = forms.ChoiceField(choices=GENDER)
    age = forms.IntegerField();
    address = forms.CharField();
    travel_time = forms.TimeField();
    weekly_study_time = forms.TimeField();
    failures = forms.IntegerField();
    extra_curricular_activities = forms.BooleanField();
    internet_acces_at_home = forms.BooleanField();
    romantic_relationship = forms.BooleanField();
    going_out_with_friends_time = forms.TimeField();
    extra_educational_support = forms.BooleanField();
    weekday_alcohol_consumption = forms.IntegerField();
    weekend_day_alcohol_consumption = forms.IntegerField();
    health = forms.IntegerField();


