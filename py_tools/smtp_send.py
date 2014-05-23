#send email using SMTP
#coding=utf-8 
import smtplib, mimetypes, time
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
from email.mime.image import MIMEImage  
  
msg = MIMEMultipart()  
msg['From'] = '2504584104@qq.com'  
msg['To'] = 'ouietesting@qq.com'  
msg['Subject'] = 'hello mail'  
  
#添加邮件内容  
txt = MIMEText('content abcde oakks %d' % time.time())
msg.attach(txt)  
'''
#添加二进制附件  
fileName = r'e:/PyQt4.rar'  
ctype, encoding = mimetypes.guess_type(fileName)  
if ctype is None or encoding is not None:  
    ctype = 'application/octet-stream'  
maintype, subtype = ctype.split('/', 1)  
att1 = MIMEImage((lambda f: (f.read(), f.close()))(open(fileName, 'rb'))[0], _subtype = subtype)  
att1.add_header('Content-Disposition', 'attachment', filename = fileName)  
msg.attach(att1)  
'''  
#发送邮件  
smtp = smtplib.SMTP()  
smtp.connect('smtp.qq.com:587')
smtp.login('2504584104@qq.com', 'k@jusF!8')  
smtp.sendmail('2504584104@qq.com', 'ouietesting@qq.com', msg.as_string())  
smtp.quit()  
print '邮件发送成功'.decode('UTF-8').encode('GBK')
