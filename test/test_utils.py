# -*- coding: utf-8 -*-
# from utils.file import readIPlist
# 在这个项目中,tests目录下的test_utils.py就可以直接引用utils，不知道这里为什么不行
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils.file import *

def test_readIPlist():
    ipList=readIPlist(filename="test/data/ip.list")
    print(ipList)

def test_readConfig():
    config=readConfig(filename="data/config.json")
    print(config["duration"])
    print(config["email"])
    print(type(config["email"]))
    print(config["email"]!=None)
    print(config["sms"])
    if(config['sms']==None):
        print("no sms")
# test_readConfig()

def test_logger():
    from utils.logger import getMyLogger
    log=getMyLogger(logPath="logs/monitor.log")
    log.info("info test")
# test_logger()

