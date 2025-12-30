# Question : Write a code to write Gradient Descent from scratch with just numpy:



import numpy as np
def Grad_Desc(X,y,lr=0.01,iters=100):
    n,d=X.shape #This gets the  number of features d and number of samples n
 # Initialising weights randomly here 
    # w=np.random.rand(d) # the shape of weight vector is (d,)
    w=np.zeros(d) #--> more preferred 
    b=0
    for i in range(iters):
        y_pred=np.dot(X,w)+b # nxd into (d,) is (n,)
        error=y-y_pred # shape  is (n,)
        dw=-(2/n)*X.T@(y-y_pred) # shape is  dxn into (n,) -->  (d,)
        db=-(2/n)*np.sum((y-y_pred))
        # Weight update
        w=w-lr*dw  
        b=b-lr*db  
    return w,b



# # Test 1
# import numpy as np

# # Single feature dataset
# X = np.array([[1],
#               [2],
#               [3],
#               [4],
#               [5]], dtype=float)

# y = np.array([3, 5, 7, 9, 11], dtype=float)

# w, b = Grad_Desc(X, y, lr=0.01, iters=2000)

# print("Weight:", w)
# print("Bias:", b)


# Test 2


# Multi-feature dataset
X = np.array([[1, 2],
              [2, 1],
              [3, 4],
              [4, 3],
              [5, 6]], dtype=float)

y = np.array([8, 9, 18, 19, 28], dtype=float)

w, b = Grad_Desc(X, y, lr=0.01, iters=3000)

print("Weights:", w)
print("Bias:", b)


#### MISTAKE ## MISTAKE
'''

Sbase Bada mistake and learning whenever writing multiplication of X and W or X with
any pother like y in weight update get a habbit of wrtting X@W or np.dot()

Its a blunder to use * symbol


db = (2/n) * (y - y_pred)

❌ Problem

db must be a scalar
This gives shape (n,)


# error = y_pred - y   , FAANGs use this convention , not the errors 

'''

