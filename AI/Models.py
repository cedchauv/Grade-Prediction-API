class StudentProfile:
    def __init__(self):
        self.sex = ""
        self.age = 0
        self.address_type = ""
        self.travel_time = 0
        self.study_time = 0
        self.failures = 0
        self.educational_support = False
        self.activities = False
        self.internet = False
        self.romance = False
        self.go_out = 0
        self.weekday_alcohol_consumption = 0
        self.weekend_alcohol_consumption = 0
        self.health = 0

    def to_numeric(self, collapse=False):
        return [
            1 if self.sex == 'M' else 0, self.age if not collapse else (self.age - 15) / 7,
            1 if self.address_type == 'R' else 0, self.travel_time if not collapse else (self.travel_time - 1) / 4,
            self.study_time if not collapse else (self.study_time - 1) / 4,
            self.failures if not collapse else self.failures / 4, 1 if self.educational_support else 0,
            1 if self.activities else 0, 1 if self.internet else 0, 1 if self.romance else 0,
            self.go_out if not collapse else (self.go_out - 1) / 4,
            self.weekday_alcohol_consumption if not collapse else (self.weekday_alcohol_consumption - 1) / 4,
            self.weekend_alcohol_consumption if not collapse else (self.weekend_alcohol_consumption - 1) / 4,
            self.health if not collapse else (self.health - 1) / 4
        ]