import numpy as np
import matplotlib.pyplot as plt
import random
# from numpy   import round
BEGIN = 0
END = 1
distribuition = [BEGIN,1,1,1,1,1,
                 1,1,1,1,1,END]


M=[]
PERIOD=10




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
    for i in range(1,11):
        Mi = np.identity(12)
        Mi[i][i]=0

        Mi[(i-1)%12][i]=0.5
        Mi[(i+1)%12][i]=0.5
        
        M.append(Mi)
    print("矩阵的特征向量")

    print(np.linalg.eig(M[0])[0])
    print(np.linalg.eig(M[1])[0])
    print(np.linalg.eig(M[2])[0])
    print(np.linalg.eig(M[3])[0])
    print("\n")
    print(np.linalg.eig(M[1])[1])
    print(np.linalg.eig(M[2])[1])
    print(np.linalg.eig(M[3])[1])
    print("\n")

    for i in range(10):
        print("第"+str(i+1)+"个矩阵")
        print(M[i])
        print("\n")

    I_10 = np.identity(12)
    for i in range(10):
        I_10 = np.dot(I_10,M[i])
        print("第"+str(i+1)+"个矩阵的乘")
        I_10=I_10.round(decimals=4)
        print(I_10)
        print("\n")
    print("最后的矩阵")
    print(np.linalg.eig(I_10)[0])

    I_temp=np.identity(12)
    print(I_temp)
    E=np.ones((12,12))
    print(E)

    print(I_10-I_temp+E)
    pai=np.linalg.pinv(I_10-I_temp+E)
    print("逆矩阵")
    print(pai)
    e=[1,1,1,1,1,1,1,1,1,1,1,1]
    pai_vector=np.dot(e,pai)
    print(pai_vector)
    
    print()    
        # temp1,temp2=np.linalg.eig(I_10)
        # print("第"+str(i+1)+"个矩阵的特征值")
        # print(temp1)
        # print(temp2)
        # print("\n")

    # for i in range(10):
    #     I_10 = np.dot(I_10,M[i])
    #     print("第"+str(i+11)+"个矩阵的乘")
    #     print(I_10)
    #     print("\n")


    # for i in range(10):
    #     I_10 = np.dot(I_10,M[i])
    #     print("第"+str(i+21)+"个矩阵的乘")
    #     print(I_10)
    #     print("\n")

def move(array):
    for i in range(10):
        array[(i+1)%10]+=10
        array=np.dot(array,M[i])
        array[(i+1)%10]-=10
        # print(array)
    return array
    
def generate_matrix_2():
    sub=np.identity(12,int)
    print(sub)    
    for i in range(1,12):
        sub[i-1][i]=-1
    print(sub)
    print(np.dot(distribuition,sub))

    sub_n=np.linalg.inv(sub)
    sub_n=sub_n.round(decimals=4)
    print(sub_n)

    print(np.dot(sub_n,sub))
    for i in range(1,11):
        Mi = np.identity(12)
        Mi[i][i]=0

        Mi[(i-1)%12][i]=0.5
        Mi[(i+1)%12][i]=0.5
        Mi=np.dot(sub_n,Mi)
        Mi=np.dot(Mi,sub)
        print("第"+str(i)+"个矩阵")
        Mi=Mi.round(decimals=4)
        print(Mi)
        print("\n")
        M.append(Mi)

    I_12 = np.identity(12)

    for i in range(10):
        I_12 = np.dot(I_12,M[i])
        print("第"+str(i+1)+"个矩阵的乘")
        I_12=I_12.round(decimals=4)
        print(I_12)
        print("\n")

def generate_matrix_3():
    sub=np.identity(12,int)
    # print(sub)    
    for i in range(1,12):
        sub[i-1][i]=-1
    # print(sub)
    # print(np.dot(distribuition,sub))

    sub_n=np.linalg.pinv(sub)
    for i in range(1,11):
        Mi = np.identity(12)
        Mi[i][i]=0

        Mi[(i-1)%12][i]=0.5
        Mi[(i+1)%12][i]=0.5
        Mi=np.dot(sub_n,Mi)
        Mi=np.dot(sub_n,Mi)
        Mi=np.dot(Mi,sub)
        Mi=np.dot(Mi,sub)
        print("第"+str(i)+"个矩阵")
        Mi=Mi.round(decimals=4)
        print(Mi)
        print("\n")
        M.append(Mi)

        I_12 = np.identity(12)

    for i in range(10):
        I_12 = np.dot(I_12,M[i])
        print("第"+str(i+1)+"个矩阵的乘")
        I_12=I_12.round(decimals=4)
        print(I_12)
        print("\n")

if __name__ == '__main__':
    # show()

    generate_matrix()
    # generate_matrix_2()
    # generate_matrix_3()
    exit()
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
    