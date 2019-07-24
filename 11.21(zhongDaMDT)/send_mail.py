'''运行不报错，但是没有结果'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱服务器
smtpserver = 'qiye.aliyun.com'
# 邮箱用户名、密码
user = 'zhanghh@chinacaring.com'
password = 'Zhh123456'
# 发送邮箱
sender = 'zhanghh@chinacaring.com'
# 接受邮箱
receiver = 'leisc@chinacaring.com'
# 发送邮件的主题
subject = 'python邮箱测试'
# 编写HTML类型的邮件正文
msg = MIMEText('<html><h1>你好!</h1></html>','html','utf-8')
msg ['subject'] = Header(subject,'utf-8')

# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
print('end')
