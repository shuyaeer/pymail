import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

GMAIL = os.environ.get('GMAIL')
GMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD')

if GMAIL is None or GMAIL_PASSWORD is None:
    print('You should config environment variable.')
    print('Run the command like following.')
    print('$ echo \'export GMAIL="hogehoge@gmail.com"\' >> ~/.bashrdc')
    print('$ echo \'export GMAIL_PASSWORD="password"\' >> ~/.bashrc')
    sys.exit()

def main(mail_to, subject, mail_body, img_path=None):
    message = setup_mail(subject, mail_to, mail_body)
    attach_img(message, img_path)
    send_mail(message)
    return


def setup_mail(subject, mail_to, mail_body):
    message = MIMEMultipart()
    message["Subject"] = subject
    message["To"] = mail_to
    message["From"] = GMAIL
    message.attach(MIMEText(mail_body, "html"))
    return message


def send_mail(message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(GMAIL, GMAIL_PASSWORD)
    server.send_message(message)
    server.quit()


def attach_img(message, img_path):
    if img_path is None:
        return
    with open(img_path, 'rb') as f:
        img = f.read()
    image = MIMEImage(img, name=img_path)
    message.attach(image)
    return
