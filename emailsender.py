import smtplib

to = input("Enter the Email of the Reciepent:\n")

content = input("Enter the content for mail:\n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.echo()
    server.starttls()
    server.login('senderemail@gmail.com','1234')
    server.sendermail('sendermail@gmail.com', to, content)
    server.close()

sendEmail(to, content)