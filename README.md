# Bank_Management_System
The Banking Management System is an application for maintaining a person’s account in a bank. The system provides the access to the customer to create an account, deposit/withdraw the cash and other core banking features from his account. It also enables customer to view reports of all accounts present.  
 
Project Modules:  

1)Registration: A customer can create an account in the bank by providing important information such as personal details.

2)Core Operations: This module enables Deposit or withdraw functionality to the customer. User can also check the balance. 

3)Reports: This module will generate different kind of statements and can be used for checking balance. 

4)Profile Management: User can update his details like contact information etc. 

5)Locker information: This will help to maintain locker details of the bank. 

6)Employee details: This will help to maintain employee details of the bank. 

Software to be used:  
  ->Python 3.x installation<br>
  ->Microsoft Excel for CSV<br>
  ->MySQL for storing information<br>

Technical Stack: 

Front-End <br>
  -IDLE Python <br>

Back-End <br>
  -MySQL as database <br>
  -CSV file <br>
  
  
  Before executing the code, creation of database and tables  has to be done at the backend (MySQL, CSV).
  Following is the code written in MySQL Command Line Client:
  
  create  database bank_management; 

#database created 

use bank_management; 

#database selected <br><br>
#Table 1 

create table account_details 

(Customer_ID integer unique, 

Acconut_Number integer primary key, 

Account_Name varchar(50) not null, 

Joint_Name varchar(50), 

Address varchar(50), 

PAN_Number  integer, 

Nominee_Name varchar(50) default  ‘NO’); 
<br><br>
#Table 2 

create table transactions 

(Account_Number  integer, 

Debit  integer, 

Credit integer, 

Amount integer, 

Cheque_Number integer, 

Particulars char(50), 

Foreign Key (Account_Number) references  account_details(Account_Number)); 
<br><br>
#Table 3 

create table final_amount 

(Account_Number  integer, 

Final_Amount integer , 

Foreign Key (Account_Number) references  account_details(Account_Number)); 
<br>
<br>
#Table 4 

create table empl 

(empno int primary key, 

ename varchar(30), 

post varchar(20), 

city varchar(20), 

salary int); 

Create an empty excel file with extension “.csv”  named Locker Details.
