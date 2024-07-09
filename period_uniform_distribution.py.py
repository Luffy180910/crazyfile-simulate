import numpy as np
import matplotlib.pyplot as plt
import random


M=[]
PERIOD=10

list=[10,10,10,10,10,
      10,10,10,10,10,PERIOD]
    


sub=np.zeros(10)
sub=( [-1,0,0,0,0,0,0,0,0,1,0],
      [1,-1,0,0,0,0,0,0,0,0,0],
      [0,1,-1,0,0,0,0,0,0,0,0],
      [0,0,1,-1,0,0,0,0,0,0,0],
      [0,0,0,1,-1,0,0,0,0,0,0],
      [0,0,0,0,1,-1,0,0,0,0,0],
      [0,0,0,0,0,1,-1,0,0,0,0],
      [0,0,0,0,0,0,1,-1,0,0,0],
      [0,0,0,0,0,0,0,1,-1,0,0],
      [0,0,0,0,0,0,0,0,1,-1,0],
      [0,0,0,0,0,0,0,0,0,0,1]    )




def generate_matrix():
    for i in range(10):
        Mi = np.identity(11)
        for j in range(11):
            Mi[j][j]=1
        Mi[i][i]=0
        Mi[(i-1)%10][i]=0.5
        Mi[(i+1)%10][i]=0.5
        Mi[10][i]=0.5
        # print(Mi)
        M.append(Mi)

    # for i in range(10):
    #     print("第"+str(i+1)+"个矩阵")
    #     print(M[i])
    #     print("\n")

def move(array):
    for i in range(10):
        array=np.dot(array,M[i])
        print(array)
    return array
    
        
if __name__ == '__main__':
    # show()
    generate_matrix()

    I_10 = np.identity(11)
    # print(I_10)
    for i in range(10):
        I_10=np.dot(I_10,M[i])
        print("第"+str(i+1)+"个矩阵")
        print(I_10)
        print("\n")

    Array=np.array(list)
    
    
    main_count=0
    while(main_count<30):

        for i in range(0,10):
            # plt.plot(Array[i]%10,main_count,'o',markersize=1)
            temp=np.dot(Array,sub)
            plt.plot(temp[i]%10,main_count,'o',markersize=1)
            print(np.dot(Array,sub))
        main_count+=1
        Array=move(Array)
    # plt.xlim(0,10)
    plt.savefig("distance.png")
    plt.show()  
    