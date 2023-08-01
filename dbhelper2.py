import mysql.connector as connector

class DBHelper2:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                      port='3306',
                      user='root',
                      password='Shrikant@06',
                      database='Human_Resources_Data')

#Insert
    def insert_projects(self,Project_No,Project_Name,Department_ID):
        query="insert into projects(Project_No,Project_Name,Department_ID) values({},'{}','{}')".format(Project_No,Project_Name,Department_ID)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("saved to database")
    
#Fech all
    def fetch_all(self):
        query="select * from projects"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Project no: ", row[0])
            print("Project name: ", row[1])
            print("Department id: ", row[2])
            print()
            print()

#delete user
    def delete_projects(self,Project_No):
        query="delete from projects where Project_No='{}'".format(Project_No)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

#update
    def update_projects(self,Project_No,Project_Name,Department_ID):
        query="update projects set Project_Name='{}',Department_ID='{}' where Project_No='{}'".format(Project_Name,Department_ID,Project_No)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")
#main coding
helper=DBHelper2()