import numpy as np
import matplotlib.pyplot as plt

BEGIN = 0
END = 1
distribuition = [BEGIN,1,1,1,1,1,
                 1,1,1,1,1,END]

count=100
M=[]





def show():
    while count:
        print(distribuition)
        for i in range(1,11):
            distribuition[i]=(distribuition[i-1]+distribuition[i+1])/2
            plt.plot(distribuition[i],100-count,'o',markersize=1)

        count-=1
    plt.xlim(0,1)
    plt.show()


if __name__ == '__main__':
    # show()
    # print(M)
    for i in range(10):
        Mi = np.identity(10)
        Mi[i][i]=0
        Mi[(i-1)%10][i]=0.5
        Mi[(i+1)%10][i]=0.5
        M.append(Mi)

    for i in range(10):
        print("第"+str(i+1)+"个矩阵")
        print(M[i])
        print("\n")

    I_10 = np.identity(10)
    print(I_10)
    for i in range(10):
        I_10=np.dot(I_10,M[i])    
        print("第"+str(i+1)+"个矩阵")
        print(I_10)
        print("\n")
