import numpy as np
import matplotlib.pyplot as plt
import time
import math
from random import random 

PERIOD=100   #ms
COLOR_LIST=['red','green','blue','yellow','pink',
            'orange','purple','brown','gray','olive',
            'cyan','lime','navy','tan','magenta',
            'gold','silver','violet','indigo','crimson']
plt_move=0
AVERAGE_PERIOD=PERIOD   #ms
time_step=0.01   #ms
now_time=0        #ms
log_add_seq=[]
log_add_timestamp=[]
log_add_address=[]

class Time:
    def __init__(self, start_time):
        self.now_time = start_time
    def update(self):
        self.now_time += time_step
        return self.now_time
    
    
class environment:
    def __init__(self):
        self.message={"address":-1,"seq":0,"timestamp":0}

    def tx(self,message):
        self.message=message
        log_add_seq.append(self.message["seq"])
        log_add_timestamp.append(self.message["timestamp"])
        log_add_address.append(self.message["address"])
    def rx(self):
        return self.message
    def clean(self):
        self.message={"address":-1,"seq":0,"timestamp":0}

class crazyflie:
    
    def __init__(self,addr):
        #宏观误差
        Macro_error=random()%1*0.02   #ms
        self.period=PERIOD -Macro_error   #ms
        self.next_tx_time = random()%1*self.period   #ms 随机初始发送时间
        self.temp_delay=0
        self.seq=0
        self.addr=addr
        self.timestamp=0
        self.message={"address":-1,"seq":0,"timestamp":0}
    def tx(self):
        if now_time>=self.next_tx_time:
            self.timestamp=self.next_tx_time
            #微观误差
            Micro_error=random()%1*0.03-0.015   #ms
            self.next_tx_time+=self.period+self.temp_delay+Micro_error   #ms
            self.temp_delay=0
            self.message["address"]=self.addr
            self.message["seq"]=self.seq
            self.message["timestamp"]=self.timestamp
            self.seq+=1

            env.tx(self.message)

    def rx(self):
        rx_message=env.rx()
        if rx_message["address"]==self.addr:
            env.clean()
            return 
        if rx_message["address"]==-1:
            return
        # print("crazyflie",self.addr,"rx",rx_message["address"],rx_message["timestamp"])
        #发送离接受太近（接受在发送之前） 推迟下一次发送
        if -rx_message["timestamp"]+self.next_tx_time<self.period:
            if -rx_message["timestamp"]+self.next_tx_time<2:
                self.temp_delay=1
        #发送离接受太进（接受在发送之后） 提前下一次发送
        if rx_message["timestamp"]+self.period-self.next_tx_time<self.period:
            if rx_message["timestamp"]+self.period-self.next_tx_time<2:
                self.temp_delay=-1

    def memory(self,message):
        1

    def swarm_range(self):
        self.rx()
        self.tx()

def plot_period():
    # print("length of log_add:",len(log_add))
    for i in range(len(log_add_seq)-1):
        plt.plot((log_add_timestamp[i]+plt_move)%AVERAGE_PERIOD,log_add_seq[i],'o',color=COLOR_LIST[log_add_address[i]-1],markersize=1)
        # print(log_add[i]["timestamp"],log_add[i]["seq"],log_add[i]["address"])
    
    plt.ylabel("seq")
    plt.title(' multi crazyflie period change in sniffer view ')
    plt.xlim(0,AVERAGE_PERIOD)
    plt.savefig(time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())+'.png')

    plt.show()


if __name__ == '__main__':
    env=environment()    #初始化环境
    uwb_time_ms=Time(0)  #初始化时间
    cf1=crazyflie(1)
    cf2=crazyflie(2)
    cf3=crazyflie(3)
    cf4=crazyflie(4)
    cf5=crazyflie(5)
    cf6=crazyflie(6)
    cf7=crazyflie(7)
    cf8=crazyflie(8)
    cf9=crazyflie(9)
    cf10=crazyflie(10)
    cf11=crazyflie(11)
    cf12=crazyflie(12)
    cf13=crazyflie(13)
    cf14=crazyflie(14)
    cf15=crazyflie(15)
    cf16=crazyflie(16)
    cf17=crazyflie(17)
    cf18=crazyflie(18)


    num_of_while=1e3*1e3*10
    while num_of_while:
        now_time=uwb_time_ms.update()
        if num_of_while%1000==0:
            print(now_time)
        cf1.swarm_range()
        cf2.swarm_range()
        cf3.swarm_range()
        cf4.swarm_range()
        cf5.swarm_range()
        cf6.swarm_range()
        cf7.swarm_range()
        cf8.swarm_range()
        cf9.swarm_range()   
        cf10.swarm_range()
        cf11.swarm_range()
        cf12.swarm_range()
        cf13.swarm_range()
        cf14.swarm_range()
        cf15.swarm_range()
        cf16.swarm_range()
        cf17.swarm_range()
        cf18.swarm_range()


        num_of_while-=1
        
    plot_period()