import json
import os

import requests
from django.template import Context, Template
from django.template.response import TemplateResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import numpy as np
from .forms import StudentDataForm
from keras.models import load_model
import AI.GradeAI as GradeAI
import AI.Advisor as Advisor


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
    requests.post('http://localhost:8080/users/student/', json=json.loads(profile))


def update_student(username, student_data_json):
    print(username, student_data_json)
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
    c = {}
    if request.method == 'POST':
        data = list(get_student(request.user.username)["studentProfile"].values())
        for i in range(len(data)):
            if data[i] == 'M' or data[i] == 'R' or data[i] == True:
                data[i] = 1
            elif data[i] == 'F' or data[i] == 'U' or data[i] == False:
                data[i] = 0

        numpy = np.fromiter(data, dtype=float)
        numpy = np.asmatrix(numpy)

        model = GradeAI.get_model()

        prediction = GradeAI.predict_np(model, numpy)
        improvements = Advisor.generate_improvement_list(data, 13 if prediction*5 < 65 else 17)
        filtered_improvements = []
        for improvement in improvements:
            if improvement[1] != 0 and improvement[0] != "freetime" and improvement[0] != "sex" and improvement[0] != "age" and improvement[0] != "failures" and improvement[0] != "schoolsup" and improvement[0] != "romantic" and improvement[0] != "health":
                filtered_improvements.append(improvement)

        print(filtered_improvements)

        c['prediction'] = int(round(prediction[0][0] * 5))
        c['improve_1'] = Advisor.advice_string(filtered_improvements[0][0]) + " There is a " + ("%.2f" % (abs(filtered_improvements[0][2]) * 100)) + "% correlation with " + ("failure." if filtered_improvements[0][2] < 0 else "success.")
        c['improve_2'] = Advisor.advice_string(filtered_improvements[1][0]) + " There is a " + ("%.2f" % abs((filtered_improvements[1][2]) * 100)) + "% correlation with " + ("failure." if filtered_improvements[1][2] < 0 else "success.")
        c['improve_3'] = Advisor.advice_string(filtered_improvements[2][0]) + " There is a " + ("%.2f" % abs((filtered_improvements[2][2]) * 100)) + "% correlation with " + ("failure." if filtered_improvements[2][2] < 0 else "success.")

    return render(request, 'grade_prediction/predict.html', c)
