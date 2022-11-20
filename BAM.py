import numpy as np
import copy

A1 = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
A2 = [1,1,0,0,1,1,0,0,1,1,0,0,1,1,0]
A3 = [1,1,1,0,0,0,1,1,1,0,0,0,1,1,1]
A4 = [1,1,1,1,0,0,0,0,1,1,1,1,0,0,0]

B1 = [1,1,1,1,0,0,0,0,1,1]
B2 = [1,1,1,0,0,0,1,1,1,0]
B3 = [1,1,0,0,1,1,0,0,1,1]
B4 = [1,0,1,0,1,0,1,0,1,0]

def activation(_list):
    acList = copy.deepcopy(_list)
    for i in range(len(acList)):
        if acList[i] > 0:
            acList[i] = 1
        else:
            acList[i] = 0
    return acList

def bipolar(_list):
    biList = copy.deepcopy(_list)
    for i in range(len(biList)):
        if biList[i] > 0:
            biList[i] = 1
        else:
            biList[i] = -1
    return biList

_A1 = np.array(bipolar(A1))
_A2 = np.array(bipolar(A2))
_A3 = np.array(bipolar(A3))
_A4 = np.array(bipolar(A4))

_B1 = np.array(bipolar(B1))
_B2 = np.array(bipolar(B2))
_B3 = np.array(bipolar(B3))
_B4 = np.array(bipolar(B4))


w1 = []
w2 = []
w3 = []
w4 = []
for j in range(len(_A1)):
    w1.append(_A1[j]*_B1)
    w2.append(_A2[j]*_B2)
    w3.append(_A3[j]*_B3)
    w4.append(_A4[j]*_B4)

w1 = np.array(w1)
w2 = np.array(w2)
w3 = np.array(w3)
w4 = np.array(w4)

weight = w1+w2+w3+w4
print("가중치:\n", weight)
newA1 = np.array(A1[0]*weight[0])
for i in range(1,len(weight)):
    newA1 += np.array(A1[i]*weight[i])
print("\nA1*W:\n",newA1)
acNewA1= np.array(activation(newA1))
print("activation 적용후 \n",acNewA1)

transWeight = np.transpose(weight)
newB1 = np.array(B1[0]*transWeight[0])
for i in range(1,len(transWeight)):
    newB1 += np.array(B1[i]*transWeight[i])
print("\nB1*W:\n",newB1)
acNewB1 = np.array(activation(newB1))
print("activation 적용후 \n",acNewB1)
print("A1 값과 동일하다\n",A1)


################################################################################
# deep copy를 이용하여 리스트 복사 이후 활용할 떄 복사 당한 리스트가 변경되는 것 막음.