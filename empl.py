import mysql.connector as sqltor
mycon= sqltor.connect(host="localhost", user="root", passwd="1234", database="bank_management")
cursor=mycon.cursor()
if mycon.is_connected():
    print('')

def insertrecord():
    n=int(input("Enter Employee id:"))
    c=input("Enter Employee Name:")
    d=input("Enter Employee post:")
    p=input("Enter Employee city's Name:")
    y=int(input("Enter Employee salary:"))
    sql="insert into empl values({},'{}','{}','{}',{})".format(n,c,d,p,y)
    cursor=mycon.cursor()
    cursor.execute(sql)
    mycon.commit()
    print("\n       *************Data Entered successfully***********")
    

def displayrecord():
    sql="select * from empl"
    cursor=mycon.cursor()
    cursor.execute(sql)
    d=cursor.fetchall()
    for i in d:
        print(i)
    



def deleterecord():
    cursor=mycon.cursor()
    s=int(input("Enter the empno which u have to delete:"))
    flag=searchrecord(s)
    if flag==1:
        
        sql="Delete from empl where empno='{}'".format(s)
        cursor.execute(sql)
        mycon.commit()
        print("\n          **********Deleted successfully***********")
    


    
def searchrecord(empno):
    cursor=mycon.cursor()
    cursor.execute("select * from empl where empno={}".format(empno))
    d=cursor.fetchall()
    count=cursor.rowcount

    if count==1:
        flag=1
        print("empno  ename  post  city  salary")
        for row in d:
            for i in row:
                print(i,end="  ")
        mycon.commit()
    else:
        flag=0
        print("Employee id u entered not found")
    
    return flag
        

def updaterecord():
    empno= int(input('Enter the employee number whose details you would like to update:'))
    flag=searchrecord(empno)
    
    if flag==1:
        print(' Modify screen ')
        print('\n 1.  Employee Name')
        print(' 2.  Employee post')
        print(' 3.  Employee city')
        print(' 4.  Employee salary')
        choice = int(input(' What do you want to change '))
        new_data  = input('Enter New value :')
        field_name=''
        if choice == 1:
            field_name ='ename'
        if choice == 2:
            field_name = 'post'
        if choice == 3:
            field_name = 'city'
        if choice == 4:
            field_name = 'salary'
        sql ='update empl set ' + field_name + '="'+ new_data +'" where empno='+str(empno)+';' 
        cursor.execute(sql)
        print('\n   **************Employee Information modified..***********')
        
        

           
while True:
    print("""
        ------------EMPLOYEE MANAGING SYSTEM------------
                   1. Add New Employee Details
                   2. Display Employee Details
                   3. Search Employee Details
                   4. To delete Employee Account
                   5. Update details of particular Employee
                   6. Exit """)
    choice= int(input("Enter your choice:"))
    
    if(choice == 1):
        insertrecord()
    elif(choice == 2):
        displayrecord()
    elif(choice == 3):
        empn= int(input("Enter the empno which u have to search:"))
        searchrecord(empn)
    elif(choice== 4):
        deleterecord()
    elif(choice== 5):
        updaterecord()
    elif(choice== 6):
        break
    else:
        print("Wrong choice.......")

