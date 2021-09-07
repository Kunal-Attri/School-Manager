import random

from data import *


def summary():
    trials = 3
    while trials > 0:
        record = input("Kindly enter your database password: ")
        print(' ')
        file = open("data/password.txt", "r")
        if record == file.read():
            file.close()
            print_data()
            break
        else:
            trials -= 1
            print("You have a entered a wrong password")
            if trials > 0:
                print('Please try again')
                print(f'No. of chances left = {trials}')
            print(' ')

    else:
        print('You have run out of all your trials left for unlocking database with password')
        continue_wrong_password()


def continue_wrong_password():
    continue_ = input("""
Now you have to provide other information to unlock database.
Would you like to continue? (Y/N) """).upper()
    cont(continue_)


def cont(continue_):
    if continue_ == "Y":
        try:
            tot_stu = int(input("Total no. of students registered in the database? "))
            tot_tea = int(input("Total no. of teachers registered in the database? "))
        except ValueError:
            print("Invalid Input")
            cont(continue_)
        else:
            check_robot = str(random.randint(0, 100))
            typed = input(f"Kindly type 'A1B2C3_{check_robot}': ")
            if typed != f"A1B2C3_{check_robot}":
                print("You seem to be a robot")
            else:
                total_database_stu = len(students)
                total_database_tea = len(teachers)
                if tot_stu == total_database_stu and tot_tea == total_database_tea:
                    print("Provided information is correct")
                    print_data()
                else:
                    print("Provided data is wrong.")
                    print("")
    elif continue_ == "N":
        print(" ")
    else:
        print("Invalid input!")
        continue_wrong_password()


def print_data():
    print(f"""
Students' names:- {students}

Students' age:- {sage}

Students' classes:- {standard}

Teachers' names:- {teachers}

Teachers' age:- {tage}

Teachers' subjects:- {subject}
""")
