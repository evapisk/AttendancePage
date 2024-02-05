# import json
# from pprint import pprint
# from models import Student
# from __init__ import db
#
# with open('fakeStudentsForEva.txt') as f:
#     student_list = json.load(f)
#     pprint(student_list)
#     #loop
#     for student_data in student_list:
#         student = Student(id=student_data.id, name=student_data.name, gender=student_data.gender, sport=student_data.sport, year=student_data.year)
#
#         db.add(student)
#     db.commit()
#
#
