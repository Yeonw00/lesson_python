from email.mime import multipart
from email.mime import text
import smtplib

import config

smtp_host = 'smtp.gmail.com'
smtp_port = 587
from_email = config.from_email
to_email = config.to_email
username = config.username
password = config.password

# msg = EmailMessage()
msg = multipart.MIMEMultipart()
# msg.set_content('안녕하세요. 이 메일은 SMTP 테스트입니다.')
msg['Subject'] = '테스트 메일 - Python SMTP'
msg['From']  = from_email
msg['To'] = to_email
msg.attach(text.MIMEText('안녕하세요. 이 메일은 SMTP 테스트입니다.', 'plain'))

with open('send_email_with_file.py', 'r', encoding='utf-8') as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment',
        filename='lesson.txt'
    )
    msg.attach(attachment)

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