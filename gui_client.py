from tkinter import *
import random
import string
import logging
import grpc
import task_pb2
import task_pb2_grpc


def guiAdd():
    logging.basicConfig(level=logging.DEBUG)
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = task_pb2_grpc.TaskapiStub(channel)
        # Code to add widgets will go here...
        desc = e1.get()
        response = stub.addTask(task_pb2.TaskDesc(description=desc))
        response1 = stub.listTasks(task_pb2.Empty())
        l3.configure(text=str(f"Task list \n{response1.tasks}"))
        # addLabel.configure(text=str(f"Task ids {task_ids}"))


def guiDelete():
    logging.basicConfig(level=logging.DEBUG)
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = task_pb2_grpc.TaskapiStub(channel)
        i = int(e2.get())
        response = stub.delTask(task_pb2.Id(id=i))
        response1 = stub.listTasks(task_pb2.Empty())
        l3.configure(text=str(f"Task list \n{response1.tasks}"))


if __name__ == "__main__":

    mainWindow = Tk()
    mainWindow.title("TUSKER TASKS")
    l1 = Label(mainWindow, text="Enter Task:")
    l2 = Label(mainWindow, text="Enter ID:")

    # grid method to arrange labels in respective
    # rows and columns as specified
    l1.grid(row=0, column=0, sticky=W, pady=3)
    l2.grid(row=1, column=0, sticky=W, pady=3)

    # entry widgets, used to take entry from user
    e1 = Entry(mainWindow)
    e2 = Entry(mainWindow)

    # this will arrange entry widgets
    e1.grid(row=0, column=1, pady=3)
    e2.grid(row=1, column=1, pady=3)

    b1 = Button(mainWindow, text="Add Task",
                bg="blue", fg="white", command=guiAdd)
    b2 = Button(mainWindow, text="Delete Task",
                bg="blue", fg="white", command=guiDelete)

    b1.grid(row=0, column=2, pady=3)
    b2.grid(row=1, column=2, pady=3)

    l3 = Label(mainWindow, text="To Do:")
    l3.grid(row=2, column=0, padx=50, pady=50)

    mainWindow.mainloop()
