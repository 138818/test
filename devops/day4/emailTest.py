from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass


def send_mail(text, subject, sender, receivers, server_host, password):
    message = MIMEText(text, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')



    smtp = smtplib.SMTP()
    smtp.connect(server_host)
    # smtp.starttls()  # 如果服务器要求安全通信,打开此注释
    smtp.login(sender, password)
    smtp.sendmail(sender, receivers, message.as_bytes())

if __name__ == '__main__':
    text = '我的邮件测试\r\n'
    subject = '测试'
    sender = 'wjy125yu@163.com'
    reveivers = ['wjy125yu@163.com', '344949398@qq.com']
    host = 'smtp.163.com'
    password = getpass.getpass('pass:')
    send_mail(text, subject, sender, reveivers,host, password)