from .Models import *
import numpy as np
import pandas as pd
import AI.DataProcesser as DataProcessor

class Course:
    def __init__(self):
        self.id = ""
        self.user_id = ""
        self.name = ""
        self.year = 0
        self.semester = ""
        self.grade = 0
        self.subject = ""


class Transcript:
    def __init__(self):
        self.courses = {}

    def add_course(self, course):
        self.courses[course.id] = course

    def remove_course(self, id):
        self.courses.pop(id)


def generate_improvement_list(student_profile, desired_grade):
    dataset = DataProcessor.get_dataset()
    relevant_features = determine_attribute_weights(dataset, absolute=False)
    print(relevant_features)
    collapsed_student_profile = collapse_attributes(student_profile.copy())

    for i in range(len(collapsed_student_profile)):
        if relevant_features[i] <= 0:
            collapsed_student_profile[i] *= relevant_features[i]
        elif relevant_features[i] > 0:
            collapsed_student_profile[i] = (1 - collapsed_student_profile[i]) * relevant_features[i]

    improvement_list = []
    for i in range(len(collapsed_student_profile)):
        if collapsed_student_profile[i] != 0:
            improvement_list.append([convert_index_to_attribute_name(i), collapsed_student_profile[i], relevant_features[i]])

    return sorted(improvement_list, key=lambda element: abs(element[1]), reverse=True)


def collapse_attributes(student_profile):
    student_profile[1] = (student_profile[1] - 15) / 7
    student_profile[3] = (student_profile[3] - 1) / 3
    student_profile[4] = (student_profile[4] - 1) / 3
    student_profile[5] = student_profile[5] / 4
    student_profile[10] = (student_profile[10] - 1) / 4
    student_profile[11] = (student_profile[11] - 1) / 4
    student_profile[12] = (student_profile[12] - 1) / 4
    student_profile[13] = (student_profile[13] - 1) / 4
    student_profile[14] = (student_profile[14] - 1) / 4

    return student_profile

def convert_index_to_attribute_name(index):
    if index == 0:
        return "sex"
    if index == 1:
        return "age"
    if index == 2:
        return "address"
    if index == 3:
        return "traveltime"
    if index == 4:
        return "studytime"
    if index == 5:
        return "failures"
    if index == 6:
        return "schoolsup"
    if index == 7:
        return "activities"
    if index == 8:
        return "internet"
    if index == 9:
        return "romantic"
    if index == 10:
        return "freetime"
    if index == 11:
        return "goout"
    if index == 12:
        return "Dalc"
    if index == 13:
        return "Walc"
    if index == 14:
        return "health"
    if index == 15:
        return "G3"
    
def advice_string(attribute_name):
    if attribute_name == "address":
        return "Consider living in a rural environment."
    if attribute_name == "traveltime":
        return "Consider living closer to your campus or applying for on campus housing."
    if attribute_name == "studytime":
        return "You should spend some more time studying."
    if attribute_name == "activities":
        return "Take a look at some extra-curricular activities your school offers."
    if attribute_name == "internet":
        return "Ask your regional internet service provider about a plan."
    if attribute_name == "goout":
        return "Spend less time going out with friends. Try picking up a book or studying for your classes."
    if attribute_name == "Dalc":
        return "Drink less alcohol during the week. Alcohol can make it difficult to study and stay focused on school work."
    if attribute_name == "Walc":
        return "Drink less alcohol on the weekend. Alcohol can make it difficult to study and stay focused on school work."

    return "Error"


def determine_attribute_weights(dataset, absolute=True):
    # calculate which attributes most affect final grade
    df = pd.DataFrame(dataset, columns=["sex", "age", "address", "traveltime", "studytime", "failures", "schoolsup", "activities", "internet", "romantic", "freetime", "goout", "Dalc", "Walc", "health", "G3"])
    cor = df.corr()
    if absolute is True:
        cor_target = abs(cor["G3"])
    else:
        cor_target = cor["G3"]

    return cor_target
