import random

all_faculties = []

#Student class
class Student:
    def __init__(self, name, year_of_studying, group, cathedra):
        self.name = name
        self.year_year_of_studying = year_of_studying
        self.group = group
        self.cathedra = cathedra


#Teacher class
class Teacher:
    def __init__(self, name, cathedra, group):
        self.name = name
        self.cathedra = cathedra
        self.group = group


class Faculty:
    def __init__(self, name):
        self.name = name
        self.cathedras = []

    def add_cathedra(self, cathedra):
        self.cathedras.append(cathedra)

    def remove_cathedra(self, cathedra):
        self.cathedras.remove(cathedra)

    def edit_cathedra(self):
        print("List of available cathedras:")
        if len(self.cathedras) == 0:
            print("No cathedras created yet. Try to add one to edit it first.")
            return
        for cath in self.cathedras:
            name = self.cathedras[cath].name
            print(name)
        new_name_set = input('Enter new name of this cathedra:')
        if cathedra in self.cathedras:
            cathedra.name == new_name_set
            return
        print('This cathedra is not in this Faculty')




    # output all students

    # output all teachers

    #item 6

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
        print(f"All students of {self.name} faculty sorted by alphabet:")
        for name in range(leng_of_list):
            print(sort[name])

    #5
    def sort_student_by_year(self):
        sorted = sorted(self.students, key=lambda x: x.year_of_studying)
        for year in range(6):
            print(f"** Year {year} students list: **")
            for stud in sorted:
                if stud.year_of_studying == year:
                    print("Year: {stud.year_of_studying} . Name: {stud.name}")



class Cathedra:
    def __init__(self, name):
        self.name = name

        self.teachers = []
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            print(f"We added {student.name} to Faculty.")
            return

    def add_teacher(self, teacher):
        if isinstance(teacher, Teacher):
            self.students.append(teacher)
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
        print("No students with this name found.")
        return

    def edit_student(self, student):
        for stud in self.students:
            if stud.name == student:
                print(f"Info about student {stud.name}: year of studying - 1, group - {stud.group}, cathedra - {stud.cathedra}")
                stud = student_pref(self.name)
                print("Chages saved.")
            else:
                print("No info about a teacher with this name found.")
                return



    def edit_teacher(self, teacher):
        for teach in self.teachers:
            try:
                if teach.name == teacher:
                    print(f"Now you are able to edit {teach.name} . Additional info: group {teach.group}, cathedra: {teach.cathedra}.")
            except:
                print("No info about a teacher with this name found.")
                break
            while True:
                ask = input("What do you want to edit? (Name - N, Group - G, End - E) ").lower
                if ask.startswith("n"):
                    name_set = input("Enter new name and surname:")
                    teach.name = name_set
                elif ask.startswith("g"):
                    group_set = input("Enter new group:")
                    teach.group = group_set
                elif ask.startswith("e"):
                    break
                else:
                    continue
        print("All changes saved.")
        return

    #4
    def get_student_by_surname(self, surname):
        for stud in self.students:
            if stud.name == surname:
                print(f"Info about student {stud.name}: year of studying - {stud.year_of_studying}, group - {stud.group}, cathedra - {stud.cathedra}")
                return
        print("No students with this name found.")

    def get_teacher_by_surname(self, surname):
        for teach in self.teachers:
            if teach.name == surname:
                print(f"Info about student {teach.name}: year of studying - {teach.year_of_studying}, group - {teach.group}, cathedra - {teach.cathedra}")
                return
        print("No teachers with this name found.")

    def get_student_by_year(self, year):
        result = []
        for stud in self.students:
            if stud.year_of_studying == year:
                result.append(stud)
                print(f"Students of {stud.year_of_studying} course: {[stud.name for _ in result]}")
                return
        print("No students on this year of studying found.")

    def get_student_by_group(self, group):
        result = []
        for stud in self.students:
            if stud.group == group:
                result.append(stud)
                print(f"Students of {stud.group} group: {[stud.group for _ in result]}")
                return
        print("No students of this group of studying found.")

    def get_teacher_by_group(self, group):
        result = []
        for teach in self.teachers:
            if teach.group == group:
                result.append(teach)
                print(f"Students of {teach.group} group: {[teach.group for _ in result]}")
                return
        print("No students of this group of studying found.")


    #9
    def get_stud_of_cath_by_year(self, cathedra, year):
        result = []
        for stud in self.students:
            if  stud.year == year and stud.cathedra == cathedra:
                result.append(stud)
                print(f"Students of {stud.cathedra} and {stud.year} course: {[stud for _ in result]}")
                return
        print('No students on cathedra of this year found')


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
        sorted = sorted(self.students, key=lambda x: x.year_of_studying)
        for year in range(6):
            print(f"** Year {year} students list: **")
            for stud in sorted:
                if stud.year_of_studying == year:
                    print("Year: {stud.year_of_studying} . Name: {stud.name}")


            #[{'name1', 1}, {'name2, 1'}, {'name3', 2}, {'name2', 3}]


    ### item 8
    def sort_student_by_name(self):
        names = []
        for stud in self.students:
            names.append(stud.name)
        names_sorted = sorted(names)
        if len(names) == 0:
            print("No students available yet.")
            return
        print("LIST OF STUDENTS SORTED BY ALPHABET")
        for nam in names:
            print(nam)
        return names

    def sort_teacher_by_name(self):
        names = []
        for teach in self.teachers:
            names.append(teach.name)
        names_sorted = sorted(names)
        if len(names) == 0:
            print("No students available yet.")
            return
        print("LIST OF TEACHERS SORTED BY ALPHABET")
        for nam in names:
            print(nam)
        return names

    # item 10

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


def faculty_create():
    name = input("Enter the name of faculty you want to create:")
    faculty = Faculty(name)
    all_faculties.append(faculty)
    print(f"Faculty {faculty.name} successfully created")


def faculty_delete(faculty):
    def faculty_delete(faculty):
        all_faculties.remove(faculty)


def faculty_edit():
    origin_name = input("Enter the name of faculty you want to edit:")
    new_name = input("Enter the name of faculty you want to replace the original name with:")
    for faculty in all_faculties:
        if faculty.name == origin_name:
            faculty.name == new_name
            return
    print("No faculty with this name found.")


def cathedra_create(fac):
    name = input("Enter the name of cathedra:")
    cathedra = Cathedra(name)
    fac.add_cathedra(cathedra)
    # all = []
    # for i in range(len(all_faculties)):
    #     element = all_faculties[i]
    #     typed = element.name
    #     all.append(typed)
    # ask = input(f"Locate your cathedra to one of the faculties: {all}(enter the full name)")
    # for i in range(len(all)):
    #     if ask == all[i]:
    #         all_faculties[i].add_cathedra(cathedra)
    return


faculty_create()
print(all_faculties)

# name generator
def name_faker():
    name = fake.first_name()
    return name


#surname generator
def surname_faker():
    surname = " "+fake.last_name()
    return surname


def student_pref(cathedra):
    name = input("Enter name:")
    year = int(input("Enter course:"))
    group = int(input("Enter group:"))
    student = Student(name, year, group, cathedra)
    return student

def teacher_pref(cathedra):
    name = input("Enter name:")
    group = int(input("Enter group:"))
    teacher = Teacher(name, group, cathedra)
    return teacher




