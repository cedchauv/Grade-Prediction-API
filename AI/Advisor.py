from .Models import *
import numpy as np
import pandas as pd

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
    dataset = np.loadtxt('Dataset\\processed-tdata2.csv', delimiter=',',skiprows=1)
    relevant_features = determine_attribute_weights(dataset)
    print(relevant_features)
    collapsed_student_profile = collapse_attributes(student_profile.copy())
    top_students = []

    # compile list of students at or above desired grade threshold
    for row in dataset:
        if row[-1] >= desired_grade:
            top_students.append(list(row[:-1]))

    # determine student from list of top students that most closely matches the users profile
    least_difference_score = -1
    for student in top_students:
        difference = 0
        collapsed_student = collapse_attributes(student.copy())
        for i in range(len(collapsed_student)):
            attribute_weight = relevant_features[convert_index_to_attribute_name(i)]
            difference += abs(collapsed_student_profile[i] - collapsed_student[i]) * attribute_weight
        if difference < least_difference_score or least_difference_score == -1:
            least_difference_score = difference
            closest_match = student

    # create list of attributes to improve prioritized by attributes that differ the most
    improvements = {}
    collapsed_match = collapse_attributes(closest_match.copy())
    for i in range(len(collapsed_student_profile)):
        attribute_weight = relevant_features[convert_index_to_attribute_name(i)]
        difference = abs(collapsed_student_profile[i] - collapsed_match[i]) * attribute_weight
        if difference not in improvements:
            improvements[difference] = [i]
        else:
            improvements[difference].append(i)

    improvement_list = []
    for improvement in sorted(improvements):
        for attribute in improvements[improvement]:
            improvement_list.append([convert_index_to_attribute_name(attribute), improvement])

    return sorted(improvement_list, key=lambda element: element[1], reverse=True)


def collapse_attributes(student_profile):
    student_profile[1] = (student_profile[1] - 15) / 7
    student_profile[3] = (student_profile[3] - 1) / 4
    student_profile[4] = (student_profile[4] - 1) / 4
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


def determine_attribute_weights(dataset):
    # calculate which attributes most affect final grade
    df = pd.DataFrame(dataset, columns=["sex", "age", "address", "traveltime", "studytime", "failures", "schoolsup", "activities", "internet", "romantic", "freetime", "goout", "Dalc", "Walc", "health", "G3"])
    cor = df.corr()
    cor_target = abs(cor["G3"])

    return cor_target[cor_target>=0.0]