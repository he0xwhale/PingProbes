# -*- coding: utf-8 -*-
from  message.message import sendmail
from utils.file import readConfig
def sendmails(subject,content):
    config=readConfig()
    email=config["email"]["addr"]
    if (email!=None):
        sendmail(config=config,subject=subject,content=content)
