from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
print('''####################################################
#==========>WELCOME TO BULK EMAIL SENDER<==========#
####################################################''')
input1=int(input("Enter the number of emails:"))
emails=[]
for z in range(1,input1+1):
    input2=input("Enter email here:")
    emails.append(input2)
sender_name=input("Enter the name from which the email has to be sent:")
subject=input("Enter the subject:")
print("<========LOGIN CREDENTIALS========>")
email_id=input("Enter the email ID from which the email has to be sent:")
password=input("Enter password here:")
for i in emails:
    message= MIMEMultipart()
    message["from"] = sender_name
    message["to"] = i
    message["subject"] = subject

    with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email_id,password)
        smtp.send_message(message)
        print("Email sent Successfully to",i)