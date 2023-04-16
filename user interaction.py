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
                print(f"{i+1}.{fac.name}")
        print("Here is a list of actions you can do:")
        print("1. View info of faculty (enter the number of faculty)")
        print("2. Add faculty")
        print("3. Delete faculty")
        print("4. Go back")
        ask = int(input('>>>'))
        if ask == 1:
            num_fac = int(input('Enter the number of faculty \n>>>'))
            for i in range(all_faculties):
                for fac in all_faculties:
                    if i == num_fac:
                        print(f"You chose {fac.name}! ")
                        cathedra_interaction(fac)
        elif ask == 2:
            faculty_create()
        elif ask == 3:
            choose = int(input("Enter the number of faculty you want to delete."))
            if choose <= len(all_faculties):
                faculty = all_faculties[choose-1]
                faculty_delete(faculty)
                return
            print("No faculty with this number")
        elif ask == 4:
            break
        else:
            continue


# def cathedra_interaction(faculty):
#     for fac in all_faculties:
#         if fac
