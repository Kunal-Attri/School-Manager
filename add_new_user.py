from data import *


def add_student():
    stu_name = input('Name of the student: ').upper()
    try:
        stu_age = int(input('Age of the student: '))
    except ValueError:
        print('Invalid Age Input')
        print(' ')
        add_student()
    else:
        if stu_age < 5:
            print('Age of a student cannot be less than 5 years old.')
            print(' ')
            add_student()
        elif stu_age > 19:
            print('Age of a student cannot be more than 19 years')
            print(' ')
            add_student()
        else:
            try:
                stu_class = int(input('Class of the student: '))
            except ValueError:
                print('Invalid Class Input')
                print(' ')
                add_student()
            else:
                if stu_class < 1 or stu_class > 12:
                    print('A school student cannot be in a class other than from class 1st to 12th')
                    print(' ')
                    add_student()
                else:
                    students.append(stu_name)
                    print(stu_name, stu_age, stu_class)
                    sage[stu_name] = stu_age
                    standard[stu_name] = stu_class
                    print(f'''
Student successfully added!
Student ID is {students.index(stu_name) + 1000}
''')


def add_teacher():
    teacher_name = input('Name of the teacher: ').upper()
    try:
        teacher_age = int(input('Age of the teacher: '))
    except ValueError:
        print('Invalid age input')
        print(' ')
        add_teacher()
    else:
        if teacher_age < 25:
            print('A person less than 25 years old cannot be a teacher.')
            print(' ')
            add_teacher()
        elif teacher_age > 75:
            print('A person more than 75 years old does not have any more capability to teach. Please retry.')
            print(' ')
            add_teacher()
        else:
            teacher_subject = input('Subject of the teacher: ').upper()
            teachers.append(teacher_name)
            tage[teacher_name] = teacher_age
            subject[teacher_name] = teacher_subject
            print(f'''
Teacher successfully added!
Teacher ID is {teachers.index(teacher_name) + 1000}
''')
