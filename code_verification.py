# ██╗██╗  ██╗██╗        ███████╗██╗      ██████╗ ██╗    ██╗███████╗██████╗ 
# ██║╚██╗██╔╝██║        ██╔════╝██║     ██╔═══██╗██║    ██║██╔════╝██╔══██╗
# ██║ ╚███╔╝ ██║        █████╗  ██║     ██║   ██║██║ █╗ ██║█████╗  ██████╔╝
# ██║ ██╔██╗ ██║        ██╔══╝  ██║     ██║   ██║██║███╗██║██╔══╝  ██╔══██╗
# ██║██╔╝ ██╗██║███████╗██║     ███████╗╚██████╔╝╚███╔███╔╝███████╗██║  ██║



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import csv
import random

def main(name, email):
    message = f"Hello <b style='color: rgb(15, 245, 84);'>{name}</b> and welcome to my website.\n\n {random_code}"
    return name, email, message

def send_email(subject, message, from_addr, to_addr):
    msg = MIMEMultipart('alternative')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    body_text = MIMEText(message, 'plain')

    html_message = f"""
    <html>
    <head>
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Vazirmatn&display=swap');
        body {{
            text-align: center;
            font-family: 'Vazirmatn', sans-serif;
            font-size: 20px;
        }}
        .container {{
            width: 50%;
            height: auto;
            background-color: rgba(36, 35, 54, 0.918);
            padding: 20px;
            border-radius: 20px;
            margin: auto;
            text-align: center;
            margin-top: 150px;
            margin-bottom: 1000px;
            box-shadow: 10px 20px 30px gray;
        }}
        </style>
    </head>
    <body>
        <div class="container">
            <p style="font-size: 20px;color: rgb(255, 140, 249);">{message.replace(str(random_code), '')}</p>
            <p style="font-size: 32px; font-weight: bold;color: rgb(51, 253, 243);">{random_code}</p>
            <p style="font-size: 20px;color: rgb(255, 140, 249);">from the ixi_flower</p>
        </div>
    </body>
    </html>
    """
    body_html = MIMEText(html_message, 'html')

    msg.attach(body_text)
    msg.attach(body_html)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, '<app password which is from your gmail>')
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()

random_code = random.randint(1000000, 9999999)

get_name = input("What is your name: ")
get_email = input("Enter your email address (e.x:example@gmail.com): ")

name, email, message = main(get_name, get_email)

with open('user_emails.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow([get_name, get_email])

subject = "Verify Your Email"
send_email(subject, message, '<enter you email here>', get_email)

print("Please enter the verification code you received via email.")
get_code = int(input())
if (get_code == random_code):
    print("\nwelcome")
else:
    print("\nnop not correct")
