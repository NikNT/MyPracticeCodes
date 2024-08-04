import smtplib

sender = "sndr@gmail.com"
receiver = "rcvr@gmail.com"
password = "password"
subject = "Python Email Test"
body = "I wrote an email using Python!"

message = f"""

From : Snoop Doog {sender}
To : Nicholas Cage {receiver}

Subject: {subject}\n
{body}

"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print('Logged In!')

    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("Unable to Sign In")
    