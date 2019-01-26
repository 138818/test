from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 邮件内容信息
message = MIMEText('hello,How are your\r\n', 'plain', 'utf8')
# message['From'] = Header('wjy@tedu.cn','utf8')
# message['To'] = Header('root@localhost', 'utf8')
# message['Subject'] = Header('my test', 'utf8')

# 邮件服务器识别信息
smtp = smtplib.SMTP('localhost')
sender = 'wjy@tedu.cn'
recervers = ['root@localhost']
smtp.sendmail(sender, recervers, message.as_bytes())
