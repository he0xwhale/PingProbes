# _*_ coding:utf-8 _*_
#!/usr/bin/python
import os,time,multiprocessing

from utils.logger import *
log=getMyLogger()
from utils.file import *
from utils.network import verbose_ping
from  message import message
from utils.heartbeat import startHeartProcess

IPLIST="./config/data/ip.list"
CONFIG="./config/config.json"

MAX_process = 300       #mutiprocessing
sms_off = 0

def readIPsAndConfig():
    """
    读取并返回ip.list和config.json
    """
    if(os.path.exists(IPLIST)):
        iplist=readIPlist(filename=IPLIST)
        log.info(u"ip.list读取成功")
    else:
        log.error(u"ip.list文件不存在，请手动创建该文件，并列出需要监控的ip")
        os._exit(0)
    if(os.path.exists(CONFIG)):
        config=readConfig(filename=CONFIG)
        log.info(u"配置文件config.json读取成功")
    else:
        log.error(u"config.json文件不存在，请手动创建该文件，并写入配置项")
        os._exit(0)
    return iplist,config

def startMonitorTask(ip,config):
    email = config['email']["addr"]
    emailEnable=config['email']['enable']
    smsNumber = config['sms']['number']
    smsEnable=str(config['sms']['enable'])

    log.info(u"开始测试{ip}".format(ip=ip))
    status=verbose_ping(ip)
    if ("Up" != status):
        warnning_message=u"IP:{ip} 掉线，请及时查看".format(ip=ip)
        log.warn(warnning_message)
        subject=u"{ip} 掉线提醒".format(ip=ip)
        if (smsNumber!=None and  smsEnable=="true"):
            message.send_muti_sms(smsNumber,sms_off,subject,warnning_message)
        if (email!=None and emailEnable=="true"):
            message.sendmail(config=config,subject=subject,content=warnning_message)


def startMonitorTasks(iplist,config):
    log.info(u"开启监控任务")
    while 1:
        pool = multiprocessing.Pool(processes=len(iplist))
        result = []
        for ip in   iplist:
            result.append(pool.apply_async(startMonitorTask, (ip,config )))
        pool.close()
        pool.join()
        for res in result:
            if (res.successful() != True):
                log.error(u"任务:ping {r}失败，请检查原因".format(r=str(res.get(),encoding="utf-8")))
        log.info(u"本轮监控结束")
        sleepTime=float(config['duration'])
        log.info(u"等待{time}s后，开启下一轮监控扫描".format(time=sleepTime))
        time.sleep(sleepTime)
        log.info(u"{time}s时间到，开启下一轮监控扫描".format(time=sleepTime))


def main():
    log.info(u"开启PingProbes")
    log.info(u"开始读取ip.list和config.json")
    iplist,config = readIPsAndConfig()
    startHeartProcess()
    startMonitorTasks(iplist,config)
if __name__ == "__main__":
    main()

