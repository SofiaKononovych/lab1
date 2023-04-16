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
        print("4. Edit cathedra")
        print("5. Get all students sorted by year")
        print("6. Get all students sorted by alphabet")
        print("7. Get all teachers sorted by alphabet")
        print("8. Go back")
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
            cathedra_create()
        elif ask == 3:
            choose = int(input("Enter the number of cathedra you want to delete."))
            if choose <= len(fac.cathedras):
                cath = fac.cathedras[choose - 1]
                fac.remove_cathedra(cath)
                return
            print("No cathedra with this number")
        elif ask == 4:
            num_cath = int(input('Enter the number of cathedra you want to edit\n>>>'))
            cathedra = fac.cathedras[num_cath - 1]
            fac.edit_cathedra(cathedra)
        elif ask == 5:
            sort_student_by_year()
        elif ask == 6:
            fac.get_students_sorted()
        elif ask == 7:
            fac.get_teachers_sorted()
        elif ask == 8:
            break
        else:
            continue


def student_teacher(cathedra):
    while True:
        print(''' *** Student ***
    Add Student (SA)     done
    Edit Student (SE)      done
    Delete Student (SD)     done

    Get Student by Surname (SBS)   done
    Get Student By Year  (SBY) done
    Get Students by Group (SBG) done

    Sort all students of cathedra by year (SABY)  done
    Sort by alphabet (SBA)    done
    Sort students of the year (SGY) done
    Sort year by alphabet (SYA) done


    *** Teacher ***
    Add Teacher (TA) done
    Edit Teacher (TE) done
    Delete Teacher (TD) done

    Sort by alphabet (TBA)   done
    Get Teacher by Surname (TBS)     done
    Get Teachers by Group (TBG)     done

    Quit (Q)
        ''')
        ask = input(f"What do you want to do in terms of {cathedra.name} cathedra?").lower()
        if ask.startswith("q"):
            break
        elif ask.startswith('sa'):  # SA
            newstudent = student_pref(cathedra.name)
            cathedra.add_student(newstudent)
        elif ask.startswith('se'):  # SE
            student = input("Whom do you want to edit?:")
            cathedra.edit_student(student)
        elif ask.startswith("sd"):  # SD
            student = input("Whom do you want to delete?:")
            cathedra.remove_student(student)
        elif ask.startswith("sbs"):  # SBS
            name = input("Enter the full name of student you want to find info about:")
            cathedra.get_student_by_surname(name)
        elif ask.startswith("sby"):  # SBY
            year = int(input("Enter the year and you`ll receive a list of students of this year:"))
            cathedra.get_student_by_year(year)
        elif ask.startswith("sbg"):  # SBG
            group = int(input("Enter the group and you`ll receive a list of students of this group:"))
            cathedra.get_student_by_group(group)
        elif ask.startswith("saby"):  # SABY
            cathedra.sort_student_by_year()
        elif ask.startswith("sba"):  # SBA
            cathedra.sort_student_by_name()
        elif ask.startswith("sgy"):  # SGY
            year = int(input("Enter the year please:"))
            cathedra.get_stud_of_cath_by_year(year)
        elif ask.startswith("sya"):  # SYA
            year = int(input("Enter the year please:"))
            cathedra.sort_student_of_course_by_alph(year)

        elif ask.startswith("ta"):  # TA
            newteacher = teacher_pref(cathedra.name)
            cathedra.add_teacher(newteacher)
        elif ask.startswith("te"):  # TE
            teacher = input("Enter teacher's full name:")
            cathedra.edit_teacher(teacher)
        elif ask.startswith("td"):  # TD
            teacher = input("Whom do you want to delete?:")
            cathedra.remove_teacher(teacher)
        elif ask.startswith("tbs"):  # TBS
            name = input("Enter the full name of teacher you want to find info about:")
            cathedra.get_teacher_by_surname(name)
        elif ask.startswith("tbg"):  # TBG
            group = int(input("Enter the group and you'll receive the teacher who :"))
            cathedra.get_teacher_by_group(group)
        elif ask.startswith("tba"):  # TBA
            cathedra.sort_teacher_by_name()


if __name__ == '__main__':
    main()
