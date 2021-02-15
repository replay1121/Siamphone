import json
import smtplib
import os

from string import Template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

email_address = 'replay10540@gmail.com'
email_password = '0875507608' 

data = {"my": "foo", "yours": "bar"}
# send_email(data)
def sentMail():
    try:
        sending_ts = datetime.now()
        sub = "หัวข้อไง %s" % sending_ts.strftime('%Y-%m-%d %H:%M:%S')
        msg = MIMEMultipart('alternative')
        msg['From'] = email_address
        msg['To'] = email_address
        msg['Subject'] = sub

        body = "ส่งได้แล้วววว"
        msg.attach(MIMEText(body, 'plain'))

        attachment = MIMEText(json.dumps(data))
        attachment.add_header('Content-Disposition', 'attachment', 
                            filename="data_file.json")
        msg.attach(attachment)

        # print(msg)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(email_address, email_password)
        # server.sendmail(email_address, email_address, "msg")
        server.send_message(msg)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')

sentMail()
