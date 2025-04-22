from email.message import EmailMessage
import smtplib

import config

smtp_host = 'smtp.gmail.com'
smtp_port = 587
from_email = config.from_email
to_email = config.to_email
username = config.username
password = config.password

msg = EmailMessage()
msg.set_content('안녕하세요. 이 메일은 SMTP 테스트입니다.')
msg['Subject'] = '테스트 메일 - Python SMTP'
msg['From']  = from_email
msg['To'] = to_email

try:
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.send_message(msg)
    server.quit()
    print('메일이 성공적으로 전송되었습니다.')
except Exception as e:
    print('메일 전송 실패:', e)