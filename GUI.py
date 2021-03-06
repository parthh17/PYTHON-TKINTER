from tkinter import *
import tkinter

top = tkinter.Tk()
count = 0

student_name = StringVar()
roll_no = StringVar()
branch = StringVar()
elective_opted = StringVar()
CGPA = StringVar()



def Add_student_name():
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'a')
    student_name = E1.get()
    roll_no = E2.get()
    branch = E3.get()
    elective_opted = E4.get()
    CGPA = E5.get()
    if (student_name == '' or roll_no == '' or branch == '' or elective_opted == '' or CGPA == ''):
        print("Details can't be empty!")
        exit()
    f.writelines(
        student_name.ljust(20) + roll_no.ljust(20) + branch.ljust(20) + elective_opted.ljust(20) + CGPA.ljust(
            3) + "\n")
    print("Record added to file!")

    f.close()


def Delete_student_name():
    k = student_name.get()
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'r')
    ctr = 0
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines = f.readlines()
    print(lines)
    f.close()
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'w')
    for book in lines:
        j = book.split()
        print(j)
        if (j[0] != k):
            f.writelines(j[0].ljust(20) + j[1].ljust(20) + j[2].ljust(20) + j[3].ljust(20) + j[4].ljust(5) + "\n")
            print("Record deleted from the file!!")
    student_name.set("")
    roll_no.set("")
    branch.set("")
    elective_opted.set("")
    CGPA.set("")
    f.close()


def Search_student_name():
    k = student_name.get()
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'r')
    ctr = 0
    flag = 0
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines = f.readlines()
    print(lines)
    for book in lines:
        j = book.split()
        if (j[0] == k):
            print(j)
            student_name.set(j[0])
            roll_no.set(j[1])
            branch.set(j[2])
            elective_opted.set(j[3])
            CGPA.set(j[4])
            flag = 1
            break
    if (flag == 0):
        print("Record not found!")
    else:
        print("Record found!")
    student_name.set("")
    roll_no.set("")
    branch.set("")
    elective_opted.set("")
    CGPA.set("")
    f.close()


def Update_student_name():
    new_id = student_name.get()
    new_name = roll_no.get()
    new_price = branch.get()
    new_author = elective_opted.get()
    new_publisher = CGPA.get()
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'r')
    ctr = 0
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines = f.readlines()
    f.close()
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'w')
    for book in lines:
        j = book.split()
        if (j[0] != new_id):
            f.writelines(j[0].ljust(3) + j[1].ljust(20) + j[2].ljust(20) + j[3].ljust(20) + j[4].ljust(5) + "\n")

        else:
            f.writelines(
                j[0].ljust(3) + new_name.ljust(20) + new_price.ljust(20) + new_author.ljust(20) + new_publisher.ljust(
                    5) + "\n")
    print("Record updated!!")
    student_name.set("")
    roll_no.set("")
    branch.set("")
    elective_opted.set("")
    CGPA.set("")
    f.close()


def Get_First_Record():
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'r')
    ctr = 0
    flag = 0
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines = f.readlines()
    l = list(lines)
    print("\n")
    print(l)
    j = l[0].split()
    student_name.set(j[0])
    roll_no.set(j[1])
    branch.set(j[2])
    elective_opted.set(j[3])
    CGPA.set(j[4])
    print("\n First Record of file is as:")
    print(l[0])
    f.close()


def Get_Last_Record():
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'r')
    ctr = 0
    flag = 0
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines = f.readlines()
    l = list(lines)
    print(l)
    j = l[ctr - 1].split()
    student_name.set(j[0])
    roll_no.set(j[1])
    branch.set(j[2])
    elective_opted.set(j[3])
    CGPA.set(j[4])
    print("\n Last Record of file is as:")
    print(l[ctr - 1])
    f.close()


def Get_Prev_Record():
    global count
    i = 0
    ctr = 0
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'r')
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    try:

        while (i <= count - 1):
            l = f.readline()
            i = i + 1

        m = l.split()
        student_name.set(m[0])
        roll_no.set(m[1])
        branch.set(m[2])
        elective_opted.set(m[3])
        CGPA.set(m[4])
        print(m)

    except:
        student_name.set("")
        roll_no.set("")
        branch.set("")
        elective_opted.set("")
        CGPA.set("")
        print("Sorry, no more records!")
    count = count - 1
    f.close()


def Get_Next_Record():
    global count
    i = 0
    ctr = 0
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'r')
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    try:

        while (i <= count):
            l = f.readline()
            i = i + 1

        m = l.split()
        student_name.set(m[0])
        roll_no.set(m[1])
        branch.set(m[2])
        elective_opted.set(m[3])
        CGPA.set(m[4])
        print(m)

    except:
        student_name.set("")
        roll_no.set("")
        branch.set("")
        elective_opted.set("")
        CGPA.set("")
        print("Sorry, no more records!")
    count = count + 1
    f.close()


top.configure(background="grey")


w = tkinter.Label(top, text="NCU STUDENT DETAILS", bg="grey", font=('calibri', 15, 'bold'), underline=-1).grid(row=0,
                                                                                                               column=1)
tkinter.Label(top, text="STUDENT NAME:", bg="grey", font=('calibri', 15, 'bold')).grid(row=5, sticky=W)
tkinter.Label(top, text="ROLL NO:", bg="grey", font=('calibri', 15, 'bold')).grid(row=6, sticky=W)
tkinter.Label(top, text="BRANCH:", bg="grey", font=('calibri', 15, 'bold')).grid(row=7, sticky=W)
tkinter.Label(top, text="ELECTIVE OPTED:", bg="grey", font=('calibri', 15, 'bold')).grid(row=8, sticky=W)
tkinter.Label(top, text="CGPA:", bg="grey", font=('calibri', 15, 'bold')).grid(row=9, sticky=W)



E1 = tkinter.Entry(top, textvariable=student_name)
E2 = tkinter.Entry(top, textvariable=roll_no)
E3 = tkinter.Entry(top, textvariable=branch)
E4 = tkinter.Entry(top, textvariable=elective_opted)
E5 = tkinter.Entry(top, textvariable=CGPA)
E1.grid(row=5, column=1)
E2.grid(row=6, column=1)
E3.grid(row=7, column=1)
E4.grid(row=8, column=1)
E5.grid(row=9, column=1)



fr = tkinter.Button(top, text="|<", width=15, bg="white", font=('Ariel', 15, 'bold'),
                    command=Get_First_Record).grid(row=10, column=0)
pr = tkinter.Button(top, text="<", width=15, bg="white", font=('Ariel', 15, 'bold'), command=Get_Prev_Record).grid(
    row=10, column=1)
nr = tkinter.Button(top, text=">", width=15, bg="white", font=('Ariel', 15, 'bold'), command=Get_Next_Record).grid(
    row=10, column=2)
lr = tkinter.Button(top, text=">|", width=15, bg="white", font=('Ariel', 15, 'bold'), command=Get_Last_Record).grid(
    row=10, column=3)

rb = tkinter.Button(top, text="ADD", width=15, bg="white", font=('Ariel', 15, 'bold'), command=Add_student_name).grid(
    row=11, column=0)
db = tkinter.Button(top, text="DELETE", width=15, bg="white", font=('Ariel', 15, 'bold'),
                    command=Delete_student_name).grid(
    row=11, column=1)
sb = tkinter.Button(top, text="SEARCH", width=15, bg="white", font=('Ariel', 15, 'bold'),
                    command=Search_student_name).grid(
    row=11, column=2)
ub = tkinter.Button(top, text="UPDATE", width=15, bg="white", font=('Ariel', 15, 'bold'),
                    command=Update_student_name).grid(
    row=11, column=3)
top.mainloop()
from tkinter import *
import tkinter

top = tkinter.Tk()
count = 0

student_name = StringVar()
roll_no = StringVar()
branch = StringVar()
elective_opted = StringVar()
CGPA = StringVar()




def Add_Book():
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'a')
    student_name = E1.get()
    roll_no = E2.get()
    branch = E3.get()
    elective_opted = E4.get()
    CGPA = E5.get()
    if (student_name == '' or roll_no == '' or branch == '' or elective_opted == '' or CGPA == ''):
        print("Details can't be empty!")
        exit()
    f.writelines(
        student_name.ljust(20) + roll_no.ljust(20) + branch.ljust(20) + elective_opted.ljust(20) + CGPA.ljust(3) + "\n")
    print("Record added to file!")
    student_name.set("")
    roll_no.set("")
    branch.set("")
    elective_opted.set("")
    CGPA.set("")
    f.close()


def Delete_Book():
    k = student_name.get()
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'r')
    ctr = 0
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines = f.readlines()
    print(lines)
    f.close()
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'w')
    for book in lines:
        j = book.split()
        print(j)
        if (j[0] != k):
            f.writelines(j[0].ljust(20) + j[1].ljust(20) + j[2].ljust(20) + j[3].ljust(20) + j[4].ljust(5) + "\n")
            print("Record deleted from the file!!")
    student_name.set("")
    roll_no.set("")
    branch.set("")
    elective_opted.set("")
    CGPA.set("")
    f.close()


def Search_Book():
    k = student_name.get()
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'r')
    ctr = 0
    flag = 0
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines = f.readlines()
    print(lines)
    for book in lines:
        j = book.split()
        if (j[0] == k):
            print(j)
            student_name.set(j[0])
            roll_no.set(j[1])
            branch.set(j[2])
            elective_opted.set(j[3])
            CGPA.set(j[4])
            flag = 1
            break
    if (flag == 0):
        print("Record not found!")
    else:
        print("Record found!")
    student_name.set("")
    roll_no.set("")
    branch.set("")
    elective_opted.set("")
    CGPA.set("")
    f.close()


def Update_Book():
    new_id = student_name.get()
    new_name = roll_no.get()
    new_price = branch.get()
    new_author = elective_opted.get()
    new_publisher = CGPA.get()
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'r')
    ctr = 0
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines = f.readlines()
    f.close()
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'w')
    for book in lines:
        j = book.split()
        if (j[0] != new_id):
            f.writelines(j[0].ljust(3) + j[1].ljust(20) + j[2].ljust(20) + j[3].ljust(20) + j[4].ljust(5) + "\n")

        else:
            f.writelines(
                j[0].ljust(3) + new_name.ljust(20) + new_price.ljust(20) + new_author.ljust(20) + new_publisher.ljust(
                    5) + "\n")
    print("Record updated!!")
    student_name.set("")
    roll_no.set("")
    branch.set("")
    elective_opted.set("")
    CGPA.set("")
    f.close()


def Get_First_Record():
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'r')
    ctr = 0
    flag = 0
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines = f.readlines()
    l = list(lines)
    print("\n")
    print(l)
    j = l[0].split()
    student_name.set(j[0])
    roll_no.set(j[1])
    branch.set(j[2])
    elective_opted.set(j[3])
    CGPA.set(j[4])
    print("\n First Record of file is as:")
    print(l[0])
    f.close()


def Get_Last_Record():
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'r')
    ctr = 0
    flag = 0
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines = f.readlines()
    l = list(lines)
    print(l)
    j = l[ctr - 1].split()
    student_name.set(j[0])
    roll_no.set(j[1])
    branch.set(j[2])
    elective_opted.set(j[3])
    CGPA.set(j[4])
    print("\n Last Record of file is as:")
    print(l[ctr - 1])
    f.close()


def Get_Prev_Record():
    global count
    i = 0
    ctr = 0
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'r')
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    try:

        while (i <= count - 1):
            l = f.readline()
            i = i + 1

        m = l.split()
        student_name.set(m[0])
        roll_no.set(m[1])
        branch.set(m[2])
        elective_opted.set(m[3])
        CGPA.set(m[4])
        print(m)

    except:
        student_name.set("")
        roll_no.set("")
        branch.set("")
        elective_opted.set("")
        CGPA.set("")
        print("Sorry, no more records!")
    count = count - 1
    f.close()


def Get_Next_Record():
    global count
    i = 0
    ctr = 0
    f = open('C:/Users/Admin/Desktop/college_db.txt', 'r')
    for line in f:
        ctr = ctr + 1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    try:

        while (i <= count):
            l = f.readline()
            i = i + 1

        m = l.split()
        student_name.set(m[0])
        roll_no.set(m[1])
        branch.set(m[2])
        elective_opted.set(m[3])
        CGPA.set(m[4])
        print(m)

    except:
        student_name.set("")
        roll_no.set("")
        branch.set("")
        elective_opted.set("")
        CGPA.set("")
        print("Sorry, no more records!")
    count = count + 1
    f.close()


top.configure(background="grey")


w = tkinter.Label(top, text="NCU STUDENT DETAILS", bg="yellow", font=('calibri', 15, 'bold'), underline=12).grid(row=0,
                                                                                                                 column=1)
tkinter.Label(top, text="STUDENT NAME:", bg="grey", font=('calibri', 15, 'bold')).grid(row=5, sticky=W)
tkinter.Label(top, text="ROLL NO.:", bg="grey", font=('calibri', 15, 'bold')).grid(row=6, sticky=W)
tkinter.Label(top, text="BRANCH:", bg="grey", font=('calibri', 15, 'bold')).grid(row=7, sticky=W)
tkinter.Label(top, text="ELECTIVE_SUBJECT:", bg="grey", font=('calibri', 15, 'bold')).grid(row=8, sticky=W)
tkinter.Label(top, text="CGPA:", bg="grey", font=('calibri', 15, 'bold')).grid(row=9, sticky=W)



E1 = tkinter.Entry(top, textvariable=student_name)
E2 = tkinter.Entry(top, textvariable=roll_no)
E3 = tkinter.Entry(top, textvariable=branch)
E4 = tkinter.Entry(top, textvariable=elective_opted)
E5 = tkinter.Entry(top, textvariable=CGPA)
E1.grid(row=5, column=1)
E2.grid(row=6, column=1)
E3.grid(row=7, column=1)
E4.grid(row=8, column=1)
E5.grid(row=9, column=1)



fr = tkinter.Button(top, text="|<", width=15, bg="white", font=('Ariel', 15, 'bold'),
                    command=Get_First_Record).grid(row=10, column=0)
pr = tkinter.Button(top, text="<", width=15, bg="white", font=('Ariel', 15, 'bold'), command=Get_Prev_Record).grid(
    row=10, column=1)
nr = tkinter.Button(top, text=">", width=15, bg="white", font=('Ariel', 15, 'bold'), command=Get_Next_Record).grid(
    row=10, column=2)
lr = tkinter.Button(top, text=">|", width=15, bg="white", font=('Ariel', 15, 'bold'), command=Get_Last_Record).grid(
    row=10, column=3)

rb = tkinter.Button(top, text="ADD", width=15, bg="white", font=('Ariel', 15, 'bold'), command=Add_student_name).grid(
    row=11, column=0)
db = tkinter.Button(top, text="DELETE", width=15, bg="white", font=('Ariel', 15, 'bold'),
                    command=Delete_student_name).grid(
    row=11, column=1)
sb = tkinter.Button(top, text="SEARCH", width=15, bg="white", font=('Ariel', 15, 'bold'),
                    command=Search_student_name).grid(
    row=11, column=2)
ub = tkinter.Button(top, text="UPDATE", width=15, bg="white", font=('Ariel', 15, 'bold'),
                    command=Update_student_name).grid(
    row=11, column=3)
top.mainloop()
