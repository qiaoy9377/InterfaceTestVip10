'''
功能描述：配置邮箱，测试用例执行完毕后将测试报告邮件发送
实现逻辑：
1-配置邮箱参数
2-组装邮件内容
3-登录并发送邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time,os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

def sendEmail():
    #1-配置邮箱信息，发件人、收件人、主题，邮箱服务器
    sender = '372305058@qq.com'
    receiver = '18335909377@163.com'
    now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    subject = 'python邮件发送测试'+now_time
    smtpserver = 'smtp.qq.com'
    username = '372305058'
    password = 'ohgyvudtacyccabi'
    content = 'python邮件发送测试正文'

    #2-添加附件功能
    file = os.path.dirname(os.path.dirname(__file__))+'/testData/data-result.xls'
    #读取文件内容
    with open(file,'rb') as f:
        mail_body = f.read()
        #组装邮件内容和标题
        #实例化类
        msg = MIMEMultipart()
        #添加附件
        att = MIMEText(mail_body,'plain','utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment;filename=report.xls'
        msg.attach(att)
        content2 = '测试报告详见附件，请查收'
        msg.attach(MIMEText(content2,'plain','utf-8'))

    #2-组装邮件内容，正文拼接主题，发件人，收件人
    # msg = MIMEText(content,'plain','utf-8')
    msg['Subject'] = Header(subject,'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    #3-登录并发送邮件
    try:
        #实例化邮件类
        se = smtplib.SMTP()
        #连接邮箱服务
        se.connect(smtpserver)
        #登录邮箱
        se.login(username,password)
        #设置发件人、收件人、内容
        se.sendmail(sender,receiver,msg.as_string())
    except Exception as e:
        print('邮件发送失败：',e)
    else:
        print('邮件发送成功')
    finally:
        se.quit()

if __name__ == '__main__':
    sendEmail()