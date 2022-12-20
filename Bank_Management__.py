
import  mysql.connector  as sqltor
mycon=sqltor.connect(host="localhost", user="root", passwd="1234", database="bank_management")
if mycon.is_connected() :
    print('successfully connected to sql database')
cursor=mycon.cursor()

def insertrecord():
    
    a=int(input("enter customer id"))
    b=input("enter account number")
    c=input("enter account name")
    d=input("enter Joint name")
    e=input("enter address")
    f=input("enter PAN card number of the account holder")
    g=input("enter nominee name if any otherwise type 'NO' ")
    


            
    st="insert into account_details(Customer_ID,Account_Number,Account_Name,Joint_Name,Address,PAN_Number,Nominee_Name) values({},{},'{}','{}','{}',{},'{}')".format(a,b,c,d,e,f,g)
    cursor.execute(st)
    mycon.commit()
    sti="insert into final_amount(Account_Number,Final_Amount) values({},{})".format(b,0)
    cursor.execute(sti)
    mycon.commit()
    print("data you entered is successfully stored")


def display():
    cursor.execute("select * from account_details")
    data=cursor.fetchall()
    count=cursor.rowcount
    print('total no. of accounts',count)
    print("Customer_ID  Account_Number    Account_Name   \t\t Joint_Name\t\tAddress\t\tPAN_Number\tNominee_Name")
    for row in data:
        print(" ")
        for i in row:
            print(i,end='\t\t')
    print(' ')

    

def deleteAccount(x):
    
    flag=searchAccount(x)
    
    if flag==1:
        cursor.execute("delete from final_amount where Account_Number={}".format(x))
        cursor.execute("delete from transactions where Account_Number={}".format(x))
        cursor.execute("delete from account_details where account_details.Account_Number={}".format(x))
        mycon.commit()
        print(" ")
        print("u deleted above mentioned row")
        print("successfully  deleted")




def searchAccount(accno):
    cursor.execute("select * from account_details where Account_Number={}".format(accno))
    data=cursor.fetchall()
    count=cursor.rowcount
    
    if count==1:
        flag=1
        print("Customer_ID  Account_Number    Account_Name   \t\t Joint_Name\t\tAddress\t\tPAN_Number\tNominee_Name")
        for row in data:
            for i in row:
                print(i,end='\t\t')
    
    else:
        flag=0
        print("The details of the entered account number not found. pls check your account number")
    return flag
        
 # searching via account number to get the details of that particular account.

def updateRecords():
    
    aaccnumber=int(input("enter the account number whose details you would like to update"))
    
    flag=searchAccount(aaccnumber)
    if flag==1:
        print(" ")
        field=input("enter the field you want to update from the following list:  (Customer_ID, Account_Name,Joint_Name, Address, Nominee_Name ) :")
        if field=="Customer_ID":
            c=int(input("enter the new value of Customer_ID"))
            st="update account_details set Customer_ID={} where Account_Number={}".format(c,aaccnumber)
            cursor.execute(st)
            mycon.commit()
            print('successfully updated')
        elif field=="Account_Name":
            c=input("enter the new account name")
            st="update account_details set Account_Name='{}' where Account_Number={}".format(c,aaccnumber)
            cursor.execute(st)
            mycon.commit()
            print('successfully updated')
        elif field=="Joint_Name":
            c=input("enter the new joint name")
            st="update account_details set Joint_Name='{}' where Account_Number={}".format(c,aaccnumber)
            cursor.execute(st)
            mycon.commit()
            print('successfully updated')
        elif field=="Address":
            c=input("enter the new address")
            st="update account_details set Address='{}' where Account_Number={}".format(c,aaccnumber)
            cursor.execute(st)
            mycon.commit()
            print('successfully updated')
        else:
            c=input("enter the new Nominee name")
            st="update account_details set Nominee_Name='{}' where Account_Number={}".format(c,aaccnumber)
            cursor.execute(st)
            mycon.commit()
            print('successfully updated')


def transactions():
    transacc=int(input("enter the account number for the transaction"))
    c_d=input("enter credit or debit")
    if c_d=="credit":
        cred=int(input("enter amount you want to credit"))
        cheq=int(input("enter the cheque number"))
        par=input("enter particulars of the transactions")
        cr="select Final_Amount from final_amount where Account_Number={}".format(transacc)
        cursor.execute(cr)
        data=cursor.fetchall()
        amo=int(data[0][0])
        f="insert into transactions(Account_Number,Debit,Credit,Amount,Cheque_Number,Particulars) values({},{},{},{},{},'{}')".format(transacc,0,cred,amo+cred,cheq,par)
        cursor.execute(f)
        mycon.commit()
        up="update final_amount set Final_Amount={} where Account_Number={}".format(amo+cred,transacc)
        cursor.execute(up)
        mycon.commit()
        print("transaction successful")
    else:
        debi=int(input("enter amount you want to debit"))
        cheq=int(input("enter the cheque number"))
        par=input("enter particulars of the transactions")
        de="select Final_Amount from final_amount where Account_Number={}".format(transacc)
        cursor.execute(de)
        data=cursor.fetchall()
        amo=int(data[0][0])
        f="insert into transactions(Account_Number,Debit,Credit,Amount,Cheque_Number,Particulars) values({},{},{},{},{},'{}')".format(transacc,debi,0,amo-debi,cheq,par)
        cursor.execute(f)
        mycon.commit()
        up="update final_amount set Final_Amount={} where Account_Number={}".format(amo-debi,transacc)
        cursor.execute(up)
        mycon.commit()
        print("transaction successful")



def displaytransactions(yac):
    fg="select * from transactions where Account_Number={}".format(yac)
    cursor.execute(fg)
    data=cursor.fetchall()
    count=cursor.rowcount
    print('total no. of transactions',count)
    print("Account_Number \t Debit \t\t Credit \t Balance \t Cheque_Number \t Particulars")
    for row in data:
        print(" ")
        for i in row:
            print(i,end='\t\t')
            
    

def displayingfinal(yac):
    fg="select * from final_amount where Account_Number={}".format(yac)
    data=cursor.execute(fg)
    data=cursor.fetchall()
    print("Account_Number \t Final_Balance")
    for row in data:
        for i in row:
            print(i,end='\t\t')
    

def csvfilelocker():

    import csv

    def insertintocsv():    
        csvfile=open("Locker Details.csv",'a')
        mywriter =csv.writer(csvfile, delimiter =  ',')
        ans ='y'
        while ans.lower()=='y':
            locknum =int(input("Enter Locker Number:"))
            name =input("Enter name of the locker holder:")
            pan =int(input("Enter PAN number of the owner of locker:"))
            locktype=input("Enter locker type Full or Half or Quarter:")
            rent=int(input("Enter rent of the locker"))
            mywriter.writerow([locknum,name,pan,locktype,rent])
            print("## Data Saved... ##")
            ans =input("Add More?...type y for yes")
        csvfile.close()

    def readcsv():    
        f=open("Locker Details.csv",'r')
        csv_reader=csv.reader(f)
        print("Locker_Number	Name_of_Locker_Owner	PAN_Number\tLocker_Type\tRent")
        for row in csv_reader:
            print(" ")
            for i in row:
                print(i,end='\t\t  ')
            
        f.close()


    def searchnum():
        f=open("Locker Details.csv",'r')
        csv_reader=csv.reader(f)
        num=int(input("enter locker number to be searched"))
        print("Locker_Number	Name_of_Locker_Owner	PAN_Number\tLocker_Type\tRent")
        for row in csv_reader:
            if row==[]:
                continue
            elif row[0]==str(num):
                print(" ")
                for i in row:
                    print(i,end='\t\t   ')
                break
        else:
            print("locker number u entered not found")
        f.close()

        
    def deletingrecord():
         f=open("Locker Details.csv",'r')
         csv_reader=csv.reader(f)
         num=int(input("enter locker number whose details u want to delete"))
         lines=[]
         for row in csv_reader:
             if row==[]:
                 continue
             else:
                 lines.append(row)
             
         for row in lines:
             if row[0]==str(num):
                 csvfile=open("Locker Details.csv",'w')
                 mywriter =csv.writer(csvfile, delimiter =  ',')
                 lines.remove(row)
                 for row in lines:
                     mywriter.writerow(row)
                 print("successfully deleted")
                 break
         else:
             print("locker number u entered not found")
         f.close()

    def updatingrecord():
        f=open("Locker Details.csv",'r')
        csv_reader=csv.reader(f)
        num=int(input("enter locker number whose details u want to update"))
        lines=[]
        for row in csv_reader:
            if row==[]:
                continue
            else:
                lines.append(row)
           
        for row in lines:
            if row[0]==str(num):
                new_name =input("Enter name of the new locker holder:")
                new_pan =int(input("Enter PAN number of the new owner of locker:"))
                row.pop(1)
                row.insert(1,new_name)
                row.pop(2)
                row.insert(2,new_pan)
                csvfile=open("Locker Details.csv",'w')
                mywriter =csv.writer(csvfile, delimiter =  ',')
                for row in lines:
                    mywriter.writerow(row)
                print("successfully updated")
                break
        else:
            print("locker number u entered not found")
        f.close()          

    #menudriven
    print("\t")
    print("\t\t\t\t#####Locker Details####")
    while True:
        print("\t")
        print("1.Insert a new record into locker details")
        print("2.To read the details stored about the lockers")
        print("3.To search the details of a particular locker number")
        print("4.To delete a locker detail")
        print("5.To update a record")
        print("6.To go back to main menu")
        print("\t")
        ch=int(input('enter your choice'))
        if ch==1:
            insertintocsv()
        elif ch==2:
            readcsv()
        elif ch==3:
            searchnum()
        elif ch==4:
            deletingrecord()
        elif ch==5:
            updatingrecord()
        elif ch==6:
            break
        else:
            print("invalid choice")
    
        

def employee():
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


    
    
    
#main menu driven program

print("\t")
print("\t\t\t\t\t##### Welcome to my application #####")
try:
    while True:
        
        print("\t")
        print("\t\t\t\t1.To enter the details of newly created account")
        print("\t\t\t\t2.To display all the accounts")
        print("\t\t\t\t3.To delete an account")
        print("\t\t\t\t4.To search details of a particular account via account number")
        print("\t\t\t\t5.To update details of a particular account")
        print("\t\t\t\t6.To credit or debit from your account")
        print("\t\t\t\t7.To display contents of passbook")
        print("\t\t\t\t8.To display only the final amount in your account")
        print("\t\t\t\t9.To access the file of locker details")
        print("\t\t\t\t10.To access the file of employee details")
        print("\t\t\t\t11.Exit the program")
        print("\t")
        ch=int(input('enter your choice'))
        if ch==1:
            insertrecord()
        elif ch==2:
            display()
        elif ch==3:
            delac=int(input("enter the account number of the account which you want to delete"))
            deleteAccount(delac)
        elif ch==4:
            searac=int(input("enter the account number of the account which you want to search"))
            searchAccount(searac)
        elif ch==5:
            updateRecords()
        elif ch==6:
            transactions()
        elif ch==7:
            u=int(input("enter the account number"))
            displaytransactions(u)
        elif ch==8:
            t=int(input("enter the account number"))
            displayingfinal(t)
        elif ch==9:
            csvfilelocker()
        elif ch==10:
            employee()
        elif ch==11:
            print("Exiting the program......Thank you so much for banking")
            break
        else:
            print("Invalid Choice")
except:
    pass






