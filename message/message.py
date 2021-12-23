#!/usr/bin/python
#coding=utf-8
import smtplib
from email.mime.text import MIMEText
# import urllib2
from utils.logger import getMyLogger
log=getMyLogger()

#-----message channel-----------------
sms_string = 'http://xxx/smsweb/send4vpn.do?clientId=60004&tel='
#----------

def send_muti_sms(config,_sms_off,title,content):
    pass
    # phones=config['sms']
    # for sms_index in range(0, len(phones.split(';'))):
    #     if _sms_off == 1:
    #         break
    #     phone = phones.split(';')[sms_index]
    #     content = content.replace(chr(34),"\"")                                           #replace " to \"
    #     if len(content) > 230:
    #         content = content[:230]                                                       # cut the string to 300
    #     sms_send_string = sms_string + phone+ '&context='+urllib2.quote(content)     #according to your message channel ,may be you should change here
    #     if phone.find('null') == -1:
    #         request =  urllib2.Request(sms_send_string)
    #         try:
    #             urllib2.urlopen(request)
    #             logger.info(u"短信发送成功，手机号码：{phone}，标题：{title}，内容：{content}".format(phone=phone,title=title,content=content))
    #         except urllib2.HTTPError as e:
    #             logger.error(u"短信发送失败，手机号码：{phone}，HTTP错误：{httpError}".format(phone=phone,httpError=str(e.code)+str(e.reason)))
    #         except urllib2.URLError as e:
    #             logger.error(u"短信发送失败，手机号码：{phone}，URL错误：{urlError}".format(phone=phone,urlError=str(e.reason)))


def sendmail(config,subject,content):
    mailAddresses=config["email"]["addr"]
    sender = config["smtp"]["sender"]
    smtpserver = config["smtp"]["server"]
    port=config["smtp"]["port"]
    username = config['smtp']["username"]
    password = config['smtp']["password"]
    
    log.info(u"邮箱相关配置读取成功！")
    log.debug(u"smtpserver:{smtpserver},port:{port},username:{username},password:{password}".format(smtpserver=smtpserver,port=port,username=username,password=password))
    for mail_index in range(0, len(mailAddresses.split(';'))):
        _receiver =  mailAddresses.split(';')[mail_index]
        log.info(u"尝试向{_receiver}发送邮件，请等待...".format(_receiver=_receiver))
        if _receiver.find('null') == -1:
            try:
                msg = MIMEText('<html>'+content+'</html>','html','utf-8')
                msg['Subject'] =  subject
                msg['to'] = _receiver
                smtp = smtplib.SMTP(smtpserver,port)
                if("smtp.office365.com"==smtpserver):
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()
                smtp.login(username, password)
                log.debug("smtp.login")
                smtp.sendmail(sender,_receiver, msg.as_string())
                smtp.quit()
                log.info(u"邮件发送成功!  subject:{subject} To:{_receiver}".format(subject=subject,_receiver=_receiver))
            except Exception as e:
                log.error(u"mail send fail!  subject:{subject} To:{_receiver}. Error Message:{errorMessage}".format(subject=subject,_receiver=_receiver,errorMessage=e))
    log.info(u"所有邮件发送完毕")
