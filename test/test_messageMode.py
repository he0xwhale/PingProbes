# -*- coding: utf-8 -*-
import sys,os
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from message.message import sendmail
from utils.file import readConfig
# 在这个项目中,tests目录下的test_utils.py就可以直接引用utils，不知道这里为什么不行
# sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# from utils.file import *
def test_sendmail():
    config=readConfig(filename="data/config.json")
    sendmail(config=config,subject='testSubject',content="testConent",mailEnabled=True)

test_sendmail()