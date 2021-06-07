import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
fromaddr = "kristian.dini01@gmail.com"
toaddr = "kristian.dini01@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "coba python with email"
 
body = "belajar mengirim pesan email dengan python"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "d01061993")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
