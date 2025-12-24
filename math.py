
'''
Question : 
# # Give a vector write a function that calculates the L-2 Norm of the vector 

# '''
# # -------------------------------------------------------------------------------------

# # import math
# import numpy as np
# def L_2_Norm(vector):
#     v1=np.array(vector)
#     # print(v1,type(v1))
#     v1=v1**2
#     # print(v1)
#     norm=np.sqrt(np.sum(v1))
#     return round(norm,2)

# list=[1,2,3,4]
# print(L_2_Norm(list))


# #-----------------------------------------------------------------------------------------
# # Fastest optimised code using linalg.norm function 
# import numpy as np
# def L_2_Norm(vector):
#     v1=np.array(vector) # This step is redundant when using the lialg.norm function 
#     norm= np.linalg.norm(v1)
#     return round(norm,2)

# if __name__ == '__main__':
# # "Only run this code if this file is executed directly, NOT when it's imported by another file."

#     list=[1,2,3,4,5]
# print(L_2_Norm(list))



'''
Q2:

Given two vectors v1 and v2 write the code to find dot product between then , and andgle between both the vectors 

'''

def dot_product(V1,V2):
    sum=0
    for i in range(len(V1)):
                sum+=V1[i]*V2[i]
    return sum
print(dot_product([1,2,3],[5,6,7]))


import numpy as np
def dot_product_1(V1,V2):
    sum=0
    V1=np.array(V1)
    V2=np.array(V2)
    V=V1*V2  # Vectorized Operation 
    # print(V)
    sum=np.sum(V)
    return sum

# fastest code 
def Dot_prod(V1,V2):
    return sum(a*b for a,b in zip(V1,V2))

# print(Dot_prod([1,2,3],[5,6,7]))

def Norm(V):
    norm=np.sqrt(Dot_prod(V,V))
    return round(norm,2)
print(Norm([1,3,5]))



a=[1,2,3]
b=[4,5,6]
# for a, b in [(1,2)]:
#     print(a*b)


# Angle calculation 
import math
def angle(V1,V2):
     a=Dot_prod(V1,V2)/(Norm(V1)*Norm(V2))
     return math.acos(a)
a=[1,2,3]
b=[4,5,6]
print(angle(a,b))

