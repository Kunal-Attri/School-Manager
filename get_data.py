

def convert(a):
    name = ""
    b = []
    for i in range(len(a)):
        if a[i] != "[" and a[i] != '"' and a[i] != "" and a[i] != "]" and a[i] != "'":
            if a[i] != ",":
                if a[i] == " " and a[i + 1] == '"':
                    pass
                elif a[i] == " " and a[i + 1] == "'":
                    pass
                else:
                    name += a[i]
            else:
                b.append(name)
                name = ""
    b.append(name)
    return b


def update_data():
    file = open("data/students.txt", "r")
    students = file.read()
    file.close()
    file = open("data/students_age.txt", "a+")
    if file.read() == "":
        sage = dict(file.read())
    else:
        sage = eval(file.read())
    file.close()
    file = open("data/students_class.txt", "a+")
    if file.read() == "":
        standard = dict(file.read())
    else:
        standard = eval(file.read())
    file.close()
    file = open("data/teachers.txt", "r")
    teachers = file.read()
    file.close()
    file = open("data/teachers_age.txt", "a+")
    if file.read() == "":
        tage = dict(file.read())
    else:
        tage = eval(file.read())
    file.close()
    file = open("data/teachers_subjects.txt", "a+")
    if file.read() == "":
        subject = dict(file.read())
    else:
        subject = eval(file.read())
    file.close()
    return convert(students), sage, standard, convert(teachers), tage, subject


def upload_data(students, sage, standard, teachers, tage, subject):
    file = open("data/students.txt", "w")
    file.write(str(students))
    file.close()
    file = open("data/students_age.txt", "w")
    file.write(str(sage))
    file.close()
    file = open("data/students_class.txt", "w")
    file.write(str(standard))
    file.close()
    file = open("data/teachers.txt", "w")
    file.write(str(teachers))
    file.close()
    file = open("data/teachers_age.txt", "w")
    file.write(str(tage))
    file.close()
    file = open("data/teachers_subjects.txt", "w")
    file.write(str(subject))
    file.close()


def change_password():
    prev_pw = input("Please enter your previous database password: ")
    file = open("data/password.txt", "w+")
    if prev_pw == file.read():
        file.close()
        file = open("data/password.txt", "w+")
        new_pw = input("Enter new database password: ")
        file.write(new_pw)
        file.close()
    else:
        file.close()
        print("Entered password didn't worked")
