# # Question1 ::  Write a code to calculate the distance of a point / vector X_0 from a plane W^T*X+b ?? 
# import numpy as np
# def distance(W,X,b):
#     X=np.array(X)
#     W=np.array(W)
#     norm_w=np.linalg.norm(W)
#     print(norm_w)
#     distance=(np.sum(W*np.transpose(X))+b)/norm_w
#     return distance

# W=[1,2,3]
# X_0=[4,5,6]
# b=1

# print(distance(W,X_0,b))

'''
Mistakes 
1: Have a habit of writing a case (raise ValueError) if denominator==0
2: What if W and X have different dimensions? , the dimensions must be same for this calculation 
3: Unnecessary transpose and sum : np.transpose(X) on a 1D array does nothing. For vectors, just use W * X directly. 

4:: Give a Keyworded parameter to have option to get the signed distance or absolute distance 

'''

# Better efficeint code :
import numpy as np
def distance(w,x,b,signed=False):
    x=np.array(x)
    w=np.array(w)
    norm=np.linalg.norm(w)
    if norm==0:
        raise ValueError("denominator has become zero so cant calculate distance now ")
    
    if w.shape != x.shape:
        raise ValueError("X and W dimensions doesnot match")
    
    numerator=np.dot(w,x) +b

    if signed:
        distance=numerator/norm
    else: # if used wants absolute distance only
        distance=np.abs(numerator/norm)
    return round(distance,2)

W=[1,2,3]
W=[0,0,0]
X_0=[4,5,6]
b=1
print(distance(W,X_0,b))







# Code Loss/ Cost function for Regression 
'''
Cost function and Loss function difference , 
Docstring for math_24DEC
'''
# Question_2 : Write code to plot x^2 and also its derivative 

# Implement GD from scratch , in Code 

