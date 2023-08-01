import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                      port='3306',
                      user='root',
                      password='Shrikant@06',
                      database='Human_Resources_Data')

#Insert
    def insert_department(self,Department_ID,Department_Name):
        query="insert into departments(Department_ID,Department_Name) values('{}','{}')".format(Department_ID,Department_Name)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("saved to database")
    
#Fech all
    def fetch_all(self):
        query="select * from departments"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Department ID :", row[0])
            print("Department name:", row[1])
            print()
            print()

#delete user
    def delete_department(self,Department_ID):
        query="delete from departments where Department_ID='{}'".format(Department_ID)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

#update
    def update_department(self,Department_ID,Department_Name):
        query="update departments set Department_Name='{}' where Department_ID='{}'".format(Department_ID,Department_Name)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")
#main coding
helper=DBHelper()

