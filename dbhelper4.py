import mysql.connector as connector

class DBHelper4:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                      port='3306',
                      user='root',
                      password='Shrikant@06',
                      database='Human_Resources_Data')

#Insert
    def insert_employee(self,Employe_ID,First_Name,Last_Name,Email,Phone_No,Hire_Date,Salary,Department_ID,Project_Name,Role_ID,DOB,Address,Age):
        query="insert into employee(Employe_ID,First_Name,Last_Name,Email,Phone_No,Hire_Date,Salary,Department_ID,Project_Name,Role_ID,DOB,Address,Age) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(Employe_ID,First_Name,Last_Name,Email,Phone_No,Hire_Date,Salary,Department_ID,Project_Name,Role_ID,DOB,Address,Age)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("saved to database")
    
#Fech all
    def fetch_all(self):
        query="select * from employee"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Employe ID: ", row[0])
            print("First name: ", row[1])
            print("Last name: ", row[2])
            print("Email : ", row[3])
            print("Phone no: ", row[4])
            print("Hire date: ", row[5])
            print("Salary: ", row[6])
            print("Department ID: ", row[7])
            print("Project name: ", row[8])
            print("Role ID: ", row[9])
            print("DOB : ", row[10])
            print("Address : ", row[11])
            print("Age : ", row[12])
            print()
            print()

#delete user
    def delete_employee(self,Employe_ID):
        query="delete from employee where Employe_ID='{}'".format(Employe_ID)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

#update
    def update_employee(self,Employe_ID,First_Name,Last_Name,Email,Phone_No,Hire_Date,Salary,Department_ID,Project_Name,Role_ID,DOB,Address,Age):
        query="update employee set First_Name='{}',Last_Name='{}',Email='{}',Phone_No='{}',Hire_Date='{}',Salary='{}',Department_ID='{}',Project_Name='{}',Role_ID='{}',DOB='{}',Address='{}',Age='{}' where Employe_ID='{}'".format(First_Name,Last_Name,Email,Phone_No,Hire_Date,Salary,Department_ID,Project_Name,Role_ID,DOB,Address,Age,Employe_ID)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")
#main coding
helper=DBHelper4()