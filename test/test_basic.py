# encoding:utf-8
# import logging
# LOG_FORMAT ="%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = "%Y/%m/%d %H:%M:%S %p"
# # logging.basicConfig(filename='my.log',level=logging.INFO,format=LOG_FORMAT,datefmt=DATE_FORMAT)
# # logging.info("info level")

# logger=logging.getLogger()
# logger.setLevel('DEBUG')
# formatter=logging.Formatter(LOG_FORMAT,datefmt=DATE_FORMAT)

# fh=logging.FileHandler('data/logs/monitor.log')
# fh.setLevel(logging.INFO)
# fh.setFormatter(formatter)

# sh=logging.StreamHandler()
# sh.setLevel(logging.INFO)
# sh.setFormatter(formatter)

# logger.addHandler(fh)
# logger.addHandler(sh)
# logger.info("this info message")

# lists=[1,2]
# print(len(lists))
# res="test"
# print("任务:{res}失败，请检查原因".format(res=res))
# iplist=["a","b"]
# for index in xrange(len(iplist)):
#     print(iplist[index])

# from multiprocessing import Process
# import os

# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')


# from threading import Timer
# import datetime


# def MonitorSystem(logfile = None):
#     cpuper = "cpuper"
#     mem = "mem"
#     memper = mem
#     now = datetime.datetime.now()
#     ts = now.strftime('%Y-%m-%d %H:%M:%S')
#     line = 'cpu:, mem'
#     print(line)
#     if logfile:
#         logfile.write(line)
#     #启动定时器任务，每三秒执行一次
#     Timer(3, MonitorSystem).start()


# def MonitorNetWork(logfile = None):
#     netinfo = "netinfo"
#     now = datetime.datetime.now()
#     ts = now.strftime('%Y-%m-%d %H:%M:%S')
#     line = 'bytessent}'
#     print(line)
#     if logfile:
#         logfile.write(line)
#     #启动定时器任务，每秒执行一次
#     Timer(1, MonitorNetWork).start()


# #记录当前时间
# print(datetime.datetime.now())
# #3S执行一次
# sTimer = Timer(3, MonitorSystem)
# #1S执行一次
# nTimer = Timer(1, MonitorNetWork)
# #使用线程方式执行
# sTimer.start()
# nTimer.start()
# #等待结束
# sTimer.join()
# nTimer.join()
# #记录结束时间
# print(datetime.datetime.now())

# s=u"中文"
# print s

import threading #多线程

def repeat(i):
    i=i+1
    print(u'执行次数:',i)
    
    t = threading.Timer(4, repeat,[i])   #[i] 是repeat参数
    t.start()    
    print(u"repeate结束")
repeat(0)
print(u"main")
