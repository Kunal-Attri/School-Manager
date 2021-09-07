from data import *


def modify_teacher():
    data = input('''What would you like to modify?
N - name of teacher
A - age of teacher
S - subject of teacher
> ''').upper()
    if data == 'N':
        mod_tea_name()
    elif data == 'A':
        mod_tea_age()
    elif data == 'S':
        mod_tea_sub()
    else:
        print("Invalid input")
        modify_teacher()


def mod_tea_name():
    try:
        usid = int(input('ID: '))
    except ValueError:
        print("Invalid ID")
        print(" ")
        mod_tea_name()
    else:
        try:
            prev_name = teachers[usid - 1000]
        except IndexError:
            print(f'Wrong ID({usid}) provided')
            mod_tea_name()
        else:
            print(f'Kindly confirm that the teacher name is {prev_name}')
            prev_age = tage[prev_name]
            prev_sub = subject[prev_name]
            teachers.pop(usid - 1000)
            tage.pop(prev_name)
            subject.pop(prev_name)
            new_name = input('New name: ').upper()
            teachers.insert(usid - 1000, new_name)
            tage[new_name] = prev_age
            subject[new_name] = prev_sub


def mod_tea_age():
    try:
        usid = int(input('ID: '))
    except ValueError:
        print('Ínvalid ID')
        print(" ")
        mod_tea_age()
    else:
        try:
            tea_name = teachers[usid - 1000]
        except IndexError:
            print(f'Wrong ID({usid}) provided')
            mod_tea_age()
        else:
            print(f'Kindly confirm that the teacher name is {tea_name}')
            try:
                new_age = int(input('New age: '))
            except ValueError:
                print('Invalid age input')
                mod_tea_age()
            else:
                if new_age < 25:
                    print('A person less than 25 years old cannot a teacher.')
                    mod_tea_age()
                elif new_age > 75:
                    print('A person more than 75 years old does not have any more capability to teach')
                    mod_tea_age()
                else:
                    tage[tea_name] = new_age


def mod_tea_sub():
    try:
        usid = int(input('ID: '))
    except ValueError:
        print("Invalid input")
        print(" ")
        mod_tea_sub()
    else:
        try:
            tea_name = teachers[usid - 1000]
        except IndexError:
            print(f'Wrong ID({usid}) provided')
            mod_tea_sub()
        else:
            print(f'Kindly confirm that the teacher name is {tea_name}')
            new_sub = input('New subject: ').upper()
            subject[tea_name] = new_sub
