# author: rishabharoraa.github.io
from tkinter import *
from tkinter import ttk

# basic configuration
window = Tk()
window.title("Employee Report")
window.geometry("480x640")

# window.background("#282828")

# heading
heading = Label(window, text="Generate Weekly Report", font = ('',15,'bold'), pady=20).pack()

# form
employeeID = Label(window, text="Employee ID").pack()
employeeIDEntry = Entry(window).pack()

employeeName = Label(window, text="Employee Name").pack()
employeeNameEntry = Entry(window).pack()

employeeDepartment = Label(window, text="Department").pack()
employeeDepartmentEntry = Entry(window).pack()

completedTasks = Label(window, text="Completed Tasks").pack()
completedTasksEntry = Text(window, height=7, width=50).pack()

ongoingTasks = Label(window, text="Ongoing Tasks").pack()
ongoingTasksEntry = Text(window, height=7, width=50).pack()

nextWeekTasks = Label(window, text="Tasks for next week").pack()
nextWeekTasksEntry = Text(window, height=7, width=50).pack()

submitItem = Button(window, text="Submit").pack()

# TODO :
# make a new Bill Object
# make a new Item Object when the button is clicked


window.mainloop()
