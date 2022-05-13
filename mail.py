#Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail

import smtplib

#create function take 2 args

def mail(to_mail,otp_msg):  
   
    
#creating smtp session :

   s=smtplib.SMTP('smtp.gmail.com',587)

#start tls for security:
#Transport Layer Security (TLS)
#TLS is a protocol that encrypts and delivers mail securely,

   s.starttls()

#authentication

   s.login('ashishkadam2898@gmail.com','ashishanita')  #mail_id and password
   #s.login('','')

#msg to be send


   msg="your otp is "+otp_msg



#sending mail :

   s.sendmail('ashishkadam2898@gmail.com',to_mail,msg)
  

#terminating session :

   s.quit()
