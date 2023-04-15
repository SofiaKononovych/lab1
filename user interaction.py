from uni import *


def main():
    ask = input(''' MENU
Add Faculty
View Faculties
Quit
>>>
''').lower()
    if ask.startswith("q"):
        return
    elif ask.startswith('a'):
        faculty_create()
        return
    elif ask.startswith("v"):
        print("Here is the list of all faculties. Choose the faculty number.")

        for fac in all_faculties:
            print ()

def faculty_interaction():




# def cathedra_interaction(faculty):
#     for fac in all_faculties:
#         if fac
