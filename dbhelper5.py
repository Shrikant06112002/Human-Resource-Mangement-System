import mysql.connector as connector

class DBHelper5:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                      port='3306',
                      user='root',
                      password='Shrikant@06',
                      database='Human_Resources_Data')

#vehicle info
    def display_vehicle_info(self,Employe_ID):
        query="select * from employee where Employe_ID='{}'".format(Employe_ID)
        cur=self.con.cursor()
        cur.execute(query)
        print("****Employee information of employee id******")
        for row in cur:
            print("Employe_ID: ", row[0])
            print("First_Name: ", row[1])
            print("Last_Name: ", row[2])
            print("Email: ", row[3])
            print("Phone_No: ", row[4])
            print("Hire_Date ", row[5])
            print("Salary: ", row[6])
            print("Department_ID: ", row[7])
            print("Project_Name: ", row[8])
            print("Role_ID: ", row[9])
            print("DOB: ", row[10])
            print("Address: ", row[11])
            print("Age: ", row[12])
            print()
            print()
 #owner info   
    def display_owner_info(self,Role_ID):
        query="select * from employee where Role_ID='{}'".format(Role_ID)
        cur=self.con.cursor()
        cur.execute(query)
        print("********Roles information of role id********" )
        for row in cur:
            print("Employe_ID: ", row[0])
            print("First_Name: ", row[1])
            print("Last_Name: ", row[2])
            print("Email: ", row[3])
            print("Phone_No: ", row[4])
            print("Hire_Date ", row[5])
            print("Salary: ", row[6])
            print("Department_ID: ", row[7])
            print("Project_Name: ", row[8])
            print("Role_ID: ", row[9])
            print("DOB: ", row[10])
            print("Address: ", row[11])
            print("Age: ", row[12])
            print()
            print()
    def display_role_info(self,Role_ID):
        query="select * from roles where Role_ID='{}'".format(Role_ID)
        cur=self.con.cursor()
        cur.execute(query)
        print("********Roles information of role id********" )
        for row in cur:
            print("Role ID: ", row[0])
            print("Role Name: ", row[1])
            print()
            print()
    def display_project_info(self,Project_No):
        query="select * from projects where Role_ID='{}'".format(Project_No)
        cur=self.con.cursor()
        cur.execute(query)
        print("********project information of project no********" )
        for row in cur:
            print("Project_No: ", row[0])
            print("Project_Name: ", row[1])
            print("Department No.: ", row[2])
            print()
            print()

#main coding
helper=DBHelper5()