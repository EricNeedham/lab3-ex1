import smtplib

fromaddr = 'eanneedham@gmail.com'
toaddr = 'eanneedham@gmail.com'
message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""
fromname = "Eric"
toname = "shan"
subject = "message"
msg = "whats up ma people"
toaddrs = "eanneedham@gmail.com"
messagetosend = message.format(

 fromname,

 fromaddr,

 toname,

 toaddr,

 subject,

 msg)

# Credentials (if needed)

username = 'eanneedham@gmail.com'

password = 'wmhfamjikzzstmtg'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddrs, messagetosend)

server.quit()