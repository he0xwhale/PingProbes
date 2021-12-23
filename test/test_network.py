import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils.network import *



def test_verbose_ping():
    # verbose_ping("fasdfasdfefas.com")
    verbose_ping("bing.com")

test_verbose_ping()