#!/usr/bin/python3
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="***"  #设置服务器
mail_user="***"    #用户名
mail_pass="***"   #口令 
 
 
sender = '**'
receivers = ['***']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('各位小伙伴吃饭要积极，开始点餐啦，点餐地址：http://testtool.vanglis.com', 'plain', 'utf-8')
message['From'] = Header("系统邮件，请勿回复")
message['To'] =  Header("***", 'utf-8')
 
subject = '开始点餐提醒'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException as e:
    print (e)
