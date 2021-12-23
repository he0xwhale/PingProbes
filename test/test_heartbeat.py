# -*- coding: utf-8 -*-
# from utils.file import readIPlist
# 在这个项目中,tests目录下的test_utils.py就可以直接引用utils，不知道这里为什么不行
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils.heartbeat import heartBeat,startHeartProcess

def test_heartBeat():
    heartBeat(intervalTime=1)
# test_heartBeat()

def test_startHeartProcess():
    startHeartProcess()
test_startHeartProcess()