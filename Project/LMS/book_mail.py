""" import subprocess
serial = subprocess.check_output('wmic bios get serialnumber').decode("utf-8").replace('SerialNumber','').strip() 

import smtplib as smtp
from datetime import datetime
connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'akharche45@gmail.com'
email_passwd = 'hdkf ucnk ppzu thqw'
connection.login(email_addr, email_passwd)

receiver='muskanmalhotra2910.com'
mail_body="I develop app to send mails for library management system"
dt_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
subject = f'my app {dt_time} @{serial}'

from email.mime.multipart import MIMEMultipart
msg = MIMEMultipart()
msg['From'] = email_addr
msg['To'] = receiver
msg['Subject'] = subject
connection.sendmail(email_addr, receiver, msg.as_string())
connection.close() """

import smtplib as smtp


connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'akharche45@gmail.com'
email_passwd = 'hdkf ucnk ppzu thqw'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='kannushikha15@gmail.com', msg="Sent from Aishwarya. Hehe")
connection.close()
print('Mail sent successfully')