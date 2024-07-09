import numpy as np
import matplotlib.pyplot as plt
import random

distrubution = [0,0,0,0,1]
M=[]

for i in range(5):
    In=np.identity(5)

    In[i][i]=0.5
    In[i][(i+1)%5]=0.5
    In[(i+1)%5][i]=0.5
    In[(i+1)%5][(i+1)%5]=0.5
    M.append(In)
    print(In)



temp=np.identity(5)
for j in range(10): 
    for i in range(5):
        temp=np.dot(temp,M[i])
        print("第"+str(i+1+j*5)+"次乘积：")
        print(temp)
        print("\n")


M_I=np.identity(5)
for i in range(5):
    M_I=np.dot(M_I,M[i])

print("M_I:")
print(M_I)
print("最终结果：")
a,b=np.linalg.eig(M_I)
a=a.round(4)
b=b.round(4)
print("a")
print(a)
print("b")
print(b)
c=np.linalg.inv(b)
c=c.round(4)
print("c")
print(c)
a=(1,0,0,0,0)
a=np.diag(a)
d=np.dot(b,a)
d=np.dot(d,c)
d=d.round(4)
print("d")
print(d)
# c=np.dot(b,b.T)
# c=c.round(4)
# print("c")
# print(c)
# d=np.dot(b.T,b)
# d=d.round(4)
# print("d")
# print(d)