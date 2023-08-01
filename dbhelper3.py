import mysql.connector as connector

class DBHelper3:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                      port='3306',
                      user='root',
                      password='Shrikant@06',
                      database='Human_Resources_Data')

#Insert
    def insert_roles(self,Role_ID,R_title):
        query="insert into roles(Role_ID,R_title) values('{}','{}')".format(Role_ID,R_title)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("saved to database")
    
#Fech all
    def fetch_all(self):
        query="select * from roles"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Role ID: ", row[0])
            print("R_title: ", row[1])
            print()
            print()

#delete user
    def delete_roles(self,Role_ID):
        query="delete from roles where Role_ID='{}'".format(Role_ID)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

#update
    def update_roles(self,Role_ID,R_title):
        query="update roles set R_title='{}' where Role_ID='{}'".format(R_title,Role_ID)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")
#main coding
helper=DBHelper3()