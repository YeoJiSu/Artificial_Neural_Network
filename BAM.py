import numpy as np

A1 = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
A2 = [1,1,0,0,1,1,0,0,1,1,0,0,1,1,0]
A3 = [1,1,1,0,0,0,1,1,1,0,0,0,1,1,1]
A4 = [1,1,1,1,0,0,0,0,1,1,1,1,0,0,0]

def activation(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = 1
        else:
            list[i] = 0
    return list

def bipolar(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = 1
        else:
            list[i] = -1
    return list

# def weight(list):
#     w = []
    
#     for i in range(1,len(list)):
#         x = np.array(list[i])
#         for j in range(len(x)):
#             x[j]*x
#     return w

A1 = bipolar(A1)
A2 = bipolar(A2)
A3 = bipolar(A3)
A4 = bipolar(A4)

w = [A1,A2,A3,A4]
# print(weight(w))
     
