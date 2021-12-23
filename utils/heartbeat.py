# _*_coding:UTF-8_*_
import threading
from utils.messages import sendmails
from utils.file import  readConfig
from threading import Timer
from utils.logger import getMyLogger
log=getMyLogger()
def heartBeat(i,intervalTime,enable):
    
    """
    intervalTime: 检测间隔时间
    enable:是否开启探测
    """

    if enable=="true" and intervalTime!=None:
        #发送邮件到通知邮箱
        if i!=0:
            log.info(u"No.{i} 发送心跳检测邮件...，心跳检测周期为{intervalTime}s".format(i=i,intervalTime=intervalTime))
            sendmails(subject=u"心跳检测",content=u"程序每隔{i}s发送一次心跳检测，如果超过{i}秒未再次收到此邮件，请查看程序是否在正常运行".format(i=intervalTime))
        i+=1
        t=threading.Timer(intervalTime,heartBeat,args=(i,intervalTime,enable))
        t.start()



def startHeartProcess():
        #读取配置文件
    config=readConfig()
    enable=config["heartBeat"]["enable"]
    intervalTime=config["heartBeat"]["intervalTime"]
    log.info(u"开启心跳检测进程")
    heartBeat(0,intervalTime,enable)

