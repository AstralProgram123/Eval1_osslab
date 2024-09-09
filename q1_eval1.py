Emp=[{"Name":"Aryan","ID":1234,"Dept":"Sales","Salary":50000.00},{"Name":"Raghav","ID":1235,"Dept":"IT","Salary":30000.00},
     {"Name":"Parth","ID":1236,"Dept":"Sales","Salary":45000.00},{"Name":"Varun","ID":1237,"Dept":"HR","Salary":27000.00}
     ,{"Name":"Vids","ID":1238,"Dept":"Research","Salary":50000.00},{"Name":"Alex","ID":1239,"Dept":"HR","Salary":30000.00}]

def newemp():
    Name=input("Enter the NAME: ")
    ID=int(input("Enter the Emp ID: "))
    Dept=input("Enter the Department: ")
    Salary=float(input("Enter the Salary: "))
    d={"Name":Name,"ID":ID,"Dept":Dept,"Salary":Salary}
    Emp.append(d)

def update(Id):
    A=input("Enter what you want to update: ")
    for i in Emp:
        if i["ID"]==Id:
            if A=="Salary":
                B=float(input("Enter the updated salary: "))
                i[A]=B
                break
            else:
                C=input("Enter the updated value: ")
                i[A]=C
                break
    else:
        print("Employee Does not Exist")

def search(Id):
    for i in Emp:
        if i["ID"]==Id:
            print("Employee Found: ")
            print(i)
            break
    else:
        print("Employee Does not Exist")

def deprec(dept):
    print("The report of Employees are: \n")
    for i in Emp:
        if i["Dept"]==dept:
            print(i,"\n")
    else:
        print("No such Employee with this Department exists")

print("To Add New Employee Enter 1\n")
print("To Update Employee Records Enter 2\n")
print("To Search for the Employee Enter 3\n")
print("To Generate Employee Report bases on Dept Enter 4\n")
print("To Display the Employee list Enter 5\n")
ch=int(input("Enter your choice: "))
while ch!=0:
    if ch==1:
        newemp()
    elif ch==2:
        Id=int(input("Enter the Id of the Employee you want to update: "))
        update(Id)
    elif ch==3:
        Id=int(input("Enter the Id of the Employee you want to search for: "))
        search(Id)
    elif ch==4:
        dept=input("Enter the Department of the Employees: ")
        deprec(dept)
    elif ch==5:
        print("The Employee List is: \n")
        for i in Emp:
            print(i,"\n")
    ch=int(input("\nEnter 0 to exit or other numbers(1-5) to continue: "))
