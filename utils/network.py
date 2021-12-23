# _*_ coding:utf-8 _*_
from ping.ping import do_one
import socket
from utils.logger import getMyLogger
log=getMyLogger()
def verbose_ping(dest_addr, timeout = 2, count = 5):
    """
    Send >count< ping to >dest_addr< with the given >timeout< and display
    the result.
    """
    Stats = "unkown"  

    for i in range(count):
        try:
            delay  =  do_one(dest_addr, timeout)
        except socket.gaierror as e:
            log.warn(u"ping {dest_addr} 失败. (socket error: {error})".format(dest_addr=dest_addr,error=e[1]))
            return  "socketError"

        if delay  ==  None:
            log.warn(u"ping {dest_addr} 失败. (timeout within {timeout}sec.)".format(dest_addr=dest_addr,timeout=timeout))
            Stats =  "Down"
        else:
            delay  =  delay * 1000
            log.info(u"ping {dest_addr} success in {delay:.2f}ms".format(dest_addr=dest_addr,delay=delay))

            return  "Up"
    return Stats