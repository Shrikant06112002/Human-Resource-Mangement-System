import sys
from dbhelper import DBHelper
from dbhelper2 import DBHelper2
from dbhelper3 import DBHelper3
from dbhelper4 import DBHelper4
from dbhelper5 import DBHelper5

while True:
    print("*********************Human resource management**************************")
    print("Select the table:")
    print("PRESS 1 for roles")
    print("PRESS 2 for projects")
    print("PRESS 3 for departments")
    print("PRESS 4 for employee")
    print("PRESS 5 for Search")
    print("PRESS 6 for  exit")
    print()
    try:
        choice0=int(input("Enter number: "))
        print()
        if (choice0==1):
            def main():
                db3=DBHelper3()
                while True:
                    print("********roles********")
                    print()
                    print("PRESS 1 to insert new role")
                    print("PRESS 2 to display all roles")
                    print("PRESS 3 to delete role")
                    print("PRESS 4 to update role")
                    print("PRESS 5 to exit program")
                    print()
                    try:
                        choice=int(input("Enter number: "))
                        print()
                        #insert user
                        if(choice==1):
                            Role_ID=input("Enter role id: ")
                            R_title=input("Enter R title: ")
                            db3.insert_roles(Role_ID,R_title)
                            pass
                        elif choice==2:
                        #dtspLay user
                            db3.fetch_all()
                            pass
                        elif choice==3:
                        #deLete user
                            Role_ID=input("Enter Role ID: ")
                            db3.delete_roles(Role_ID)
                            pass
                        elif choice==4:
                        #update user
                            Role_ID=input("Enter Role id: ")
                            R_title=input("Enter R title: ")
                            db3.update_roles(Role_ID,R_title)
                            pass
                        elif choice==5:
                            break
                        else:
                            print("Invalid input ! Try again")
                    except Exception as e:
                        print(e)
                        print("Invalid Details")

            if __name__=="__main__":
                main()
        elif choice0==2:
            def main():
                db2=DBHelper2()
                while True:
                    print("********Projects********")
                    print()
                    print("PRESS 1 to insert new project")
                    print("PRESS 2 to display all projects")
                    print("PRESS 3 to delete project")
                    print("PRESS 4 to update project")
                    print("PRESS 5 to exit program")
                    print()
                    try:
                        choice=int(input("Enter number: "))
                        print()
                        #insert user
                        if(choice==1):
                            Project_No=input("Enter project no: ")
                            Project_Name=input("Enter project name: ")
                            Department_ID=input("Enter department id: ")
                            db2.insert_projects(Project_No,Project_Name,Department_ID)
                            pass
                        elif choice==2:
                        #dtspLay user
                            db2.fetch_all()
                            pass
                        elif choice==3:
                        #deLete user
                            Project_No=input("Enter State district code: ")
                            db2.delete_projects(Project_No)
                            pass
                        elif choice==4:
                        #update user
                            Project_No=input("Enter project no: ")
                            Project_Name=input("Enter project name: ")
                            Department_ID=input("Enter department id: ")
                            db2.update_projects(Project_No,Project_Name,Department_ID)
                            pass
                        elif choice==5:
                            break
                        else:
                            print("Invalid input ! Try again")
                    except Exception as e:
                        print(e)
                        print("Invalid Details")

            if __name__=="__main__":
                main()  
        elif choice0==3:
            def main():
                db=DBHelper()
                while True:
                    print("********Department*******")
                    print()
                    print("PRESS 1 to insert new department")
                    print("PRESS 2 to display all departments")
                    print("PRESS 3 to delete department")
                    print("PRESS 4 to update department")
                    print("PRESS 5 to exit program")
                    print()
                    try:
                        choice=int(input("Enter number: "))
                        print()
                        #insert user
                        if(choice==1):
                            id= input("Enter department ID: ")
                            name= input("Enter department name: ")
                            db.insert_department(id,name)
                            pass
                        elif choice==2:
                        #dtspLay user
                            db.fetch_all()
                            pass
                        elif choice==3:
                        #deLete user
                            Code=input("Enter department ID: ")
                            db.delete_rto(Code)
                            pass
                        elif choice==4:
                        #update user
                            Code=input("Enter department ID: ")
                            newName= input("Enter department name: ")
                            db.update_rto(Code,newName)
                            pass
                        elif choice==5:
                            break
                        else:
                            print("Invalid input ! Try again")
                    except Exception as e:
                        print(e)
                        print("Invalid Details")

            if __name__=="__main__":
                 main() 
        elif choice0==4:
            def main():
                db4=DBHelper4()
                while True:
                    print("********employee********")
                    print()
                    print("PRESS 1 to insert new user")
                    print("PRESS 2 to display all user")
                    print("PRESS 3 to delete user")
                    print("PRESS 4 to update user")
                    print("PRESS 5 to exit program")
                    print()
                    try:
                        choice=int(input("Enter number: "))
                        print()
                        #display vehicle info
                        if(choice==1):
                            Employe_ID=input("Enter employe id: ")
                            First_Name=input("Enter first name: ")
                            Last_Name=input("Enter last name: ")
                            Email=input("Enter email: ")
                            Phone_No=input("Enter phone no: ")
                            Hire_Date=input("Enter hire date: ")
                            Salary=input("Enter salary: ")
                            Department_ID=input("Enter department id: ")
                            Project_Name=input("Enter project name: ")
                            Role_ID=input("Enter role id: ")
                            DOB=input("Enter DOB: ")
                            Address=input("Enter Address: ")
                            Age=input("Enter age: ")
                            db4.insert_employee(Employe_ID,First_Name,Last_Name,Email,Phone_No,Hire_Date,Salary,Department_ID,Project_Name,Role_ID,DOB,Address,Age)
                            pass
                        elif choice==2:
                        #display owner info
                            db4.fetch_all()
                            pass
                        elif choice==3:
                         #deLete user
                            Employe_ID=input("Enter employe ID: ")
                            db4.delete_employee(Employe_ID)
                            pass   
                        elif choice==4:
                        #update user
                            Employe_ID=input("Enter employe id: ")
                            First_Name=input("Enter first name: ")
                            Last_Name=input("Enter last name: ")
                            Email=input("Enter email: ")
                            Phone_No=input("Enter phone no: ")
                            Hire_Date=input("Enter hire date: ")
                            Salary=input("Enter salary: ")
                            Department_ID=input("Enter department id: ")
                            Project_Name=input("Enter project name: ")
                            Role_ID=input("Enter role id: ")
                            DOB=input("Enter DOB: ")
                            Address=input("Enter Address: ")
                            Age=input("Enter age: ")
                            db4.update_employee(Employe_ID,First_Name,Last_Name,Email,Phone_No,Hire_Date,Salary,Department_ID,Project_Name,Role_ID,DOB,Address,Age)
                            pass
                        elif choice==5:
                            break
                        else:
                            print("Invalid input ! Try again")
                    except Exception as e:
                        print(e)
                        print("Invalid Details")

            if __name__=="__main__":
                main() 
        elif choice0==5:
            def main():
                db5=DBHelper5()
                while True:
                    print("***Search***")
                    print()
                    print("PRESS 1 to search employee information on entering employe id")
                    print("PRESS 2 to search all employee on entering role id")
                    print("PRESS 3 to search roles on enter Role ID")
                    print("PRESS 4 to search Project Name and Department Name on entering project id")
                    print("PRESS 5 to exit")
                    print()
                    try:
                        choice=int(input("Enter number: "))
                        print()
                        #display vehicle info
                        if(choice==1):
                            Employe_ID=input("Enter Employe ID: ")
                            db5.display_vehicle_info(Employe_ID)
                            pass
                        elif choice==2:
                        #display owner info
                            Role_ID=input("Enter Role ID: ")
                            db5.display_owner_info(Role_ID)
                            pass
                        elif choice==3:
                        #display owner info
                            Role_ID=input("Enter Role ID: ")
                            db5.display_role_info(Role_ID)
                            pass
                        elif choice==4:
                            break
                        else:
                            print("Invalid input ! Try again")
                    except Exception as e:
                        print(e)
                        print("Invalid Details")

            if __name__=="__main__":
                main()            
        elif choice0==6:
            sys.exit()
        else:
            print("Invalid input ! Try again")
        
    except Exception as e:
        print(e)
        print("Invalid Details")