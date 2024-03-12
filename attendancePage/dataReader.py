import json
# json library
from .models import Student
from . import db


def openData():
    print("hello")
    with open('fakeStudentsForEva.txt') as f:
        student_list = json.load(f)
        year_list6 = []
        year_list7 = []
        year_list8 = []
        male_list = []
        female_list = []
        print(student_list)

        for student_data in student_list:
            #Accessing attributes in a JSON object using keys
            student = Student(id=student_data['id'], name=student_data['name'], gender=student_data['gender'],
                              sport=student_data['sport'], year=student_data['year'])

            # Fixed condition checks and appending to lists
            if student.year == "6":
                year_list6.append(student)
            elif student.year == "7":
                year_list7.append(student)
            else:  # Assuming all other students are in year 8
                year_list8.append(student)

            if student.gender == 'F':
                female_list.append(student)
            else:
                male_list.append(student)

            db.add(student)
            print(student)

        db.commit()

        # Return lists in a tuple or a dictionary
        return {'year_list6': year_list6, 'year_list7': year_list7, 'year_list8': year_list8, 'male_list': male_list,
                'female_list': female_list}

def
