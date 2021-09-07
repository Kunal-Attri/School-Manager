from add_new_user import *
from get_user_data import *
from modify import *
from summarise import *

file = open("data/password.txt", "r")
jnew_pw = False
if file.read() == "":
    pw = input('Provide a password for your database: ')
    file.close()
    file = open("data/password.txt", "w")
    file.write(pw)
    file.close()
    jnew_pw = True
else:
    file.close()

pass_entered = False
tries = 0

file = open("data/password.txt", "r")
real_pw = file.read()
file.close()

while tries < 3 and not jnew_pw:
    pw = input('Enter your database password: ')
    if pw == real_pw:
        pass_entered = True
        break
    tries += 1

while pass_entered:
    purpose = input('''What would you like to do? 
A - add new student
B - add new teacher
C - get user data
D - modify data
E - summarise all data
Z - exit program
> ''').upper()
    if purpose == 'A':
        add_student()
    elif purpose == 'B':
        add_teacher()
    elif purpose == 'C':
        get_user_data()
    elif purpose == 'D':
        modify_user_data()
    elif purpose == 'E':
        summary()
    elif purpose == "F":
        change_password()
    elif purpose == 'Z':
        upload_data(students, sage, standard, teachers, tage, subject)
        break
    else:
        print('Invalid input')
        print(' ')
