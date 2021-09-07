from data import *


def get_user_data():
    type_of_user = user_type()
    if type_of_user == 'S':
        get_student_data()
    elif type_of_user == 'T':
        get_teacher_data()
    else:
        print('Invalid input')
        print(' ')


def user_type():
    type_of_user = input('Student(S) or Teacher(T): ').upper()
    return type_of_user


def get_student_data():
    try:
        stu_id = int(input('ID of the student: '))
    except ValueError:
        print('Invalid ID')
        print(' ')
        get_student_data()
    else:
        try:
            name_of_the_student = students[stu_id - 1000]
        except IndexError:
            print(f'Invalid ID({stu_id}) provided')
            print(' ')
            get_student_data()
        else:
            print(f'''
Name: {name_of_the_student}
Age: {sage[name_of_the_student]} years
Class: {standard[name_of_the_student]}
''')


def get_teacher_data():
    try:
        tea_id = int(input('ID of the teacher: '))
    except ValueError:
        print('Invalid ID')
        print(' ')
        get_teacher_data()
    else:
        try:
            name_of_the_teacher = teachers[tea_id - 1000]
        except IndexError:
            print(f'Wrong ID({tea_id}) provided')
            print(' ')
            get_teacher_data()
        else:
            print(f'''
Name: {name_of_the_teacher}
Age: {tage[name_of_the_teacher]} years
Subject: {subject[name_of_the_teacher]}
''')
