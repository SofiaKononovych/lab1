import random

all_faculties = []


# Student class
class Student:
    def __init__(self, name, year_of_studying, group, cathedra):
        self.name = name
        self.year_of_studying = year_of_studying
        self.group = group
        self.cathedra = cathedra


# Teacher class
class Teacher:
    def __init__(self, name, cathedra, group):
        self.name = name
        self.cathedra = cathedra
        self.group = group


# Faculty class
class Faculty:
    def __init__(self, name):
        self.name = name
        self.cathedras = []

# task 2
    def add_cathedra(self, cathedra):
        self.cathedras.append(cathedra)

    def remove_cathedra(self, cathedra):
        self.cathedras.remove(cathedra)

    def edit_cathedra(self, cathedra):
        new_name_set = input('Enter new name of this cathedra:')
        cathedra.name = new_name_set

# task 5
    def sort_student_by_year(self):
        all_student_listbox = []
        # sort = sorted(self.students, key=lambda x: x.year_of_studying)
        for cath in self.cathedras:
            for stud in cath.students:
                all_student_listbox.append(stud)
        if len(all_student_listbox) == 0:
            print("No students on this faculty found")
            return
        for year in range(6):
            print(f"** Year {year+1} students: **")
            for stud in all_student_listbox:
                if stud.year_of_studying - 1 == year:
                    print(stud.name)


# task 6
    def get_students_sorted(self):
        all_students_box = []
        for cathedra in self.cathedras:
            for stud in cathedra.students:
                all_students_box.append(stud.name)
        sort = sorted(all_students_box)
        leng_of_list = len(sort)
        if leng_of_list == 0:
            print("No students available yet.")
            return
        print(f"** All students of {self.name} faculty sorted by alphabet: **")
        for name in range(leng_of_list):
            print(sort[name])

    def get_teachers_sorted(self):
        all_teachers_box = []
        for cathedra in self.cathedras:
            for teach in cathedra.teachers:
                all_teachers_box.append(teach.name)
        sort = sorted(all_teachers_box)
        leng_of_list = len(sort)
        if leng_of_list == 0:
            print("No teachers available yet.")
            return
        print(f"** All teachers of {self.name} faculty sorted by alphabet: **")
        for name in range(leng_of_list):
            print(sort[name])


# Cathedra class
class Cathedra:
    def __init__(self, name):
        self.name = name

        self.teachers = []
        self.students = []

# task 3
    def add_student(self, student):
        self.students.append(student)
        print(f"We added {student.name} to Faculty.")
        return

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"We added {teacher.name} to Faculty.")
        return

    def remove_student(self, student):
        for stud in self.students:
            if stud.name == student:
                print(f"{stud.name} was deleted from faculty.")
                self.students.remove(stud)
                return
        print("No students with this name found.")
        return

    def remove_teacher(self, teacher):
        for teach in self.teachers:
            if teach.name == teacher:
                print(f"{teach.name} was deleted from faculty.")
                self.teachers.remove(teach)
                return
        print("No teachers with this name found.")
        return

    def edit_student(self, name):
        for stud in self.students:
            if stud.name == name:
                print(f"Info about student {stud.name}: year of studying - {stud.year_of_studying}, group - {stud.group}, cathedra - {stud.cathedra}")
                edited_stud = student_pref(self.name)
                self.students.remove(stud)
                self.students.append(edited_stud)
                print("Changes saved.")
                return
        print("No info about a student with this name found.")


    def edit_teacher(self, name):
        for teach in self.teachers:
            if teach.name == name:
                print(f"Info about teacher {teach.name} cathedra - {teach.cathedra}, group {teach.group}")
                edited_teach = teacher_pref(self.name)
                self.teachers.remove(teach)
                self.teachers.append(edited_teach)
                print("Changes saved.")
                return
        print("No info about teacher with this name found.")


# task 4
    def get_student_by_surname(self, surname):
        for stud in self.students:
            if stud.name == surname:
                print(
                    f"Info about student {stud.name}: year of studying - {stud.year_of_studying}, group - {stud.group}, cathedra - {stud.cathedra}")
                return
        print("No students with this name found.")

    def get_teacher_by_surname(self, surname):
        for teach in self.teachers:
            if teach.name == surname:
                print(
                    f"Info about student {teach.name}:  group - {teach.group}, cathedra - {teach.cathedra}")
                return
        print("No teachers with this name found.")



# task 9
    def get_student_by_year(self, year):
        result = []
        print(f"** Students of {year} year: ** ")
        for stud in self.students:
            if stud.year_of_studying == year:
                result.append(stud.name)
        print(*result, sep="\n")
        if len(result) == 0:
            print("No students of this year found.")


    def get_student_by_group(self, group):
        result = []
        print(f"** Students of {group} group: ** ")
        for stud in self.students:
            if stud.group == group:
                result.append(stud.name)
        print(*result, sep="\n")
        if len(result) == 0:
            print("No students of this group found.")


    def get_teacher_by_group(self, group):
        result = []
        print(f"** Teachers of {group} group: ** ")
        for teach in self.teachers:
            if teach.group == group:
                result.append(teach.name)
        print(*result, sep="\n")
        if len(result) == 0:
            print("No teacher teaching in this group found.")

# output all cathedra
    def get_teacher(self, cathedra):
        values = self.teachers.values()
        keys = self.teachers.keys()
        for k in keys:
            for v in values:
                if v == cathedra:
                    print(f"{k} is a member of {v} cathedra.")
                    return
        print("No teachers with on this cathedra found.")

# task 7
    def sort_cath_student_by_year(self):
        for year in range(6):
            print(f"** Year {year + 1} students: **")
            for stud in self.students:
                if stud.year_of_studying - 1 == year:
                    print(stud.name)


# task 8
    def sort_student_by_name(self):
        names = []
        for stud in self.students:
            names.append(stud.name)
        names_sorted = sorted(names)
        if len(names) == 0:
            print("No students available yet.")
            return
        print("LIST OF STUDENTS SORTED BY ALPHABET")
        for nam in names_sorted:
            print(nam)
        return names

    def sort_teacher_by_name(self):
        names = []
        for teach in self.teachers:
            names.append(teach.name)
        names_sorted = sorted(names)
        if len(names) == 0:
            print("No teachers available yet.")
            return
        print("LIST OF TEACHERS SORTED BY ALPHABET")
        for nam in names_sorted:
            print(nam)
        return names

# task 10

    def sort_student_of_course_by_alph(self, course):
        student_box = []
        for stud in self.students:
            if stud.year_of_studying == course:
                student_box.append(stud.name)
        sorted_list = sorted(student_box)
        print(f"Students of {course} course:")
        for name in sorted_list:
            print(name)
        if len(student_box) == 0:
            print(f"No students of year {course} on the cathedra yet.")


# task 1
def faculty_create():
    name = input("    Enter the name of faculty you want to create:")
    if name == '':
        print('The name can not be none')
        return
    faculty = Faculty(name)
    for fac in all_faculties:
        if fac.name == faculty.name:
            print("This faculty was already added.")
            return
    all_faculties.append(faculty)
    print(f"    Faculty {faculty.name} successfully created")


def faculty_delete(faculty):
    all_faculties.remove(faculty)


def faculty_edit(name):
    new_name = input("   Enter the name of faculty you want to replace the original name with:")
    for faculty in all_faculties:
        if faculty.name == name:
            faculty.name = new_name
            return
    print("No faculty with this name found.")


# function which uses add_cathedra method
def cathedra_create(fac):
    name = input("Enter the name of cathedra:")
    if name == '':
        print('The name can not be none')
        return
    cathedra = Cathedra(name)
    for cath in fac.cathedras:
        if cath.name == cathedra.name:
            print("This cathedra was already added.")
            return
    fac.add_cathedra(cathedra)
    print(f"    {cathedra.name} successfully created")

# function for creating instances of students
def student_pref(cathedra):
    while True:
        name = input("Enter name:")
        year = int(input("Enter year of studying (1-6):"))
        if year > 6:
            continue
        group = int(input("Enter group (1-10):"))
        if group > 10:
            continue
        student = Student(name, year, group, cathedra)
        return student


# function for creating instances of teachers
def teacher_pref(cathedra):
    while True:
        name = input("Enter name:")
        group = int(input("Enter group(1-10):"))
        if group > 10:
            continue
        teacher = Teacher(name, cathedra, group)
        return teacher




