from mod_student import *
from mod_teacher import *


def modify_user_data():
    usr = input('Student(S) or Teacher(T): ').upper()
    if usr == 'S':
        modify_student()
    elif usr == 'T':
        modify_teacher()
    else:
        print("Invalid input")
        modify_user_data()
    print('Data successfully updated!')
    print(' ')
