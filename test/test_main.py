# -*- coding: utf-8 -*-
import sys,os
# 在这个项目中,tests目录下的test_utils.py就可以直接引用utils，不知道这里为什么不行
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from main import  *
def test_getDuration():
    iplist,config=readIPsAndConfig()
    print(type(getDuration()))
# test_getDuration()

def test_startMonitorTasks():
    iplist=["bing.com"]
    import json
    content="""
    {
    "duration": "6",
    "email": {
        "enable": "true",
        "addr": "test@hotmail.com"
    },
    "sms": {
        "enable": "false",
        "number": 12345678901
    },
    "smtp": {
        "sender": "test@hotmail.com",
        "server": "smtp.office365.com",
        "port": 587,
        "username": "test@hotmail.com",
        "password": "password"
    }
}
    """
    config=json.loads(content)
    # print(config['duration'])
    startMonitorTasks(iplist,config)
test_startMonitorTasks()