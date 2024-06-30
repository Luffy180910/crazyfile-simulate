import numpy as np
import matplotlib.pyplot as plt
import time
import math
from random import random 

PERIOD=15   #ms
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
        self.message={"address":0,"seq":0,"timestamp":0}

    def tx(self,message):
        self.message=message
        log_add_seq.append(self.message["seq"])
        log_add_timestamp.append(self.message["timestamp"])
        log_add_address.append(self.message["address"])
    def rx(self):
        return self.message
        

class crazyflie:
    
    def __init__(self,addr):
        self.period=PERIOD - random()%1*0.02   #ms
        self.next_tx_time = random()%1*self.period   #ms
        self.temp_delay=0
        self.seq=0
        self.addr=addr
        self.timestamp=0
        self.message={"address":0,"seq":0,"timestamp":0}
    def tx(self):
        if now_time>=self.next_tx_time:
            self.timestamp=self.next_tx_time
            self.next_tx_time+=self.period+self.temp_delay
            self.temp_delay=0
            self.message["address"]=self.addr
            self.message["seq"]=self.seq
            self.message["timestamp"]=self.timestamp
            self.seq+=1

            env.tx(self.message)

    def rx(self):
        rx_message=env.rx()
        if -rx_message["timestamp"]+self.next_tx_time<self.period:
            if -rx_message["timestamp"]+self.next_tx_time<2:
                self.temp_delay=1
        
    def swarm_range(self):
        signal_rx_tx = 1

def plot_period():
    # print("length of log_add:",len(log_add))
    for i in range(len(log_add_seq)-1):
        plt.plot((log_add_timestamp[i]+plt_move)%AVERAGE_PERIOD,log_add_seq[i],'o',color=COLOR_LIST[log_add_address[i]],markersize=1)
        # print(log_add[i]["timestamp"],log_add[i]["seq"],log_add[i]["address"])
    
    plt.ylabel("seq")
    plt.title(' multi crazyflie period change in sniffer view ')
    plt.xlim(0,AVERAGE_PERIOD)

    plt.show()


if __name__ == '__main__':
    env=environment()
    uwb_time_ms=Time(0)
    cf1=crazyflie(1)
    cf2=crazyflie(2)
    cf3=crazyflie(3)
    cf4=crazyflie(4)
    num_of_while=1e3*1e3
    while num_of_while:
        now_time=uwb_time_ms.update()
        if num_of_while%1000==0:
            print(now_time)
        cf1.rx()
        cf1.tx()
        cf2.rx()
        cf2.tx()
        cf3.rx()
        cf3.tx()
        cf4.rx()
        cf4.tx()
        num_of_while-=1
        
    plot_period()