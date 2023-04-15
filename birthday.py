import datetime
import ssl
import time

from openpyxl import workbook,load_workbook

import  streamlit as st
import random as r
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sender_email="happybirthdaytmessage@gmail.com"
password="fndxbxxbpwuluxnp"
if "button_clicked" not in st.session_state:
    st.session_state.disable=False
    st.session_state.disable1 = True
    st.session_state.otp=""
    st.session_state.otp1=""
    st.session_state.button_clicked=False

if "verify Email" not in st.session_state:
    st.session_state["verify Email"] = False
if "button2" not in st.session_state:
    st.session_state["button2"] = False
if "button3" not in st.session_state:
    st.session_state["button3"] = False
def callback():
    st.session_state.button_clicked=True



def verify():

        p.success("Please wait Processing")
        a1 = "@" in email2
        a2 = email2.endswith(".com")
        if a1 == False or a2 == False:
            p.warning(f"{email2} doesn't seems like a Genuine Email please complete the required email")
            return
        p.success("Please wait Processing")
        st.session_state.otp = ""
        m = MIMEMultipart('alternative')
        for i in range(5):
            st.session_state.otp += str(r.randint(1, 9))
        print(st.session_state.otp)
        html = f"""\
            <html>
              <head></head>
              <body>
               <p>The Otp To Confirm  <b> {name.upper()}</b> Data is :</p>
               <h1 style="color: #FF6F61"><strong>{st.session_state.otp}</strong></h1>

               <p><br><br><br><br><br><br><br> Developed with lots of ❤️and ☕ by jayeshdarda9@gmsil.com</p>
              </body>
            </html>
            """
        part1 = MIMEText(html, 'html')

        m.attach(part1)

        m['Subject'] = 'Otp Verfication For Birthday Wisher Ver 1.0.0'
        m['From'] = "happybirthdaytmessage@gmail.com"
        m['To'] = email2

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, email2, m.as_string())
        except Exception as e:
            print(e)
            server.sendmail(sender_email, 'jayeshdarda9@gmail.com', e)
st.title("Happy Birthday Wisher ver 1.0.0")
name=st.text_input("Please Enter the name of Person whom you want to wish !",key="birth",help="please enter the name of the person whose birthday is now")
email1=st.text_input(f"Please enter the Email-address of {name}",key="emailbirth",help="please enter the email-address of the person whom you want to message")
date1=st.date_input(f"Please select the Birthdate of {name}",datetime.date(2002,10  ,10),key="birthday",help="Please select the current date year doesn't Meatter !")
msg=st.text_area(f"Please enter your Customized Message for {name}",help=f"the message you entered here will be sent to {email1} on their Birthday")

email2=st.text_input("please enter your email address",help="your Email will be Verified and it will be sent an email as a reminder for {name} birthday and for confirmation that email has been sent")
st.checkbox("I AGREE TO RECIEVE EMAILS FROM BIRTHDAY SERVICE (no promotions)",key="disable")
p=st.empty()
p.write(f"\n ")
col1,col2,col3=st.columns(3)
with col1:
    c1=st.empty()

with col2:
    c2=st.empty()
with col3:
    c3=st.empty()






if c2.button('verify Email',disabled=not st.session_state.disable,on_click=callback):
    st.session_state["verify Email"] = not st.session_state["verify Email"]
    verify()

if st.session_state["verify Email"] and not st.session_state['button2']:
    c2.empty()
    p.success("OTP sent Successfully Please check Your Email")
    if c1.button('Resend otp ', key="fsgsgsgs"):
        verify()
        c2.empty()
        p.success("OTP sent Successfully Please check Your Email")
    otp1 = c2.text_input("Enter Otp here 👇", key="con")
    if c3.button("Verify Otp"):
        print("working verify")

        print(otp1)
        st.session_state.otp = st.session_state.otp.replace(" ", "")
        otp1 = otp1.replace(" ", "")
        if st.session_state.otp==otp1:
            p.success("email SuccesFully verified!")
            c1.empty()
            c2.empty()
            c3.empty()
            st.session_state["button2"] = not st.session_state["button2"]

        else:
            p.error("Sorry! Wrong Otp!,Please Click on Resend Otp to Try again!")

if st.session_state["verify Email"] and st.session_state["button2"]:
    if c2.button("Save Data"):
           while True:
                try:
                    a = "@" in email1
                    a1 = "@" in email2
                    a2 = email1.endswith(".com")
                    print(a)
                    print(a1)
                    if name == "":
                        p.warning("name of the person cannot be empty!")
                        c1.empty()
                        c3.empty()
                        break

                    if msg == "":
                        p.warning("message cannot be empty please conplete it!")
                        c1.empty()
                        c3.empty()
                        break

                    if a == False or a2 == False:
                        p.warning(f"{email1} doesn't Seems like a Genuine Email please complete the required email")
                        c1.empty()
                        c3.empty()
                        break

                    if a1 == False:
                        p.warning(f"{email2} doesn't seems like a Genuine Email please complete the required email")
                        c1.empty()
                        c3.empty()
                        break

                    date2 = str(date1)[5:]
                    print(date2)
                    date = date2.replace("-", "!")


                    wb = load_workbook('birth.xlsx')
                    ws = wb.active
                    data1 = [name, email1, date, msg, email2]
                    ws.append(data1)
                    wb.save('birth.xlsx')
                    p.success(f"THanks! For using our service {name} details have been added successfully!")

                    st.balloons()
                    c1.empty()
                    c2.button("Please Reload The page to use Again",disabled=st.session_state.disable1)
                    c3.empty()
                    time.sleep(60)
                    break
                except:
                    c1.empty()
                    c3.empty()
                    pass
                    break
