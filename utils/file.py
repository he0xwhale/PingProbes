# -*- coding: utf-8 -*-
import os
class CustomDict(dict):
    def __missing__(self, key):
        return None

# 读取ip列表
def readIPlist(filename="ip.list"):
    lines=[]
    with open(filename) as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines

#读取配置文件config.json
def readConfig(filename=os.getcwd()+"/config/config.json"):
    import json
    content=""
    with open(filename) as f:
        content=f.read()
    paras=CustomDict(json.loads(content))
    return paras


