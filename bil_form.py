import mysql.connector

from fpdf import FPDF

from datetime import datetime

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#connect = mysql.connector.connect(
     #host="localhost", 
     #user="root",
     #password="",
     #database="natural_icecreame"
     #)


#cursor=connect.cursor()

def bill():

     now=datetime.now()

     dt_string=now.strftime("%d /%m /%y ")
     
     #cursor.execute("create table  bill(id int(5) not null,flavor varchar(30),quantity int(5),cup_corn int(5),price int(10),gst decimal(10),total decimal(10),cust_email_id varchar(30),cust_number varchar(10),PRIMARY KEY(id))")

     #cursor.execute("create table if not exists bill(id int(5) not null,flavor varchar(30),quantity int(5),cup_corn int(5),price int(10),gst decimal(10),total decimal(10),cust_email_id varchar(30),cust_number varchar(10),PRIMARY KEY(id))")
     print("Natural_ice-cream bill form : \n")

     print("which ice-cream flavour :")
    

     icecream=['Vanilla' ,'Matcha', 'Chocolate' ,'Coconut', 'Strawberry', 'Banana' ,'Mango', 'Oreo' ]

     icecream_price=[200,230,100,150,300,160,280,350]

     for x in range (len(icecream)):

          print(x+1," ",icecream[x],"        Rs :",icecream_price[x] )

     b=int(input("enter number :"))-1

     price=0

     for y in range (len(icecream_price)):
          

          if y==b:

               price=icecream_price[y]

     print(price)

     flavor=icecream[b]

     print(flavor)

     print(" which type of icecream do you want ? \n")

     print("press 1 for CUP :")

     print("press 2 for CONE:")

     c=int(input(" "))

     #c=0

     if c==1:

         c=5
         
         #price_c=price+c

          #print(price)

     elif c==2:

         c=10

        # price_c=price+c
          
          #print(price)

     else:

         print("invalid option selected")
         
     q=int(input(" icecream quantity:"))
     
     
     print("----------------------- natural_icecream_bill-------------------------")


     email=""
     mobile=""

     z=1
     
     while  z==1:
          print("press 1 for customer info \n")

          print("press 2 for customer is not intrested")


          e=int(input(""))


          if e==1:

               #z=z+1
               
               email=input("enter customer mail_id : ")

               mobile=input("enter customer mobile_number :")

               break
          
          elif  e==2:
               
               #z=z+1
               
               #pass
               break

          else:
               #z==1
               #e=e+1

               print("invalid option selected")

               
     print("customer  email_id is : ",email)

     print("customer mobile_number is: ",mobile)

     print("ICE_CREAM PRICE :",price)
    
     gst=(price*q+c)*0.1

     print("GST 10% AS PER YOUR ICE-CREAM :",gst)

     total_price=(price*q)+gst+c

     print(" TOTAL PRICE :",total_price)

     print("press 1 for bill paid :")

     print("press 2 for order cancel:")

     x=int(input(""))

     connect = mysql.connector.connect(
             host="localhost", 
             user="root",
             password="",
             database="natural_icecreame"
              )
     cursor=connect.cursor()

     if x ==1:

          #try:
               
               print("insert bill data table")
            
             
               sql="insert into bill (id,flavor,quantity,cup_corn,price,gst,total,cust_email_id,cust_number)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

               value=["",flavor,q,c,price,gst,total_price,email,mobile]

               cursor.execute(sql,value)

               connect.commit()

               print(cursor.rowcount,"row inserted successfully")

               # pdf work started:

               
               document=FPDF()
           
               document.add_page()

               #NATURAL_ICE_CREAM
               
               document.set_font("Arial",size=20)
               document.cell(200,10,'NATURAL ICE-CREAME',0,1,'C')

               #PHONE NUMBER

               document.set_font("Arial",size=10)
               document.cell(200,10,'ph: 1234567890,7045767397',0,1,'C')

               
               document.set_font("Arial",size=10)
               document.cell(200,10,'------------------------------------------------------------TAX Invoice---------------------------------------------',0,1,'C')

               #DATE

               document.set_font("Arial",size=10)
               document.cell(130,5,'Date:',0,0,'C')
               document.cell(1,7,str(dt_string),0,1,'R')

               #BILL NUMBER

               

               #bill_number()

               document.set_font("Arial",size=10)
               document.cell(130,5,'Bill No:',0,0,'C')
               document.cell(1,7,str(bill_number()),0,1,'R')
          
               document.set_font("Arial",size=10)
               document.cell(200,3,'----------------------------------------------------------------------------------------------------------------------------',0,1,'C')

               #FLAVOR
             
              
               document.set_font("Arial",size=10)
               document.cell(130,7,'flavor  :',0,0,'C')
               document.cell(10,7,str(flavor),0,1,'C')

               #QUANTITY

               document.set_font("Arial",size=10)
               document.cell(130,7,'quantity :',0,0,'C')
               document.cell(160,7,str(q),0,1)

               #CUP_CORN

               document.set_font("Arial",size=10)
               document.cell(130,7,'cup_corn :',0,0,'C')
               document.cell(160,7,str(c),0,1)

               #PRICE

               document.set_font("Arial",size=10)
               document.cell(130,7,'price :',0,0,'C')
               document.cell(160,7,str(price),0,1)

               #GST
               
               document.set_font("Arial",size=10)
               document.cell(130,7,'gst :',0,0,'C')
               document.cell(160,7,str(gst),0,1)

               
               document.set_font("Arial",size=10)
               document.cell(200,5,'----------------------------------------------------------------------------------------------------------------------------',0,1,'C')

               #TOTAL_PRICE

                
               document.set_font("Arial",size=10)
               document.cell(130,7,'total :',0,0,'C')
               document.cell(160,7,str(total_price),0,1)

               #THANK YOU

               document.set_font("Arial",size=15)
               document.cell(200,20,'Thank You... :',0,1,'C')
           

               document.output("codework.pdf",'F')
               #document=FPDF(orientation='P',unit='mm',format='A4')

               print("pdf created")

               mail_pdf(email)
          #except:

            #connect.rollback()
     else:

        print("thank you for visiting our ice cream shop")

        connect.close()


def bill_number ():


     connect = mysql.connector.connect(
             host="localhost", 
             user="root",
             password="",
             database="natural_icecreame"
              )
     cursor=connect.cursor()


     cursor.execute("select id from bill order by id desc limit 1")
    
     result=cursor.fetchone()

     id =0

     for i in result:

          id=i

     return id


     return result()

def mail_pdf(to_mail):

    print(to_mail)

    subject = "NATURAL ICE-CREAM INVOICE"
    body = "INVOICE"
    sender_email = "ashishkadam2898@gmail.com"
 
    receiver_email ="ashwiniwagh690@gmail.com"
    password = input("Type your password and press enter:")

# Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "codework.pdf"  # In same directory as script

# Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

# Add header as key/value pair to attachment part
    part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
    )

# Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

# Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

        server.quit()


bill()








     





















     
            
