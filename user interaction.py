from uni import *


def main():
    while True:
        ask = input(''' MENU
    Add Faculty
    View Faculties
    Quit
    >>>
    ''').lower()
        if ask.startswith("q"):
            break
        elif ask.startswith('a'):
            faculty_create()
        elif ask.startswith("v"):
            faculty_interaction()
        else:
            continue


def faculty_interaction():
    while True:
        print("Here is the list of all faculties.")
        for i in range(len(all_faculties)):
            for fac in all_faculties:
                print(f"{i + 1}.{fac.name}")
        print("Here is a list of actions you can do:")
        print("1. View info of faculty (enter the number of faculty)")
        print("2. Add faculty")
        print("3. Delete faculty")
        print("4. Go back")
        ask = int(input('>>>'))
        if ask == 1:
            num_fac = int(input('Enter the number of faculty \n>>>'))
            # for i in range(len(all_faculties)):
            #     for fac in all_faculties:
            #         if fac == num_fac:
            fac = all_faculties[num_fac - 1]
            print(f"You chose {fac.name}! ")
            cathedra_interaction(fac)
        elif ask == 2:
            faculty_create()
        elif ask == 3:
            choose = int(input("Enter the number of faculty you want to delete."))
            if choose <= len(all_faculties):
                faculty = all_faculties[choose - 1]
                faculty_delete(faculty)
                return
            print("No faculty with this number")
        elif ask == 4:
            break
        else:
            continue


def cathedra_interaction(fac):
    while True:
        print(f"Here is all cathedras on this faculty:")
        for i in range(len(fac.cathedras)):
            for cath in fac.cathedras:
                print(f"{i + 1}.{cath.name}")
        print("Here is a list of actions you can do:")
        print("1. View info of cathedra (enter the number of cathedra")
        print("2. Add cathedra")
        print("3. Delete cathedra")
        print("4. Go back")
        ask = int(input('>>>'))
        if ask == 1:
            num_cath = int(input('Enter the number of cathedra \n>>>'))
            cathedra = fac.cathedras[num_cath - 1]
            # for i in range(fac.cathedras):
            #     for cath in fac.cathedras:
            #         if i == num_cath:
            #             print(f"You chose {cath.name}! ")
            #             student_teacher(cath)
            student_teacher(cathedra)
        elif ask == 2:
            cathedra_create(fac)
        elif ask == 3:
            faculty_delete(faculty)
        elif ask == 4:
            break
        else:
            continue


def student_teacher(cathedra):
    while True:
        print(''' *** Student ***
    Add Student (SA)
    Edit Student (SE)
    Delete Student (SD)
    Sort by alphabet (SBA)
    Sort by year (SBY)
    Sort students of the course (SC)
    Get Students by Group (SBG)
    Get Student by Surname (SBS)

    *** Teacher ***
    Add Teacher (TA)
    Edit Teacher (TE)
    Delete Teacher (TD)
    Sort by alphabet (TBA)
    Get Teacher by Surname (TBS)
    Get Teachers by Group (TBG)

    Quit (Q)
        ''')
        ask = input(f"What do you want to do in terms of {cathedra.name} cathedra?").lower()
        if ask.startswith("q"):
            break
        elif ask.startswith('sa'):
            newstudent = student_pref(cathedra.name)
            cathedra.add_student(newstudent)
        elif ask.startswith('se'):
            student = input("Whom do you want to edit?:")
            cathedra.edit_student(student)
        elif ask.startswith("sd"):
            student = input("Whom do you want to delete?:")
            cathedra.remove_student(student)
        elif ask.startswith("sba"):
            cathedra.sort_student_by_name()
        elif ask.startswith("sbg"):
            group = int(input("Enter the group:"))
            cathedra.get_student_by_group(group)
        elif ask.startswith("sbs"):
            name = input("Enter the full name of student you want to find info about:")
            cathedra.get_student_by_surname(name)
        elif ask.startswith("ta"):
            newteacher = teacher_pref(cathedra.name)
            cathedra.add_teacher(newteacher)
        elif ask.startswith("te"):
            teacher = input("Enter teacher's name:")
            cathedra.edit_teacher(teacher)
        elif ask.startswith("td"):
            teacher = input("Whom do you want to delete?:")
            cathedra.remove_teacher(teacher)
        elif ask.startswith("tba"):
            cathedra.sort_teacher_by_name()
        elif ask.startswith("tbg"):
            group = int(input("Enter the group:"))
            cathedra.get_teacher_by_group(group)
        elif ask.startswith("tbs"):
            name = input("Enter the full name of teacher you want to find info about:")
            cathedra.get_teacher_by_surname(name)

if __name__ == '__main__':
    main()
