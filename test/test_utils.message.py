# -*- coding: utf-8 -*-
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.messages import sendmails

def test_sendmails():
    sendmails(subject=u"标题",content=u"内容")

test_sendmails()