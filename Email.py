import json
import smtplib
import os
from os.path import basename
from string import Template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

email_address = 'replay10540@gmail.com'
email_password = '0875507608' 


# send_email(data)


def sentMail(message):
    try:
        sending_ts = datetime.now()
        sub = "New Smartphones Siamphone %s" % sending_ts.strftime('%Y-%m-%d %H:%M:%S')
        msg = MIMEMultipart('alternative')
        msg['From'] = email_address
        msg['To'] = email_address
        msg['Subject'] = sub
        
        data = ""
        for item in message:
            data = data + format("<tr><td>"+item["brandname"]+"</td><td>"+item["name"]+"</td><td>"+item["price"]+"</td>"
            "<td>"+item["newprice"]+"</td>""<td>"+item["datetime"]+"</td>""<td><a href="+item["link"]+">ดูข้อมูล</a></td></tr>")
        html = """\
        <html>
          <head>
          <style>body{
            font:1.2em normal Arial,sans-serif;
            color:#34495E;
            }

            h1{
            text-align:center;
            text-transform:uppercase;
            letter-spacing:-2px;
            font-size:2.5em;
            margin:20px 0;
            }

            .container{
            width:90%;
            margin:auto;
            }

            table{
            border-collapse:collapse;
            width:100%;
            }

            .blue{
            border:2px solid #1ABC9C;
            }

            .blue thead{
            background:#1ABC9C;
            }

            .purple{
            border:2px solid #9B59B6;
            }

            .purple thead{
            background:#9B59B6;
            }

            thead{
            color:white;
            }

            th,td{
            text-align:center;
            padding:5px 0;
            }

            tbody tr:nth-child(even){
            background:#ECF0F1;
            }

            tbody tr:hover{
            background:#BDC3C7;
            color:#FFFFFF;
            }

            .fixed{
            top:0;
            position:fixed;
            width:auto;
            display:none;
            border:none;
            }

            .scrollMore{
            margin-top:600px;
            }

            .up{
            cursor:pointer;
            }</style>
          </head>
          <body>
           <h1>&darr; NEWITEM &darr;</h1>
            <table class="blue">
            <thead>
                <tr>
                <th>Brand</th>
                <th>NamePhone</th>
                <th>price</th>
                <th>newprice</th>
                <th>date</th>
                <th>image</th>
                </tr>
            </thead>
            <tbody>
               """+data+"""
            </tbody>
            </table>
          </body>
        </html>
        """
        print(html)
        #msg.attach(MIMEText(body,'plain'))
        msg.attach(MIMEText(html, 'html'))

        

        # attachment = MIMEText(json.dumps(data))
        # attachment.add_header('Content-Disposition', 'attachment', 
        #                     filename="data_file.json")
        # msg.attach(attachment)
        

        # print(msg)
        # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # server.ehlo()
        # server.login(email_address, email_password)
        # # server.sendmail(email_address, email_address, "msg")
        # server.send_message(msg)
        # server.close()

        print ('Email sent!')
    except ValueError:
        print ('Something went wrong...')
        print (ValueError)



