import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
Period=100
Time_Interval=1
Number_of_Crazyflies=20

mu=(Number_of_Crazyflies-1)*(Time_Interval/Period)
sigma=(Number_of_Crazyflies-1)*(Time_Interval/Period)*(1-Time_Interval/Period)
mu*=Number_of_Crazyflies
sigma*=Number_of_Crazyflies
samples_normal=np.random.normal(mu,sigma,10000)

#绘制正态分布
x_normal=np.linspace(0,10,500)
y_normal=norm.pdf(x_normal,mu,sigma)

plt.hist(samples_normal,bins=50,density=True,alpha=0.5,label='Generated samples')
plt.plot(x_normal,y_normal,color="red",label='Normal distribution')
plt.xlabel('丢包次数')
plt.ylabel('概率')
plt.title('Period: '+str(Period)+'s, Number of crazyflies: '+str(Number_of_Crazyflies))
plt.legend()
plt.show()

