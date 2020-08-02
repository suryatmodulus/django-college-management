import sendgrid
from sendgrid.helpers.mail import *

def Send_Email(to_email,msg_body):
    sg = sendgrid.SendGridAPIClient(apikey='')
    from_email = Email("dscefurore@gmail.com")
    to_email = Email(to_email)
    subject = "Furore'18 Registration !"
    content = Content("text/plain",msg_body)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

