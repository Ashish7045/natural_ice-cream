import random

import time

import mysql.connector

import mail


connect = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="",
    #database="natural_icecreame"
    )

cursor=connect.cursor()

cursor.execute("create database if not exists natural_icecreame") 
'''
cursor=connect.cursor()


cursor.execute("show tables like 'Employee' ")

result=cursor.fetchone()

if result :

    print("table exists ")

else :

    print("table should be created")

'''
print("welcome to natural ice creame")

print("press 1 FOR TO ADD NEW EMPLOYEE")

print("press 2 FOR LOGIN ")


a=int(input("press number :"))

if a==1:

   try:
       #create database:

       #cursor.execute("create database natural_icecreame")

       #create table:

       #cursor.execute("create table if not exists Employee(emp_id int(20)NOT NULL,Full_Name varchar(30),Mobile_no int (10),Email_id varchar(30),Address varchar (30),PRIMARY KEY(emp_id))")
       
       
       print("pelase enter employee details carefully")

 
       name=input("enter youe full name :") 
       mobile_no=input("enter your mobile number:")
       email_id=input("enter your email_id:")
       address=input("enter your address:")

       cursor=connect.cursor()

       sql="insert into employee (emp_id,Full_name,Mobile_no,Email_id,Address) values (%s,%s,%s,%s,%s)"

       value=["",name,mobile_no,email_id,address]

       cursor.execute(sql,value)

       connect.commit()

       print(cursor.rowcount," row inserted successfully")
   
   except:
       #print("yoyo")
       
       connect.rollback()
    
   connect.close()
    
if a==2:
    
    print("login:")
    
    print("fill your correct email_id and mobile number :")

    emp_email_id=input("enter your email_id: ")

    emp_mobile_no=input("enter mobile number: ")
    
    try:
       
       # Reading the employee data :
       
        cursor.execute("""select Mobile_no, Email_id from employee where Mobile_no =%s and Email_id =%s """,(emp_mobile_no,emp_email_id))


        #print("employee data found")

        #fetching the  first row form the cursor object :
        
        result=cursor.fetchone()

        if result:

           print("OTP has been successfully send to your registered Email_id ")

           start_time=time.time()
           

           otp=random.randrange(1000,10000)
###           

           mail.mail(emp_email_id,str(otp))
###

           #print("your otp is ",otp)

           num=int(input("Your OTP is  :"))

           end_time=time.time()


           result_time=format(end_time-start_time)


           if float(result_time)>=60:

              print("otp session expired")
   
           elif num==otp:
    
              print("OTP verified successfully")
     
           else :
              print("otp does not matched try again ")
      #else :
          #print("no  Employee data found!!!")

        #print(result)
        
    except:

        print("no such employee data found!!!")

    connect.close()
        
'''  
   
      for x in range(1,4):

          a=int(input("enter otp:"))

          if a==otp:

              print("mobile number  verified successfully")

              break

          else:

                print("wrong otp,going for sleep")

                for z in range(1,6):

                    print(z,end=' ')

                    time.sleep(1)
                
'''    

