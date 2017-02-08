import smtplib

from_addr = 'blackbeard@gmail.com'

to_addr = 'david@someemail.com'

from_name = 'Andrew'
to_name = 'David'
subject = 'test'
msg = 'Yo waddup this is a test script!'

message = """From: {} <{}>

to: {} <{}>

Subject: {}
{}
"""

message_to_send = message.format(from_name, from_addr, to_name,
to_addr, subject, msg)
# Credentials (if needed)
username = 'blackbeard@gmail.com'
password = 'yohohoandabottleofrum'
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()

