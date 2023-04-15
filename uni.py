import random

# from faker import Faker
# fake = Faker()

all_faculties = []


#Student class
class Student:
    def __init__(self, name, surname, year_of_studying, group, cathedra):
        self.name = name
        self.surname = surname
        self.year_year_of_studying = year_of_studying
        self.group = group
        self.cathedra = cathedra


#Teacher class
class Teacher:
    def __init__(self, name, surname, cathedra):
        self.name = name
        self.surname = surname
        self.cathedra = cathedra


class Faculty:
    def __init__(self, name):
        self.name = name
        self.cathedras = []

    def add_cathedra(self, cathedra):
        self.cathedras.append(cathedra)

    def remove_cathedra(self, cathedra):
        self.cathedras.remove(cathedra)

    def edit_cathedra(self, cathedra, new_name):
        self.cathedras.remove(cathedra.name)
        self.cathedras.append(new_name)

    # output all students

    # output all teachers

    #item 6
    # def get_students_sorted(self):
    #     all_students_box = []
    #     all_cathedras = len(self.cathedras)
    #     for i in range(all_cathedras):
    #         cathedra = self.cathedras[i]
    #         names = cathedra.sort_student_by_name()
    #         all_students_box.append(names)
    #     names_sorted = sorted(all_students_box)
    #     leng_of_list = len(names_sorted)
    #     for i in range(leng_of_list):
    #         print(names[i])
    #     if leng_of_list == 0:
    #         print("No students available yet.")
    #     return

    def get_students_sorted(self):
        all_students_box = []
        all_cathedras = len(self.cathedras)
        for i in range(all_cathedras):
            cathedra = self.cathedras[i].students
            keys = cathedra.keys()
            for k in keys:
                all_students_box.append(k)
        sort = sorted(all_students_box)
        leng_of_list = len(sort)
        for i in range(leng_of_list):
            print(sort[i])
        if leng_of_list == 0:
            print("No students available yet.")
        return


class Cathedra:

    def __init__(self, name):
        self.name = name

        self.teachers = {}
        self.students = {}

    def add_student(self, student):

        if isinstance(student, Student):
            student_name = student.name+student.surname
            add_stud = {student_name:(student.group, student.year_year_of_studying, student.cathedra)}
            self.students.update(add_stud)
            print(f"We added {student_name} to Faculty.")
            return

    def add_teacher(self, teacher):

        if isinstance(teacher, Teacher):
            teacher_name = teacher.name+teacher.surname
            add_stud = {teacher_name:teacher.cathedra}
            self.teachers.update(add_stud)
            print(f"We added {teacher_name} to Faculty.")
            return

    def remove_student(self, student):

        if isinstance(student, Student):
            students = self.students.keys()
            search = student.name + student.surname
            for stud in students:
                if stud == search:
                    print(f"{stud} was deleted from faculty.")
                    self.students.pop(stud)
                    return
        print("No students with this name found.")
        return

    def remove_teacher(self, teacher):

        if isinstance(teacher, Teacher):
            teachers = self.teachers.keys()
            search = teacher.name + teacher.surname
            for teach in teachers:
                if teach == search:
                    print(f"{teach} was deleted from faculty.")
                    self.teachers.pop(teach)
                    return
        print("No students with this name found.")
        return

    #
    # def sort_by_year(self, year):
    #
    #     values = self.students.values()
    #     keys = self.students.keys()
    #     for k in keys:
    #         for v in values:
    #             if v[0] == year:
    #                 print(f"{k} is on {v[0]} course.")
    #                 return
    #     print("No students with this name found.")

    #output all cathedra
    def get_teacher(self, cathedra):
        values = self.teachers.values()
        keys = self.teachers.keys()
        for k in keys:
            for v in values:
                if v == cathedra:
                    print(f"{k} is a member of {v} cathedra.")
                    return
        print("No teachers with on this cathedra found.")

    ## item 7

    def sort_student_by_year(self):
        for k, v in sorted(students.items(), key=lambda p: p[1]):
            print(k, v[1])


    ### item 8
    def sort_student_by_name(self):
        names = []
        keys = self.students.keys()
        for k in keys:
            names.append(k)
        names_sorted = sorted(names)
        leng_of_list = len(names_sorted)
        for i in range(leng_of_list):
            print(names_sorted[i])
        if leng_of_list == 0:
            print("No students available yet.")
        return names

    def sort_teacher_by_name(self):
        names = []
        keys = self.teachers.keys()
        for k in keys:
            names.append(k)
        names_sorted = sorted(names)
        leng_of_list = len(names_sorted)
        for i in range(leng_of_list):
            print(names_sorted[i])
        if leng_of_list == 0:
            print("No teachers available yet.")

    # item 10

    def sort_student_of_course_by_alph(self, course):
        student_box = []
        keys = self.students.keys()
        for k in keys:
            v = self.students.get(k)
            if v[1] == course:
                student_box.append(k)
        sorted_list = sorted(student_box)
        print(sorted_list)
        if len(student_box) == 0:
            print(f"No students of year {course} on the cathedra yet.")





# sort by name/sur here:

# sort by course here:

#sort by group here:


def available_faculties():
    for i in range(len(all_faculties)):
        print(i)
    return

# name generator
def name_faker():
    name = fake.first_name()
    return name

#surname generator
def surname_faker():
    surname = " "+fake.last_name()
    return surname

def student_pref():
    if len(all_faculties) == 0:
        print("You have to add at least one faculty firstly.")
        return
    student = Student(name_faker(), surname_faker(), 1, 1)
    faculty = input(f"Enter the faculty you want to enroll your student in: {all_faculties}:").lower()
    if faculty.startswith('fi'):
        faculty.add_student(student)
    return

def teacher_pref():
    if len(all_faculties) == 0 :
        print("You have to add at least one faculty firstly.")
        return
    faculty = input(f"Add this teacher to one of the faculties: {all_faculties}")
    cathedra = input("Add this teacher to cathedra(Mathematics/):").lower()
    teacher = faculty.get_teacher("Mathematics")
    if cathedra.startswith('fi'):
        faculty.add_teacher(teacher)
    return

#student = Student(name_faker(), surname_faker(), 1, 1)
#teacher = Teacher(name_faker(), surname_faker(), "Mathematics")


def faculty_create():
    name = input("Enter the name of faculty:")
    faculty = Faculty(name)
    all_faculties.append(faculty)

#not finished yet:
def cathedra_create():
    name = input("Enter the name of cathedra:")
    cathedra = Cathedra(name)
    all = []
    if len(all_faculties) == 0:
        print("No faculties added yet.")
        return
    for i in range(len(all_faculties)):
        element = all_faculties[i]
        typed = element.name
        all.append(typed)
    ask = input(f"Locate your cathedra to one of the faculties: {all}(enter the full name)")
    for i in range(len(all)):
        if ask == all[i]:
            all_faculties[i].add_cathedra(cathedra)
    return

faculty_create()
print(all_faculties)
cathedra_create()
def main():
    while True:
        ask = input(''' *** MENU ***

Quit
>>
''').lower()
        if ask.startswith("q"):
            break
        # elif ask.startswith("a"):
        #     what = input("Choose the option to add(Student/Teacher/Faculty/Cathedra):").lower()
        #     if what.startswith("s"):
        #         student_pref()
        #     elif what.startswith("t"):
        #         teacher_pref()
        #         return
        #     elif what.startswith("f"):
        #         faculty.to_the_all_faculties()
        #     elif what.startswith("c"):
        #         return

