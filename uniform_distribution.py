import numpy as np
import matplotlib.pyplot as plt
import random
BEGIN = 0
END = 1
distribuition = [BEGIN,1,1,1,1,1,
                 1,1,1,1,1,END]


M=[]
PERIOD=10
sub=np.zeros(10)
sub=( [-1,0,0,0,0,0,0,0,0,1],
      [1,-1,0,0,0,0,0,0,0,0],
      [0,1,-1,0,0,0,0,0,0,0],
      [0,0,1,-1,0,0,0,0,0,0],
      [0,0,0,1,-1,0,0,0,0,0],
      [0,0,0,0,1,-1,0,0,0,0],
      [0,0,0,0,0,1,-1,0,0,0],
      [0,0,0,0,0,0,1,-1,0,0],
      [0,0,0,0,0,0,0,1,-1,0],
      [0,0,0,0,0,0,0,0,1,-1]  )



def show():
    count=100
    while count:
        print(distribuition)
        for i in range(1,11):
            distribuition[i]=(distribuition[i-1]+distribuition[i+1])/2
            plt.plot(distribuition[i],100-count,'o',markersize=1)

        count-=1
    plt.xlim(0,1)
    plt.show()

def generate_matrix():
    for i in range(10):
        Mi = np.identity(10)
        Mi[i][i]=0
        Mi[(i-1)%10][i]=0.5
        Mi[(i+1)%10][i]=0.5
        M.append(Mi)

    # for i in range(10):
    #     print("第"+str(i+1)+"个矩阵")
    #     print(M[i])
    #     print("\n")

def move(array):
    for i in range(10):
        array[(i+1)%10]+=10
        array=np.dot(array,M[i])
        array[(i+1)%10]-=10
        # print(array)
    return array
    
        
if __name__ == '__main__':
    # show()
    generate_matrix()
    I_10 = np.identity(10)
    # print(I_10)

    list=[10,10,10,10,10,
          10,10,10,10,10]
    

    array=np.array(list)
    
    # exit() 
    main_count=0
    while(main_count<30):
        array=move(array)
        for i in range(0,10):
            # plt.plot(array[i]%10,main_count,'o',markersize=1)
            temp=np.dot(array,sub)
            plt.plot(temp[i]%10,main_count,'o',markersize=1)
            print(np.dot(array,sub))
        main_count+=1
    # plt.xlim(0,10)
    plt.show()  
    