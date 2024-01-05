from tkinter import *
import MySQLdb

# Establish a connection to the MySQL database
db = MySQLdb.connect("127.0.0.1", "root", "Nk@123", "python_sql")

# Create a cursor object to interact with the database
cursor = db.cursor()

def create_record():
    sex = "Male" if C1.get() == "M" else "Female"
    sql = "INSERT INTO EMPLOYEE_DETAILS(empno, empname, sex, age, desig, salary) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (int(T1.get()), T2.get(), sex, int(T3.get()), T4.get(), float(T5.get()))
    cursor.execute(sql, values)
    db.commit()

def read_records():
    sql="SELECT * FROM EMPLOYEE_DETAILS"
    cursor.execute(sql)
    try:
        records = cursor.fetchall()
        for record in records:
            empno=record[0]
            empname=record[1]
            gender=record[2]
            desig=record[3]
            salary=record[4]
        print("Employee No=",(empno))
        print("Employee Name=",(empname))
        print("Gender=",(gender))
        print("Designation=",(desig))
        print("Salary=",(salary))
    except:
        print("No Data")
        

def update_record():
    sex = "Male" if C1.get() == "M" else "Female"
    sql = "UPDATE EMPLOYEE_DETAILS SET empname=%s, sex=%s, age=%s, desig=%s, salary=%s WHERE empno=%s"
    values = (T2.get(), sex, int(T3.get()), T4.get(), float(T5.get()), int(T1.get()))
    cursor.execute(sql, values)
    db.commit()

def delete_record():
    sql = "DELETE FROM EMPLOYEE_DETAILS WHERE empno=%s"
    cursor.execute(sql, (int(T1.get()),))
    db.commit()

master = Tk()

group = LabelFrame(master, text="EMPLOYEE DATA ENTRY SCREEN", padx=10, pady=10)
group.pack(padx=10, pady=10)

T1 = StringVar()
T2 = StringVar()
T3 = StringVar()
T4 = StringVar()
T5 = StringVar()
C1 = StringVar()

Label(group, text="Employee No").grid(row=0, column=3)
W1 = Entry(group, textvariable=T1).grid(row=0, column=20, padx=10, pady=10)

Label(group, text="Employee Name").grid(row=3, column=3)
W2 = Entry(group, textvariable=T2).grid(row=3, column=20, padx=10, pady=10)

Label(group, text="Age").grid(row=9, column=3)
W3 = Entry(group, textvariable=T3).grid(row=9, column=20, padx=10, pady=10)

Label(group, text="Designation").grid(row=12, column=3)
W4 = Entry(group, textvariable=T4).grid(row=12, column=20, padx=10, pady=10)

Label(group, text="Sex").grid(row=6, column=3)
R1 = Radiobutton(group, text="Male", variable=C1, value="M").grid(row=6, column=19, padx=10, pady=10)
R2 = Radiobutton(group, text="Female", variable=C1, value="F").grid(row=6, column=20, padx=10, pady=10)

Label(group, text="Salary").grid(row=15, column=3)
W5 = Entry(group, textvariable=T5).grid(row=15, column=20, padx=10, pady=10)

# CRUD Buttons
Button(group, text="Add", command=create_record).grid(row=18, column=15, padx=10, pady=10)
Button(group, text="View", command=read_records).grid(row=18, column=16, padx=10, pady=10)
Button(group, text="Update", command=update_record).grid(row=18, column=17, padx=10, pady=10)
Button(group, text="Delete", command=delete_record).grid(row=18, column=18, padx=10, pady=10)

C1.set("M")

mainloop()
db.close()
