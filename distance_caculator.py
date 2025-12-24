
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





