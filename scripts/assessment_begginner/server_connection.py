import socket
from ssh2.session import Session
import requests
import smtplib

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to Machine...")
s.connect(("172.18.51.115", 22))

session = Session()
session.handshake(s)
session.userauth_password('*****', '****')

# Creating a session
channel = session.open_session()
channel.execute('ls')
size, data = channel.read()
while size > 0:
    print(data.decode())
    size, data = channel.read()
channel.close()

if channel.get_exit_status() == 0:
    print("Connection established")
    s1 = smtplib.SMTP('smtp.gmail.com',587)

    s1=smtplib.SMTP_SSL("smtp.gmail.com",465)
    s1.ehlo()

    s1.starttls()

    # Authentication
    s1.login("****@gmail.com", "*****")

    # message to be sent
    message = "Connection established with machine"

    # sending the mail
    s1.sendmail("****", "*****", message)

    # terminating the session
    s1.quit()
    print("Mail Sent")
else:
    print("Connection failed {0}".format(channel.get_exit_status()))
