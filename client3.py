import subprocess
import json
import requests
from threading import Timer
from datetime import datetime
import re
import psutil
#发送时间 CPU利用率  四张卡显卡利用率，显存占用


class MySend:
    def send_info(self):
        '''获取当前时间'''
        current_time=str(datetime.now())

        cpu_usage=psutil.cpu_percent(1)  #通过时间间隔1s 获取cpu利用率
        
        memory_usage=psutil.virtual_memory().percent
        
        dict_trans={'current_time':current_time,'cpu_use_ratio':cpu_usage,'memory_ratio':memory_usage}
        json_trans=json.dumps(dict_trans)
        '''传输json串,用requests'''
        response=requests.post(url='http://47.115.204.111:8000/heart/',data=json_trans)

class MyTimer():
    def __init__(self, start_time, interval, program):
        self.__timer=None
        self.__start_time=start_time
        self.__interval=interval
        self.__program=program
    
    def exec_program(self):
        # print(1)
        self.__program()
        self.__timer=Timer(self.__interval,self.exec_program)  #用于执行等待的时间，要执行的方法
        self.__timer.start()

    def start(self):
        #中止时间减去已经进行了多少时间   (现在的时间减去起始的时间)
        interval=self.__interval-(datetime.now().timestamp()-self.__start_time.timestamp())
        self.__timer=Timer(interval,self.exec_program)  #用于执行等待的时间，要执行的方法
        self.__timer.start() #开始才能执行上一个语句
    def cancel(self):
        self.__timer.cancel()
        self.__timer=None

if __name__=='__main__':
    send=MySend()  #实例化类
    start=datetime.now()
    tmr=MyTimer(start,60*3,send.send_info) #每三分钟发送一次
    tmr.start()
