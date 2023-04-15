import pandas as pd
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl
sender_email="happybirthdaytmessage@gmail.com"
password="fndxbxxbpwuluxnp"
a=pd.read_excel("birth.xlsx")
d=a['Birth-Date']
day=str(date.today().day)
print(day)
month=str(date.today().month)
print(month)
if len(day)==1:
    day=str("0"+day)
if len(month)==1:
    month=str("0"+month)
print(month)
dates=f"{month}!{day}"
print (dates)
i=0

result=[]
for values in d:
    print(values)
    if values==dates:
         result.append(i)
    i=i+1
if len(result) !=0:
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(sender_email, password)
            for value in result:
                m = MIMEMultipart('alternative')
                m1 = MIMEMultipart('alternative')

                row=a.iloc[value]
                name=row['Name']
                sendto=row['Email-1']
                msg=row['Message']
                sendcnf=row['Email-2']
                html = f"""\
                           <html>
                             <head></head>
                             <body>
                              
                              <h1 style="color: #C3447A"><strong>{msg}</strong></h1>
                              <br>from:- {sendcnf}<br><br><br>
                              <p  style="color: #D2386C">  <b> And also happy Birthday From Our Side We WisH You a Great Future </b> </p>
        
                              <p style="color: #FDAC53"><br><br><br><br><br><br><br> Developed with lots of ❤️and ☕ by jayeshdarda9@gmsil.com</p>
                             </body>
                           </html>
                           """
                html1=f"""\
                           <html>
                             <head></head>
                             <body>
                              
                              <h1 style="color: #C3447A"><strong>Today was {name} Birthday we Sent Him Your Message</strong></h1>
                              
        
                              <p style="color: #FDAC53"><br><br><br><br><br><br><br> For Feedback and Suggestions Please mail at: jayeshdarda9@gmail.com</p>
                             </body>
                           </html>
                           """
                part1 = MIMEText(html, 'html')
                m.attach(part1)
                part11 = MIMEText(html1, 'html')
                m1.attach(part11)

                m['Subject'] = f'Happy Birthday {name}'
                m['From'] = "happybirthday"
                m['To'] = sendto
                m1['Subject'] = f'Happy Birthday Message was sent to  {name}'
                m1['From'] = "happybirthdaytmessage@gmail.com"
                m1['To'] = sendcnf
                server.sendmail(sender_email, sendto, m.as_string())
                server.sendmail(sender_email, sendcnf, m1.as_string())


            print("done for the day")
    except Exception as e:
        print(e)
        server.sendmail(sender_email, 'jayeshdarda9@gmail.com', e)


else:
    print("sorry No birthday Today")

