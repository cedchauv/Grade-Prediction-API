from .Models import *

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


def generate_improvement_list(student_profile, model_weights):
    return 0
