import json
from pprint import pprint
from .models import Student
from . import db
from .routes import year


def openData():
    print("hello")
    with open('fakeStudentsForEva.txt') as f:
        student_list = json.load(f)
        year_list6 = []
        year_list7 = []
        year_list8 = []
        male_list = []
        female_list = []
        pprint(student_list)
        #loop
        print("hi")
        for student_data in student_list:
            student = Student(id=student_data.id, name=student_data.name, gender=student_data.gender, sport=student_data.sport, year=student_data.year)
            if Student[year]=="6":
                year_list6.append(student)
                print("yes")
            elif (Student[year] == "7"):
                year_list7.append(Student)
            else:
                year_list8.append(Student)
            if Student[gender] == 'F':
                female_list.append(Student)
            else:
                male_list.append(Student)
            pprint(year_list6)
            db.add(student)
            print(student)
        db.commit()
        return year_list6
        return year_list7
        return year_list8









