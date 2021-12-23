# _*_ coding:utf-8 _*_
import logging
log_path = r'logs/monitor.log'
LOG_FORMAT =" %(asctime)s - %(levelname)s - PID:%(process)d - %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S %p"

def singleton(cls):
  instances = {}
  def _singleton(*args,**kwargs):
    if cls not in instances:
      instances[cls] = cls(*args,**kwargs)
    return instances[cls]
  return _singleton
 
@singleton
class Log():
    def __init__(self,logPath=log_path):
        self.logger = logging.getLogger()
        formatter=logging.Formatter(LOG_FORMAT,datefmt=DATE_FORMAT)
        self.sh = logging.StreamHandler()
        self.sh.setFormatter(formatter)
        self.fh = logging.FileHandler(logPath)
        self.fh.setFormatter(formatter)
        self.logger.addHandler(self.sh)
        self.logger.addHandler(self.fh)
        self.logger.setLevel(logging.INFO)
    def returnLogger(self):
        return self.logger


def getMyLogger(logPath=log_path):
    return Log(logPath).returnLogger()