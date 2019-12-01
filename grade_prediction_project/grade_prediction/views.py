import json

import requests
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import StudentDataForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        student_data_form = StudentDataForm(request.POST)
        if student_data_form.is_valid():
            if update_student(request.user.username, student_data_form.cleaned_data) != 200:
                add_student(request.user.username, json.dumps(student_data_form.cleaned_data))
            return HttpResponseRedirect('/')
    else:
        try:
            student_data_form = StudentDataForm(initial=get_student(request.user.username)['studentProfile'])
        except:
            print("no profile data")
            student_data_form = StudentDataForm()

    return render(request, 'profile.html', {'student_data_form': student_data_form, })


def get_student(username):
    return requests.get('http://localhost:8080/users/' + username).json()


def add_student(username, student_data_json):
    profile = '{"userName": "' + username + '", "userType": "STUDENT", "studentProfile": ' + student_data_json + ',"courses": []}'
    requests.post('http://localhost:8080/users/student/', json=profile)


def update_student(username, student_data_json):
    r = requests.patch('http://localhost:8080/users/student/' + username + "/", json=student_data_json)
    print(r.status_code)
    return r.status_code


def logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required()
def class_search(request):
    return render(request, 'grade_prediction/search.html')


@login_required()
def advisor(request):
    return render(request, 'grade_prediction/advisor.html')


@login_required()
def predict(request):
    if request.method == 'POST':
        print('predict stuff here')
    return render(request, 'grade_prediction/predict.html')