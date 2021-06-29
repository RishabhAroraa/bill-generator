# author: rishabharoraa.github.io
from tkinter import *
from tkinter import ttk
from reportlab.pdfgen import canvas

# basic configuration
window = Tk()
window.title("Employee Report")
window.geometry("480x640")

# window.background("#282828")

# heading
heading = Label(window, text="Generate Weekly Report", font = ('',15,'bold'), pady=20).pack()

# form
employeeID = Label(window, text="Employee ID").pack()
employeeIDEntry = Entry(window)
employeeIDEntry.pack()

employeeName = Label(window, text="Employee Name").pack()
employeeNameEntry = Entry(window)
employeeNameEntry.pack()

employeeDepartment = Label(window, text="Department").pack()
employeeDepartmentEntry = Entry(window)
employeeDepartmentEntry.pack()

completedTasks = Label(window, text="Completed Tasks").pack()
completedTasksEntry = Text(window, height=7, width=50)
completedTasksEntry.pack()

ongoingTasks = Label(window, text="Ongoing Tasks").pack()
ongoingTasksEntry = Text(window, height=7, width=50)
ongoingTasksEntry.pack()

nextWeekTasks = Label(window, text="Tasks for next week").pack()
nextWeekTasksEntry = Text(window, height=7, width=50)
nextWeekTasksEntry.pack()

def generatePDF(empID, empName, empDepartment, completedTasksList, ongoingTasksList, nextWeekTasksList):

    fileName = "report.pdf"
    res = canvas.Canvas(fileName)
    res.setTitle("report")
    res.setFont("Courier-Bold",24)
    res.drawString(50,775,"SAMPLE COMPANY")
    res.setFont("Courier-Bold",16)
    res.drawString(50,750,"Weekly Report")
    res.setFont("Courier",12)

    res.drawString(50,700,"Employee ID: "+empID)
    res.drawString(50,675,"Employee Name: "+empName)
    res.drawString(50,650,"Employee Department: "+empDepartment)

    text = res.beginText(50,600)

    text.setFont("Courier-Bold", 14)
    text.textLine("Completed Tasks: ")
    text.setFont("Courier", 12)
    text.textLine("")
    for element in completedTasksList:
        text.textLine("> "+element)
    text.textLine("")

    text.setFont("Courier-Bold", 14)
    text.textLine("Ongoing Tasks: ")
    text.setFont("Courier", 12)
    text.textLine("")
    for element in ongoingTasksList:
        text.textLine("> "+element)
    text.textLine("")

    text.setFont("Courier-Bold", 14)
    text.textLine("Next Week Tasks: ")
    text.setFont("Courier", 12)
    text.textLine("")
    for element in nextWeekTasksList:
        text.textLine("> "+element)
    text.textLine("")



    res.drawText(text)
    res.save()



def getAllTasks():

    completedTasksList = completedTasksEntry.get('1.0', 'end - 1c').split('\n')
    ongoingTasksList = ongoingTasksEntry.get('1.0', 'end - 1c').split('\n')
    nextWeekTasksList = nextWeekTasksEntry.get('1.0', 'end - 1c').split('\n')
    generatePDF(employeeIDEntry.get(), employeeNameEntry.get(), employeeDepartmentEntry.get(), completedTasksList, ongoingTasksList, nextWeekTasksList)

submitItem = Button(window, text="Submit", command=getAllTasks).pack()

# TODO :
# make a new Bill Object
# make a new Item Object when the button is clicked


window.mainloop()
