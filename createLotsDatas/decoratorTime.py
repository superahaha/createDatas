#-*- coding:utf-8 -*-

import time

def timer(function):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        function(*args, **kwargs)
        time_end = time.time()
        spend_time = time_end - time_start
        print("耗时：{}秒".format(spend_time))
    return wrapper


