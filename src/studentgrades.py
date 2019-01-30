#studentgrades.py
#   Plot a horizontal bar chart of student exam scores

from graphics import *
from tkinter.filedialog import askopenfilename

def main():
    print("Choose a file you want chart-ified\n")

    studFile = askopenfilename(filetypes=[("Text Document", ".txt"), ("Text Document", ".doc"), ("Text Document", ".docx")])
    grades = open(studFile, "r")

    #get list of lines
    gradesls = grades.readlines()

    #remove newlines from list
    gradesls = [e.rstrip() for e in gradesls]

    #Get student count
    students = int(gradesls[0])

    #get list of names
    names = []
    for student in gradesls[1:]:
        if student[-3:] == "100":
            names.append(student[:-4])
        else:
            names.append(student[:-3])

    #get list of grades
    grades = []
    for student in gradesls[1:]:
        if student[-3:] == "100":
            grades.append(int(student[-3:]))
        else:
            grades.append(int(student[-2:]))

    #Initialize Window
    win = GraphWin("Grades Chart", 600, 50 * students)
    win.setCoords(-20, 0.0, 100, students * 2)

    #Get longest name
    size = (len(max(names, key=len)))

    #Draw Names
    for name in names:
        lbl = ("{0:>{1}}").format(name, size)
        Text(Point(-10, names.index(name) * 2 + 1), lbl).draw(win)

    #Draw Animated bars
    iterations  = max(grades)
    for i in range(iterations + 1):
        for grade in grades:
            rect = Rectangle(Point(0.0, grades.index(grade) * 2 + 0.5), Point((grade / iterations) * i, grades.index(grade) * 2 + 1.5))
            rect.setFill("green")
            rect.setWidth("2")
            rect.setOutline("black")
            rect.draw(win)




    win.getMouse()
main()
