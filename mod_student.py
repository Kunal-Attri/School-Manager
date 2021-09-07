from data import *


def modify_student():
    data = input('''What would you like to modify?
N - name of student
A - age of student
C - class of student
> ''').upper()
    if data == 'N':
        mod_stu_name()
    elif data == 'A':
        mod_stu_age()
    elif data == 'C':
        mod_stu_class()


def mod_stu_name():
    global prev_name
    try:
        usid = int(input('ID: '))
    except ValueError:
        print("Invalid ID")
        print(" ")
        mod_stu_name()
    else:
        try:
            prev_name = students[usid - 1000]
        except IndexError:
            print(f'Wrong ID({usid}) provided')
            print(" ")
            mod_stu_name()
        else:
            print(f'Kindly confirm that the student name is {prev_name}')
            prev_age = sage[prev_name]
            prev_class = standard[prev_name]
            students.pop(usid - 1000)
            sage.pop(prev_name)
            standard.pop(prev_name)
            new_name = input('New name: ').upper()
            students.insert(usid - 1000, new_name)
            sage[new_name] = prev_age
            standard[new_name] = prev_class


def mod_stu_age():
    try:
        usid = int(input('ID: '))
    except ValueError:
        print("Invalid ID")
        print(" ")
        mod_stu_age()
    else:
        try:
            stu_name = students[usid - 1000]
        except IndexError:
            print(f'Wrong ID({usid}) provided')
            mod_stu_age()
        else:
            print(f'Kindly confirm that the student name is {stu_name}')
            try:
                new_age = int(input('New age: '))
            except ValueError:
                print('Invalid Age Input')
                mod_stu_age()
            else:
                if new_age < 5:
                    print('Age of a student cannot be less than 5 years old.')
                    mod_stu_age()
                elif new_age > 19:
                    print('Age of a student cannot be more than 19 years')
                    mod_stu_age()
                else:
                    sage[stu_name] = new_age


def mod_stu_class():
    try:
        usid = int(input('ID: '))
    except ValueError:
        print("Invalid ID")
        print(" ")
        mod_stu_class()
    else:
        try:
            stu_name = students[usid - 1000]
        except IndexError:
            print(f'Invalid ID({usid}) provided')
            mod_stu_class()
        else:
            print(f'Kindly confirm that the student name is {stu_name}')
            try:
                new_class = int(input('New Class: '))
            except ValueError:
                print('Invalid Class Input')
                mod_stu_class()
            else:
                if new_class < 1 or new_class > 12:
                    print('A school student cannot be in a class other than from class 1st to 12th')
                    mod_stu_class()
                else:
                    standard[stu_name] = new_class
